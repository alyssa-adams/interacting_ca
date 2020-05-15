import re, csv, os
import pickle
from run_model import RegularCA
from pybdm import BDM
import networkx as nx


wmax = 4

# ============ ECA trajectories ==============

# instantiate eca class instance
regularCA = RegularCA()

# make the ECA update rule lookup tables
rules = regularCA.make_rules()

# do all ecas, these are the trajectories needed to compare
ecas = regularCA.run_all_ecas(wmax)


# ============ Compare to ICA trajectories ==============

rule_types = ['both_states', 'this_state', 'other_state', 'mixed']

# load the pickle files
for file in list(filter(lambda x: re.split('_\d', x)[0] in ['both_states', 'this_state', 'other_state', 'mixed'], os.listdir('.'))):

    data = pickle.load(open(file, "rb"))
    rule_type = file.split()[0]
    ca1_w = file.split()[1]
    ca2_w = file.split()[2]
    i = file.split()[4]
    interaction_rule_1 = data['interaction_rule_1']
    interaction_rule_2 = data['interaction_rule_2']
    states_rules_trajectories = data['states_rules_trajectories']

    # get bdm for interaction rules
    g_interaction_rule_1 = nx.Graph()
    g_interaction_rule_1.add_edges_from(interaction_rule_1)
    g_interaction_rule_2 = nx.Graph()
    g_interaction_rule_2.add_edges_from(interaction_rule_2)
    adj1 = nx.adjacency_matrix(g_interaction_rule_1)
    adj2 = nx.adjacency_matrix(g_interaction_rule_2)

    bdm = BDM(ndim=2)
    bdm_interaction_rule_1 = bdm(adj1)
    bdm_interaction_rule_2 = bdm(adj2)

    for sr in states_rules_trajectories:

        ica_states = sr['ica_states']
        ica_rules = sr['ica_rules']

        ca1_states = list(map(lambda x: x[0], ica_states))
        ca2_states = list(map(lambda x: x[1], ica_states))
        ca1_rules = list(map(lambda x: x[0], ica_rules))
        ca2_rules = list(map(lambda x: x[1], ica_rules))

        # is it oee: Is tr > tp and is it innovative?
        # is state trajectory in ecas?
        # Does s+r of CA occur more than once?

        # get bdm for each state
        # max, mean, last few states mean

        # get bdm for the whole trajectory


