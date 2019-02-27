import timeit
from dict_classes.ListBased import LinearSearchDictionary, \
    BinarySearchDictionary
from dict_classes.HashTableBased import HashTableDictionary
from dict_classes.TreeBased import BalancedTreeDictionary, BinaryTreeDictionary

# dict_types = [,
dict_types = [BinarySearchDictionary,
              HashTableDictionary,
              BinaryTreeDictionary,
              BalancedTreeDictionary,
              dict]

operation_count = 1


class TimeAnalyser:
    def __init__(self, data):
        self.data = data

        self.time_get = []
        # self.time_set = []
        # self.time_del = []
        # self.time_items = []
        # self.time_keys = []
        # self.time_values = []

    def run_for_all(self):
        for dict_type in dict_types:
            # self.make_time_set(dict_type)
            self.make_time_get(dict_type)
            # self.make_time_del(dict_type)
            # self.make_time_items(dict_type)
            # self.make_time_keys(dict_type)
            # self.make_time_values(dict_type)

    # def make_time_set(self, dict_type):
    #     time = 0
    #     for ones in range(operation_count):
    #         d = dict_type()
    #         time += self.do_set_ones(d)
    #     time = time / operation_count
    #     self.time_set.append(time)
    #
    # def do_set_ones(self, d):
    #     start = timeit.default_timer()
    #     for i in self.data:
    #         d[i] = i
    #     end = timeit.default_timer()
    #     return (end - start)/len(self.data)

    def make_time_get(self, dict_type):
        time = 0
        for ones in range(operation_count):
            d = dict_type()
            self.full_dict(d)
            time += self.do_get_ones(d)
        time = time / operation_count
        self.time_get.append(time)

    def do_get_ones(self, d):
        temp = 0
        start = timeit.default_timer()
        for i in self.data:
            temp = d[i]
        end = timeit.default_timer()
        return (end - start) / len(self.data)

    def full_dict(self, d):
        for i in self.data:
            d[i] = i

    # def make_time_del(self, dict_type):
    #     time = 0
    #     for ones in range(operation_count):
    #         d = dict_type()
    #         self.full_dict(d)
    #         time += self.do_del_ones(d)
    #     time = time / operation_count
    #     self.time_del.append(time)
    #
    # def do_del_ones(self, d):
    #     start = timeit.default_timer()
    #     for i in self.data:
    #         del d[i]
    #     end = timeit.default_timer()
    #     return (end - start) / len(self.data)
    #
    # def make_time_items(self, dict_type):
    #     time = 0
    #     for ones in range(operation_count):
    #         d = dict_type()
    #         self.full_dict(d)
    #         time += self.do_items_ones(d)
    #     time = time / operation_count
    #     self.time_items.append(time)
    #
    # @staticmethod
    # def do_items_ones(d):
    #     start = timeit.default_timer()
    #     d.items()
    #     end = timeit.default_timer()
    #     return end - start
    #
    # def make_time_keys(self, dict_type):
    #     time = 0
    #     for ones in range(operation_count):
    #         d = dict_type()
    #         self.full_dict(d)
    #         time += self.do_keys_ones(d)
    #     time = time / operation_count
    #     self.time_keys.append(time)
    #
    # @staticmethod
    # def do_keys_ones(d):
    #     start = timeit.default_timer()
    #     d.keys()
    #     end = timeit.default_timer()
    #     return end - start
    #
    # def make_time_values(self, dict_type):
    #     time = 0
    #     for ones in range(operation_count):
    #         d = dict_type()
    #         self.full_dict(d)
    #         time += self.do_values_ones(d)
    #     time = time / operation_count
    #     self.time_values.append(time)
    #
    # @staticmethod
    # def do_values_ones(d):
    #     start = timeit.default_timer()
    #     d.values()
    #     end = timeit.default_timer()
    #     return end - start
