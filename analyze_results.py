import re, csv, os
import pickle
from run_model import RegularCA
from pybdm import BDM
from pybdm.partitions import PartitionRecursive


wmax = 3
bdm = BDM(ndim=1)
bdm_traj = BDM(ndim=1, nsymbols=8, warn_if_missing_ctm=False, partition=PartitionRecursive)

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

    with open(rule_type + '_results.csv', 'w+') as csvfile:

        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['rule_i', 'ca1_r', 'ca2_r', 'ca1_is', 'ca2_is'])

        for file in list(filter(lambda x: re.search('\d', x), os.listdir(os.path.join('trajectories', rule_type)))):

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
                ca2_inn = ca1_state_traj in eca_trajectories

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
                ca1_bdm = [bdm.bdm(s, normalized=True) for s in ca1_state_traj]
                ca2_bdm = [bdm.bdm(s, normalized=True) for s in ca2_state_traj]

                # max, mean, last few states mean
                ca1_bdm_max = max(ca1_bdm)
                ca2_bdm_max = max(ca2_bdm)
                ca1_bdm_mean = sum(ca1_bdm)/len(ca1_bdm)
                ca2_bdm_mean = sum(ca2_bdm)/len(ca2_bdm)
                ca1_bdm_mean_last = sum(ca1_bdm[-5:])/len(ca1_bdm[-5:])
                ca2_bdm_mean_last = sum(ca2_bdm[-5:]) / len(ca2_bdm[-5:])

                # get bdm for the whole trajectory
                # 2^w states means 2^3 = 8 states, can use one state per symbol here
                ca1_bdm_traj = bdm_traj.bdm(ca1_state_traj, normalized=True)
                ca2_bdm_traj = bdm_traj.bdm(ca2_state_traj, normalized=True)

                # save to file
                ca1_bdm