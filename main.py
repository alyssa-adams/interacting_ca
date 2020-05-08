import pickle
from itertools import product
import random


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

        # for different widths
        for w in range(3, wmax+1):

            eca_states[w] = {}

            # get all possible initial states
            state0s = regularCA.make_state0s(w)

            # for all possible rules,
            for r in range(256):

                eca_states[w][r] = {}

                # and all possible initial states,
                for i in state0s:

                    states = []
                    state_now = i

                    for t in range(2 ** w + 1):
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

        # get all possible initial states for both ca sizes
        ca1_state0s = regularCA.make_state0s(ca1_w)
        if ca1_w == ca2_w:
            ca2_state0s = ca1_state0s
        else:
            ca2_state0s = regularCA.make_state0s(ca2_w)

        # for each initial state for ca1,
        for i in ca1_state0s:

            # and for each initial state for ca2,
            for j in ca2_state0s:

                states = []
                state_now = (i, j)
                rules_now = (ca1_r, ca2_r)

                for t in range(2 * (2 ** max(ca1_w, ca2_w)) + 1):

                    # save old state
                    states.append(state_now)
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
                        rule_now_1 = interaction_rule_1[random.choice([(state_now_1, state_now_2), state_now_1, state_now_2])]
                        rule_now_2 = interaction_rule_2[random.choice([(state_now_1, state_now_2), state_now_1, state_now_2])]

                    rules_now = (rule_now_1, rule_now_2)

                ica_states.append(states)

        return ica_states


    def run_all_icas(self, wmax, rule_type):

        '''
        Runs all interactions over all widths, rules, and initial states for each ca for some interaction rule type
        :param wmax: max width to include
        :param rule_type: one of the following ['both_states', 'this_state', 'other_state', 'mixed']
        :return:
        '''

        # loop over all interaction rules and widths and initial rules
        if rule_type == 'both_states':
            interaction_rule_1 = interatingCA.make_interaction_rules(wmax)['both_states']
            interaction_rule_2 = interatingCA.make_interaction_rules(wmax)['both_states']
        elif rule_type == 'this_state' or 'other_state':
            interaction_rule_1 = interatingCA.make_interaction_rules(wmax)['one_state']
            interaction_rule_2 = interatingCA.make_interaction_rules(wmax)['one_state']
        elif rule_type == 'mixed':
            interaction_rule_1 = interatingCA.make_interaction_rules(wmax)
            interaction_rule_1 = {**interaction_rule_1['both_states'], **interaction_rule_1['one_state']}
            interaction_rule_2 = interatingCA.make_interaction_rules(wmax)
            interaction_rule_2 = {**interaction_rule_2['both_states'], **interaction_rule_2['one_state']}

        icas_all = {}

        for ca1_w in range(3, wmax + 1):

            icas_all[ca1_w] = {}

            for ca2_w in range(3, wmax + 1):

                icas_all[ca1_w][ca2_w] = {}

                for ca1_r in range(256):

                    icas_all[ca1_w][ca2_w][ca1_r] = {}

                    for ca2_r in range(256):

                        icas = interatingCA.run_both_icas(ca1_w, ca2_w, ca1_r, ca2_r, interaction_rule_1,
                                                          interaction_rule_2, rule_type)
                        icas_all[ca1_w][ca2_w][ca1_r][ca2_r] = icas

        results = {
            'rule_type': rule_type,
            'interaction_rule_1': interaction_rule_1,
            'interaction_rule_2': interaction_rule_2,
            'icas_all': icas_all
        }

        return results


# --------------------------------

# ============ ECA trajectories ==============

# instantiate eca class instance
regularCA = RegularCA()

# make the ECA update rule lookup tables
rules = regularCA.make_rules()

# do all ecas, these are the trajectories needed to compare
wmax = 4
ecas = regularCA.run_all_ecas(wmax)


# ============ interacting CA trajectories ==============

# make all a set of interaction rules
interatingCA = InteractingCA()

# save results to dict
rule_types = ['both_states', 'this_state', 'other_state', 'mixed']

for rule_type in rule_types:
    print(rule_type)
    results = interatingCA.run_all_icas(wmax, rule_type)

    # save resulting dict to pickle file
    pickle.dump(results, open(rule_type, "wb"))
