import re, csv, os
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import pickle
import pandas as pd
from matplotlib.colors import LogNorm
sns.set_style("whitegrid")
from collections import Counter


def make_oee_results(tp, rule_types):

    # results: rule_type, rule_i

    percent_oees = {}

    # load the csv files
    for rule_type in rule_types:

        print(rule_type)
        percent_oees[rule_type] = []
        files = list(filter(lambda x: re.search('\d', x), os.listdir(os.path.join('measurements', rule_type))))

        for file in files:

            interaction_rule_i = file.split('_')[0]
            oee_count_1 = 0
            oee_count_2 = 0
            total_count = 0

            with open(os.path.join('measurements', rule_type, file)) as csvfile:

                csvreader = csv.reader(csvfile)
                try:
                    header = next(csvreader)

                    for i, row in enumerate(csvreader, start=1):
                        if i % 2 == 0:
                            data = dict(zip(header, row))
                            total_count += 1

                            # oee if inn = true and tr > tp
                            if data['ca1_inn'] == 'True' and int(data['tr']) > tp:
                                oee_count_1 += 1
                            if data['ca2_inn'] == 'True' and int(data['tr']) > tp:
                                oee_count_2 += 1

                except:
                    print(file)
                    continue

            percent_oees[rule_type].append((interaction_rule_i, oee_count_1, oee_count_2, total_count))

    results = {}

    # group by interaction rules
    # 3 pairs of high and low rules
    for rule_type in rule_types:

        results[rule_type] = {}

        for i in range(6):
            i_rule = list(filter(lambda x: str(i) == x[0], percent_oees[rule_type]))
            oee_counts_1 = sum(list(map(lambda x: x[1], i_rule)))
            oee_counts_2 = sum(list(map(lambda x: x[2], i_rule)))
            totals = sum(list(map(lambda x: x[3], i_rule)))

            results[rule_type][i] = (oee_counts_1, oee_counts_2, totals)

    pickle.dump(results, open("oee_results", "wb"))


def make_tr_dists(rule_types):

    all_trs = {}

    # load the csv files
    for rule_type in rule_types:

        print(rule_type)
        all_trs[rule_type] = []
        files = list(filter(lambda x: re.search('\d', x), os.listdir(os.path.join('measurements', rule_type))))

        for file in files:

            interaction_rule_i = file.split('_')[0]
            trs = []

            with open(os.path.join('measurements', rule_type, file)) as csvfile:

                try:
                    csvreader = csv.reader(csvfile)
                    header = next(csvreader)

                    for i, row in enumerate(csvreader, start=1):
                        if i % 2 == 0:
                            data = dict(zip(header, row))
                            tr = data['tr']
                            if tr == '':
                                tr = 2*(2**w) + 1
                            trs.append(int(tr))

                except:
                    print(file)
                    continue

            all_trs[rule_type].append((interaction_rule_i, trs))


    results = {}

    # group by interaction rules
    # 3 pairs of high and low rules
    for rule_type in rule_types:

        results[rule_type] = {}

        for i in range(6):
            i_rule = list(filter(lambda x: str(i) == x[0], all_trs[rule_type]))
            tr_counts = list(map(lambda x: x[1], i_rule))
            tr_counts = [item for sublist in tr_counts for item in sublist]
            tr_counts = Counter(tr_counts)

            results[rule_type][i] = tr_counts

    pickle.dump(results, open("tr_dists", "wb"))


def make_bdm_dists_max(rule_types):

    percent_oees = {}

    # load the csv files
    for rule_type in rule_types:

        print(rule_type)
        percent_oees[rule_type] = []
        files = list(filter(lambda x: re.search('\d', x), os.listdir(os.path.join('measurements', rule_type))))

        for file in files:

            interaction_rule_i = file.split('_')[0]
            bdms = []

            with open(os.path.join('measurements', rule_type, file)) as csvfile:

                try:
                    csvreader = csv.reader(csvfile)
                    header = next(csvreader)

                    for i, row in enumerate(csvreader, start=1):
                        if i % 2 == 0:
                            data = dict(zip(header, row))
                            bdm_1 = data['ca1_bdm_max']
                            bdm_2 = data['ca2_bdm_max']
                            bdms.append((float(bdm_1), float(bdm_2)))

                except:
                    print(file)
                    continue

            percent_oees[rule_type].append((interaction_rule_i, bdms))

    results = {}

    # group by interaction rules
    # 3 pairs of high and low rules
    for rule_type in rule_types:

        results[rule_type] = {}

        for i in range(6):
            i_rule = list(filter(lambda x: str(i) == x[0], percent_oees[rule_type]))
            bdms = list(map(lambda x: x[1], i_rule))
            bdms = list(map(lambda x: list(zip(*x)), bdms))
            bdm1_counts = list(map(lambda x: list(x[0]), bdms))
            bdm1_counts = [item for sublist in bdm1_counts for item in sublist]
            bdm1_counts = Counter(bdm1_counts)
            bdm2_counts = list(map(lambda x: list(x[1]), bdms))
            bdm2_counts = [item for sublist in bdm2_counts for item in sublist]
            bdm2_counts = Counter(bdm2_counts)

            results[rule_type][i] = (bdm1_counts, bdm2_counts)

    pickle.dump(results, open("bdm_dists_max", "wb"))


def make_bdm_dists_mean(rule_types):

    percent_oees = {}

    # load the csv files
    for rule_type in rule_types:

        print(rule_type)
        percent_oees[rule_type] = []
        files = list(filter(lambda x: re.search('\d', x), os.listdir(os.path.join('measurements', rule_type))))

        for file in files:

            interaction_rule_i = file.split('_')[0]
            bdms = []

            with open(os.path.join('measurements', rule_type, file)) as csvfile:

                try:
                    csvreader = csv.reader(csvfile)
                    header = next(csvreader)

                    for i, row in enumerate(csvreader, start=1):
                        if i % 2 == 0:
                            data = dict(zip(header, row))
                            bdm_1 = data['ca1_bdm_mean']
                            bdm_2 = data['ca2_bdm_mean']
                            bdms.append((float(bdm_1), float(bdm_2)))

                except:
                    print(file)
                    continue

            percent_oees[rule_type].append((interaction_rule_i, bdms))

    results = {}

    # group by interaction rules
    # 3 pairs of high and low rules
    for rule_type in rule_types:

        results[rule_type] = {}

        for i in range(6):
            i_rule = list(filter(lambda x: str(i) == x[0], percent_oees[rule_type]))
            bdms = list(map(lambda x: x[1], i_rule))
            bdms = list(map(lambda x: list(zip(*x)), bdms))
            bdm1_counts = list(map(lambda x: list(x[0]), bdms))
            bdm1_counts = [item for sublist in bdm1_counts for item in sublist]
            bdm1_counts = Counter(bdm1_counts)
            bdm2_counts = list(map(lambda x: list(x[1]), bdms))
            bdm2_counts = [item for sublist in bdm2_counts for item in sublist]
            bdm2_counts = Counter(bdm2_counts)

            results[rule_type][i] = (bdm1_counts, bdm2_counts)

    pickle.dump(results, open("bdm_dists_mean", "wb"))


def make_bdm_dists_last(rule_types):

    percent_oees = {}

    # load the csv files
    for rule_type in rule_types:

        print(rule_type)
        percent_oees[rule_type] = []
        files = list(filter(lambda x: re.search('\d', x), os.listdir(os.path.join('measurements', rule_type))))

        for file in files:

            interaction_rule_i = file.split('_')[0]
            bdms = []

            with open(os.path.join('measurements', rule_type, file)) as csvfile:

                try:
                    csvreader = csv.reader(csvfile)
                    header = next(csvreader)

                    for i, row in enumerate(csvreader, start=1):
                        if i % 2 == 0:
                            data = dict(zip(header, row))
                            bdm_1 = data['ca1_bdm_mean_last']
                            bdm_2 = data['ca2_bdm_mean_last']
                            bdms.append((float(bdm_1), float(bdm_2)))

                except:
                    print(file)
                    continue

            percent_oees[rule_type].append((interaction_rule_i, bdms))

    results = {}

    # group by interaction rules
    # 3 pairs of high and low rules
    for rule_type in rule_types:

        results[rule_type] = {}

        for i in range(6):
            i_rule = list(filter(lambda x: str(i) == x[0], percent_oees[rule_type]))
            bdms = list(map(lambda x: x[1], i_rule))
            bdms = list(map(lambda x: list(zip(*x)), bdms))
            bdm1_counts = list(map(lambda x: list(x[0]), bdms))
            bdm1_counts = [item for sublist in bdm1_counts for item in sublist]
            bdm1_counts = Counter(bdm1_counts)
            bdm2_counts = list(map(lambda x: list(x[1]), bdms))
            bdm2_counts = [item for sublist in bdm2_counts for item in sublist]
            bdm2_counts = Counter(bdm2_counts)

            results[rule_type][i] = (bdm1_counts, bdm2_counts)

    pickle.dump(results, open("bdm_dists_mean_last", "wb"))


def make_bdm_dists_traj(rule_types):

    percent_oees = {}

    # load the csv files
    for rule_type in rule_types:

        print(rule_type)
        percent_oees[rule_type] = []
        files = list(filter(lambda x: re.search('\d', x), os.listdir(os.path.join('measurements', rule_type))))

        for file in files:

            interaction_rule_i = file.split('_')[0]
            bdms = []

            with open(os.path.join('measurements', rule_type, file)) as csvfile:

                try:
                    csvreader = csv.reader(csvfile)
                    header = next(csvreader)

                    for i, row in enumerate(csvreader, start=1):
                        if i % 2 == 0:
                            data = dict(zip(header, row))
                            bdm_1 = data['ca1_bdm_traj']
                            bdm_2 = data['ca2_bdm_traj']
                            bdms.append((float(bdm_1), float(bdm_2)))

                except:
                    print(file)
                    continue

            percent_oees[rule_type].append((interaction_rule_i, bdms))

    results = {}

    # group by interaction rules
    # 3 pairs of high and low rules
    for rule_type in rule_types:

        results[rule_type] = {}

        for i in range(6):
            i_rule = list(filter(lambda x: str(i) == x[0], percent_oees[rule_type]))
            bdms = list(map(lambda x: x[1], i_rule))
            bdms = list(map(lambda x: list(zip(*x)), bdms))
            bdm1_counts = list(map(lambda x: list(x[0]), bdms))
            bdm1_counts = [item for sublist in bdm1_counts for item in sublist]
            bdm1_counts = Counter(bdm1_counts)
            bdm2_counts = list(map(lambda x: list(x[1]), bdms))
            bdm2_counts = [item for sublist in bdm2_counts for item in sublist]
            bdm2_counts = Counter(bdm2_counts)

            results[rule_type][i] = (bdm1_counts, bdm2_counts)

    pickle.dump(results, open("bdm_dists_traj", "wb"))


# --------------------------------

if __name__ == "__main__":

    w = 3
    tp = 2 ** w
    rule_types = ['both_states', 'this_state', 'other_state', 'mixed']

    # load in interaction rule bdms
    both_rules_use = pickle.load(open("both_rules_use", "rb"))
    one_rules_use = pickle.load(open("one_rules_use", "rb"))

    # get numbers to plot

    # CAN'T GET BDM OF MIXED RULE

    # FIGURE of % OEE cases for each of the four interaction rule types

    #make_oee_results(tp, rule_types)
    oee_results = pickle.load(open("oee_results", "rb"))
    # Bar chart with 4 bars, one for each type
    # Bar chart with 6 bars, 4 charts, one per type


    # FIGURE of distribution of trs

    #make_tr_dists(rule_types)
    tr_dists = pickle.load(open("tr_dists", "rb"))
    # One histogram plot, one dist per type, overlaid
    # 4 histogram plots, 6 dists per type, 4 panels


    # FIGURE of the BDMs of state trajectories VS BDMs of the interaction rules for both encodings of state trajectories

    #make_bdm_dists_max(rule_types)
    bdm_dists_max = pickle.load(open("bdm_dists_max", "rb"))
    #make_bdm_dists_mean(rule_types)
    bdm_dists_mean = pickle.load(open("bdm_dists_mean", "rb"))
    #make_bdm_dists_last(rule_types)
    bdm_dists_last = pickle.load(open("bdm_dists_mean_last", "rb"))
    #make_bdm_dists_traj(rule_types)
    bdm_dists_traj = pickle.load(open("bdm_dists_traj", "rb"))

    # interaction rule complexities
    both_rules_bdms = list(map(lambda x: x[1], both_rules_use))
    one_rules_bdms = list(map(lambda x: x[1], one_rules_use))

    # Single violin plot, each type is a violin, the BDMs of each type are overlaid (6 points per violin), 2 y axes
    # 4 panels of violin plots, 6 violins, one dot overlaid on each


    # FIGURE of rule complexity vs \% OEE cases
    # 2-panel scatterplot, BDM of rule on x, %oee on y, one panel per interaction type
