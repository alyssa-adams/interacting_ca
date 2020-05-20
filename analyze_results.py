import re, csv, os
import pickle
from run_model import RegularCA
from pybdm import BDM
from pybdm.partitions import PartitionRecursive
import numpy as np


wmax = 3
bdm = BDM(ndim=1, warn_if_missing_ctm=False, partition=PartitionRecursive)
bdm_traj = BDM(ndim=1, nsymbols=9, warn_if_missing_ctm=False, partition=PartitionRecursive)

# map states to integers
ks = ['111', '110', '101', '100', '011', '010', '001', '000']
vs = list(range(8))
states_ints_map = dict(zip(ks, vs))

# only use the 88 unique ca rules for this analysis, since it's taking a while to come up with results
# (will reduce redundancy anyways)
use_these_rules = [0, 1, 4, 5, 18, 19, 22, 23, 32, 33, 36, 37, 50, 51, 54, 55, 72, 73, 76, 77, 90, 91, 94, 95, 104, 105, 108, 109, 122, 123, 126, 127, 128, 129, 132, 133, 146, 147, 150, 151, 160, 161, 164, 165, 178, 179, 182, 183, 200, 201, 204, 205, 218, 219, 222, 223, 232, 233, 236, 237, 250, 251, 254, 255]

# ============ ECA trajectories ==============

# instantiate eca class instance
regularCA = RegularCA()

# make the ECA update rule lookup tables
rules = regularCA.make_rules()

# do all ecas, these are the trajectories needed to compare
ecas = regularCA.run_all_ecas(wmax)
eca_trajectories = [list(ic.values()) for ic in ecas[3].values()]
eca_trajectories = [item for sublist in eca_trajectories for item in sublist]


# ============ Compare to ICA trajectories ==============

rule_types = ['both_states', 'this_state', 'other_state', 'mixed']

# load the pickle files
for rule_type in rule_types:

    print(rule_type)

    files = list(filter(lambda x: re.search('\d', x), os.listdir(os.path.join('trajectories', rule_type))))
    files = list(filter(lambda x: int(x.split('_')[3]) in use_these_rules and int(x.split('_')[4]) in use_these_rules, files))

    for file in files:

        with open(os.path.join('measurements', rule_type, file + '_results.csv'), 'w+') as csvfile:

            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['ca1_inn', 'ca2_inn', 'tr',
                                'ca1_bdm_max', 'ca2_bdm_max', 'ca1_bdm_mean', 'ca2_bdm_mean', 'ca1_bdm_mean_last',
                                'ca2_bdm_mean_last', 'ca1_bdm_traj', 'ca2_bdm_traj'])

            print(file)

            # load in file
            data = pickle.load(open(os.path.join('trajectories', rule_type, file), "rb"))

            # parse model info
            rule_i = file.split('_')[0]
            ca1_r = file.split('_')[3]
            ca2_r = file.split('_')[4]

            # parse data
            ica_states = data['ica_states']
            ica_rules = data['ica_rules']

            # loop over each initial state
            for i, initial_state in enumerate(ica_states):

                # individual trajectories
                ca1_state_traj = list(map(lambda x: x[0], initial_state))
                ca2_state_traj = list(map(lambda x: x[1], initial_state))
                ca1_rule_traj = list(map(lambda x: x[0], ica_rules[i]))
                ca2_rule_traj = list(map(lambda x: x[1], ica_rules[i]))

                # is it oee: Is tr > tp and is it innovative?
                # is state trajectory in ecas?
                ca1_inn = ca1_state_traj in eca_trajectories
                ca2_inn = ca2_state_traj in eca_trajectories

                # Does s+r of CA occur more than once?
                # get state-rule pairs for each ca, see when there's a repeat
                srs = tuple(zip(ca1_state_traj, ca2_state_traj, ca1_rule_traj, ca2_rule_traj))

                # check for repeating sr
                # if no tr is found, then tr is greater than 2*2^w
                tr = None
                for sr in srs:
                    sr_rep = [i for i, x in enumerate(srs) if x == sr]
                    if len(sr_rep) > 1:
                        tr = sr_rep[1]  # this means it repeats after THIS many time steps

                # get bdm for each state
                ca1_bdm = [bdm.bdm(np.array(list(s), dtype=int), normalized=True) for s in ca1_state_traj]
                ca2_bdm = [bdm.bdm(np.array(list(s), dtype=int), normalized=True) for s in ca2_state_traj]

                # max, mean, last few states mean
                ca1_bdm_max = max(ca1_bdm)
                ca2_bdm_max = max(ca2_bdm)
                ca1_bdm_mean = sum(ca1_bdm)/len(ca1_bdm)
                ca2_bdm_mean = sum(ca2_bdm)/len(ca2_bdm)
                ca1_bdm_mean_last = sum(ca1_bdm[-5:])/len(ca1_bdm[-5:])
                ca2_bdm_mean_last = sum(ca2_bdm[-5:]) / len(ca2_bdm[-5:])

                # get bdm for the whole trajectory
                # 2^w states means 2^3 = 8 states, can use one state per symbol here
                ca1_bdm_traj = bdm_traj.bdm(np.array([states_ints_map[s] for s in ca1_state_traj]), normalized=True)
                ca2_bdm_traj = bdm_traj.bdm(np.array([states_ints_map[s] for s in ca2_state_traj]), normalized=True)

                # save to file
                data_row = [ca1_inn, ca2_inn, tr, ca1_bdm_max, ca2_bdm_max, ca1_bdm_mean, ca2_bdm_mean, ca1_bdm_mean_last, ca2_bdm_mean_last, ca1_bdm_traj, ca2_bdm_traj]

                csvwriter.writerow(data_row)
