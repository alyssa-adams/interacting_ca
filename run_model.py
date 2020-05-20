import pickle
import os
from itertools import product
import random
from pybdm import BDM
import networkx as nx


# This models two elementary cellular automata that interact with each other
# they change their rules based on number of states
# Count the number of "open-ended" cases by comparing to regular ECA

# Apparent open-ended criteria:
# Innovative (unique state trajectories) and takes longer than 2^w steps to repeat

class RegularCA:

    def make_rules(self):

        '''
        Makes the ECA rules 0-255
        :return: Dict of rules
        '''

        neighbs = ['111', '110', '101', '100', '011', '010', '001', '000']
        binaries = ["{0:08b}".format(i) for i in range(256)]
        newneighbs = list(map(lambda x: list(x), binaries))

        rules = {}
        for i in range(256):
            rules[i] = dict(zip(neighbs, newneighbs[i]))

        return rules


    def make_state0s(self, w):

        '''
        Makes all possible initial states for a CA for some width
        :param w: width
        :return: list of strings of initial states
        '''

        perms = list(product('01', repeat=w))
        perms = list(map(lambda x: ''.join(x), perms))

        return perms


    def run_all_ecas(self, wmax):

        '''
        Run all possible ECAs, all possible initial states and all possible initial rules
        :return: Dict of width, rule, initial state, list of states
        '''

        # save results to a dict
        eca_states = {}

        rules = self.make_rules()

        # for different widths
        for w in range(3, wmax+1):

            eca_states[w] = {}

            # get all possible initial states
            state0s = self.make_state0s(w)

            # for all possible rules,
            for r in range(256):

                eca_states[w][r] = {}

                # and all possible initial states,
                for i in state0s:

                    states = []
                    state_now = i

                    for t in range(2 * (2 ** w + 1) - 1):
                        # save old state
                        states.append(state_now)

                        state_wrapped = i + i[:-1]
                        state_broken = [state_wrapped[i:i + 3] for i in range(len(state_wrapped) - 2)]
                        state_new = [rules[r][neighb] for neighb in state_broken]
                        state_now = ''.join(state_new)

                    eca_states[w][r][i] = states

        return eca_states


class InteractingCA:

    def make_interaction_rules(self, wmax):

        '''
        Make some interaction rules from networks
        max: max width to iterate over (but included)
        :return: Dict of rules {both states always, only one state}
        '''

        # save results to a dict
        interaction_rules = {
            'both_states': '',
            'one_state': ''
        }

        # ----- both states always -----

        # make list of all possible states
        states = []
        for w in range(3, wmax+1):
            s = RegularCA().make_state0s(w)
            [states.append(i) for i in s]

        # all possible pairs as nodes
        nodes1 = [p for p in product(states, repeat=2)]

        # the other nodes in the bipartite network
        nodes2 = range(256)

        # make one random out-edge PER state-pair node
        edges = {}
        for node in nodes1:
            out_node = random.choice(nodes2)
            edges[node] = out_node

        interaction_rules['both_states'] = edges


        # ----- one state only -----

        # make one random out-edge PER state node
        edges = {}
        for node in states:
            out_node = random.choice(nodes2)
            edges[node] = out_node

        interaction_rules['one_state'] = edges

        return interaction_rules


    def run_both_icas(self, ca1_w, ca2_w, ca1_r, ca2_r, interaction_rule_1, interaction_rule_2, rule_type):

        '''
        Run all possible CA interaction couples, all possible initial states and all possible initial rules
        :param ca1_w: ca1 width
        :param ca2_w: ca2 width
        :param ca1_r: ca1 initial rule
        :param ca2_r: ca2 initial rule
        :param interaction_rule_1: ca1 interaction rule
        :param interaction_rule_2: ca2 interaction rule
        :param rule_type: interaction rule type: one of from this list: ['both_states', 'this_state', 'other_state', 'mixed']
        :return: Dict of width, rule, initial state, list of states
        '''

        # save results to a dict
        ica_states = []
        ica_rules = []

        # get all possible initial states for both ca sizes
        ca1_state0s = regularCA.make_state0s(ca1_w)
        if ca1_w == ca2_w:
            ca2_state0s = ca1_state0s
        else:
            ca2_state0s = regularCA.make_state0s(ca2_w)

        # for mixed, mix up the rules here
        if rule_type == 'mixed':
            interaction_rule = {**random.choice(interaction_rule_1)[0], **interaction_rule_2[0]}

        # for each initial state for ca1,
        for i in ca1_state0s:

            # and for each initial state for ca2,
            for j in ca2_state0s:

                states = []
                rs = []
                states_now = (i, j)
                rules_now = (ca1_r, ca2_r)

                for t in range(2 * (2 ** max(ca1_w, ca2_w)) + 1):

                    # save old state
                    states.append(states_now)
                    rs.append(rules_now)
                    state_wrapped_1 = i + i[:2]
                    state_wrapped_2 = j + j[:2]
                    state_broken_1 = [state_wrapped_1[x:x + 3] for x in range(len(state_wrapped_1) - 2)]
                    state_broken_2 = [state_wrapped_2[x:x + 3] for x in range(len(state_wrapped_2) - 2)]
                    state_new_1 = [rules[rules_now[0]][neighb] for neighb in state_broken_1]
                    state_new_2 = [rules[rules_now[1]][neighb] for neighb in state_broken_2]
                    state_now_1 = ''.join(state_new_1)
                    state_now_2 = ''.join(state_new_2)

                    # check interaction rule type ['both_states', 'this_state', 'other_state', 'mixed']
                    if rule_type == 'both_states':
                        rule_now_1 = interaction_rule_1[(state_now_1, state_now_2)]
                        rule_now_2 = interaction_rule_2[(state_now_1, state_now_2)]
                    elif rule_type == 'this_state':
                        rule_now_1 = interaction_rule_1[state_now_1]
                        rule_now_2 = interaction_rule_2[state_now_2]
                    elif rule_type == 'other_state':
                        rule_now_1 = interaction_rule_1[state_now_2]
                        rule_now_2 = interaction_rule_2[state_now_1]
                    elif rule_type == 'mixed':
                        # randomly pick a type
                        rule_now_1 = interaction_rule[random.choice([(state_now_1, state_now_2), state_now_1, state_now_2])]
                        rule_now_2 = interaction_rule[random.choice([(state_now_1, state_now_2), state_now_1, state_now_2])]

                    states_now = (state_now_1, state_now_2)
                    rules_now = (rule_now_1, rule_now_2)

                ica_states.append(states)
                ica_rules.append(rs)

        return ica_states, ica_rules


    def run_all_icas(self, wmax, rule_type):

        '''
        Runs all interactions over all widths, rules, and initial states for each ca for some interaction rule type
        :param wmax: max width to include
        :param rule_type: one of the following ['both_states', 'this_state', 'other_state', 'mixed']
        :return: None, just saves to file
        '''

        # load in interaction rules based on interaction rule type

        # loop over all interaction rules and widths and initial rules
        if rule_type == 'both_states':
            interaction_rules = pickle.load(open('both_rules_use', "rb"))
        elif rule_type == 'this_state' or rule_type == 'other_state':
            interaction_rules = pickle.load(open('one_rules_use', "rb"))
            # make pairs of interaction rules
            interaction_rules = list(zip(interaction_rules[0::2], interaction_rules[1::2]))
        elif rule_type == 'mixed':
            r1 = pickle.load(open('one_rules_use', "rb"))
            r1 = list(zip(r1[0::2], r1[1::2]))
            # put together later
            r2 = pickle.load(open('both_rules_use', "rb"))
            interaction_rules = r1
        else:
            interaction_rules = None

        # 6 interaction rules, three high and three low
        for i, rule_pair in enumerate(interaction_rules):

            for ca1_w in range(3, wmax):

                for ca2_w in range(3, wmax):

                    for ca1_r in range(256):

                        for ca2_r in range(256):

                            # loop over all possible initial states for both CA

                            if rule_type == 'both_states':
                                ica_states, ica_rules = interactingCA.run_both_icas(ca1_w, ca2_w, ca1_r, ca2_r,
                                                                                    rule_pair[0],
                                                                                    rule_pair[0], rule_type)
                            elif rule_type == 'this_state' or rule_type == 'other_state':
                                ica_states, ica_rules = interactingCA.run_both_icas(ca1_w, ca2_w, ca1_r, ca2_r,
                                                                                    rule_pair[0][0],
                                                                                    rule_pair[1][0], rule_type)
                            elif rule_type == 'mixed':
                                # put the rules together so that they randomly choose at each time step
                                ica_states, ica_rules = interactingCA.run_both_icas(ca1_w, ca2_w, ca1_r, ca2_r,
                                                                                    rule_pair,
                                                                                    r2[i], rule_type)

                            results = {
                                'ica_states': ica_states,
                                'ica_rules': ica_rules
                                        }

                            # save resulting dict to pickle file
                            dir = 'trajectories'
                            filename = str(i)+'_'+str(ca1_w)+'_'+str(ca2_w)+'_'+str(ca1_r)+'_'+str(ca2_r)
                            pickle.dump(results, open(os.path.join(dir, rule_type, filename), "wb"))
                            print(filename)

        return None


    def pick_interaction_rules(self, wmax):

        '''
        Make 1000 interaction rules, measures the 2d bdm, then picks the top 3 highest and lowest
        :param wmax: max width of CA states
        :return: None, just saves rules to pickle files
        '''

        # make a thousand, then pick from dist
        both_interaction_rules = []
        one_interaction_rules = []

        # Since these are randomly generated, they are almost guaranteed to have LOW bdm values
        # TODO: In the future, get a better way of getting an algorithmic distribution of interaction rules
        for i in range(5000):

            interaction_rules = self.make_interaction_rules(wmax)
            rule_both = interaction_rules['both_states']
            rule_one = interaction_rules['one_state']

            # get bdm
            rule_both_graph = nx.Graph()
            rule_both_graph.add_edges_from(rule_both.items())
            adj_both = nx.adjacency_matrix(rule_both_graph)
            rule_one_graph = nx.Graph()
            rule_one_graph.add_edges_from(rule_one.items())
            adj_one = nx.adjacency_matrix(rule_one_graph)

            bdm_graphs = BDM(ndim=2)
            bdm_interaction_rule_both = bdm_graphs.bdm(adj_both.toarray(), normalized=True)
            bdm_interaction_rule_one = bdm_graphs.bdm(adj_one.toarray(), normalized=True)

            both_interaction_rules.append((rule_both, bdm_interaction_rule_both))
            one_interaction_rules.append((rule_one, bdm_interaction_rule_one))

        # sort by BDM value
        both_interaction_rules.sort(key=lambda x: x[1])
        one_interaction_rules.sort(key=lambda x: x[1])

        # pick top and bottom three
        both_rules_use = []
        both_rules_use.append(both_interaction_rules[:3])
        both_rules_use.append(both_interaction_rules[-3:])
        both_rules_use = [item for sublist in both_rules_use for item in sublist]

        # pick top and bottom three PAIRS
        one_rules_use = []
        one_rules_use.append(one_interaction_rules[:6])
        one_rules_use.append(one_interaction_rules[-6:])
        one_rules_use = [item for sublist in one_rules_use for item in sublist]

        # save rules to file
        pickle.dump(both_rules_use, open('both_rules_use', "wb"))
        pickle.dump(one_rules_use, open('one_rules_use', "wb"))

        return None


# --------------------------------

if __name__ == "__main__":

    # TODO: Eventually, make this bigger and run more experiments
    wmax = 3

    # ============ ECA trajectories ==============

    # instantiate eca class instance
    regularCA = RegularCA()

    # make the ECA update rule lookup tables
    rules = regularCA.make_rules()

    # do all ecas, these are the trajectories needed to compare
    ecas = regularCA.run_all_ecas(wmax)


    # ============ interacting CA trajectories ==============

    # make all a set of interaction rules
    interactingCA = InteractingCA()

    # save results to dict
    rule_types = ['both_states', 'this_state', 'other_state', 'mixed']
    rule_types = ['mixed']

    # this make the interaction rules, comment this out for running CAs
    #interactingCA.pick_interaction_rules(wmax)

    # comment this out when making the interaction rules
    for rule_type in rule_types:
        interactingCA.run_all_icas(wmax, rule_type)
