from os import O_CLOEXEC
import pickle
import collections
import matplotlib.pyplot as plot

def plot_accuracies_per_class():
    with open('accuracy_map.pyobj', 'rb') as in_file:
        accuracies = pickle.load(in_file)
    o_accs = collections.OrderedDict(sorted(accuracies.items()))
    labels = list()
    values = list()

    for key in o_accs:
        labels.append(key)
        values.append(o_accs[key])
    
    plot.bar(labels, values, color='tab:orange')
    plot.xlabel('class name')
    plot.ylabel('accuracy')
    plot.title('Accuracies per class')
    plot.savefig("./plots/acc_per_class")
    plot.clf()


plot_accuracies_per_class()
