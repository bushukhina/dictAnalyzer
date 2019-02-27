from sys import argv
from analyzers.timeAnalyzer import TimeAnalyser
from analyzers.dataGenerator import DataGenerator
from analyzers.memoryAnalyzer import MemoryAnalyzer
from dict_classes.ListBased import LinearSearchDictionary, \
    BinarySearchDictionary
from dict_classes.HashTableBased import HashTableDictionary
from dict_classes.TreeBased import BalancedTreeDictionary, BinaryTreeDictionary
import matplotlib.pyplot as plt


dict_types = [BinarySearchDictionary,
              HashTableDictionary,
              BinaryTreeDictionary,
              BalancedTreeDictionary,
              dict]

# memory_size = {}
# set_time = {}
get_time = {}
# del_time = {}
# items_time = {}
# keys_time = {}
# values_time = {}


def full_with_default_values():
    for dt in dict_types:
        # set_time[dt] = {}
        get_time[dt] = {}
        # del_time[dt] = {}
        # items_time[dt] = {}
        # keys_time[dt] = {}
        # values_time[dt] = {}
        # memory_size[dt] = {}


def rewrite_time_measure_results(time_analyzer, data_size):
    for i in range(len(dict_types)):
        dt = dict_types[i]
        # set_time[dt][data_size] = time_analyzer.time_set[i]
        get_time[dt][data_size] = time_analyzer.time_get[i]
        # del_time[dt][data_size] = time_analyzer.time_del[i]
        # items_time[dt][data_size] = time_analyzer.time_items[i]
        # keys_time[dt][data_size] = time_analyzer.time_keys[i]
        # values_time[dt][data_size] = time_analyzer.time_values[i]


# def rewrite_memory_measure_results(results, data_size):
#     for i in range(len(dict_types)):
#         dt = dict_types[i]
#         memory_size[dt][data_size] = results[i]


def draw_single_plot(d, label1, label2, plot_title, k):
    for v in d.values():
        plt.plot(v.keys(), [i * k for i in v.values()], 'o')
    # plt.legend(["LS", "BS", "HT", "BinT", "BalT", "d"],  loc='best')
        plt.legend(["BS", "HT", "BinT", "BalT", "d"], loc='best')
    plt.xlabel(label1)
    plt.ylabel(label2)
    plt.title(plot_title)
    # plt.show()
    plt.savefig(plot_title + ".png")
    plt.clf()


def make_plots():
    # draw_single_plot(set_time, "DATA SIZE", "SECONDSe-03",
    #                  "SET OPERATION 2", 10 ** 3)
    draw_single_plot(get_time, "DATA SIZE", "SECONDSe-03",
                     "GET OPERATION", 10 ** 3)
    # draw_single_plot(del_time, "DATA SIZE", "SECONDSe-03",
    #                  "DEL OPERATION", 10 ** 3)
    # draw_single_plot(items_time,
    #                  "DATA SIZE", "SECONDSe-06", "ITEMS OPERATION", 10 ** 6)
    # draw_single_plot(keys_time, "DATA SIZE", "SECONDSe-06",
    #                  "KEYS OPERATION", 10 ** 6)
    # draw_single_plot(values_time,
    #                  "DATA SIZE", "SECONDSe-06", "VALUES OPERATION", 10 ** 6)
    # draw_single_plot(memory_size, "DATA SIZE", "BYTES", "MEMORY SIZE", 1)


if __name__ == '__main__':
    if len(argv) > 1 and argv[1] == '--measuring':
        dg = DataGenerator(10000, 25000, 50000, 100000, 200000)
        full_with_default_values()
        for data in reversed(dg.data_sets):
            """TIME MEASURES"""
            print(len(data))
            t_a = TimeAnalyser(data)
            t_a.run_for_all()
            rewrite_time_measure_results(t_a, len(data))
            """MEMORY MEASURES"""
            # m_a = MemoryAnalyzer(data)
            # m_a.run_for_all()
            # rewrite_memory_measure_results(m_a.result, len(data))
        make_plots()
        with open("results.txt", "w") as f:
            # f.write("memory\n" + str(memory_size))
            # f.write("\n\nset\n" + str(set_time))
            f.write("\n\nget\n" + str(get_time))
            # f.write("\n\ndel\n" + str(del_time))
            # f.write("\n\nitems\n" + str(items_time))
            # f.write("\n\nkeys\n" + str(keys_time))
            # f.write("\n\nvalues \n" + str(values_time))
