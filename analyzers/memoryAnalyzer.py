from queue import Queue
from sys import getsizeof
from dict_classes.ListBased import LinearSearchDictionary, \
    BinarySearchDictionary
from dict_classes.HashTableBased import HashTableDictionary
from dict_classes.TreeBased import BalancedTreeDictionary, BinaryTreeDictionary

dict_types = [LinearSearchDictionary,
              BinarySearchDictionary,
              HashTableDictionary,
              BinaryTreeDictionary,
              BalancedTreeDictionary]


class MemoryAnalyzer:
    def __init__(self, data):
        self.data = data
        self.result = []

    def full_dict(self, d):
        for i in self.data:
            d[i] = i

    def run_for_all(self):
        for dict_type in dict_types:
            d = dict_type()
            self.full_dict(d)
            size = getsizeof(d)
            size += self.count_array_size(d.elements)
            size += self.count_array_size(d.k_list)
            size += self.count_array_size(d.v_list)
            if isinstance(d, BinaryTreeDictionary):
                size += self.count_bin_tree_size(d)
            elif isinstance(d, BalancedTreeDictionary):
                size += self.count_bal_tree_size(d)
            elif isinstance(d, HashTableDictionary):
                size += self.count_hash_table_size(d)
            self.result.append(size)
        self.count_size_built_in_dict()

    def count_size_built_in_dict(self):
        d = dict()
        self.full_dict(d)
        size = getsizeof(d)
        for key in d.keys():
            size += getsizeof(d[key])
        self.result.append(size)

    @staticmethod
    def count_array_size(array):
        size = getsizeof(array)
        for i in range(len(array)):
            size += getsizeof(array[i])
        return size

    @staticmethod
    def count_bin_tree_size(btd):
        size = getsizeof(btd.popped)
        queue = Queue()
        queue.put(btd.peek)
        while not queue.empty():
            leaf = queue.get()
            size += getsizeof(leaf)
            if leaf.right is not None:
                queue.put(leaf.right)
            if leaf.left is not None:
                queue.put(leaf.left)
        return size

    @staticmethod
    def count_bal_tree_size(btd):
        size = 0
        queue = Queue()
        queue.put(btd.tree)
        while not queue.empty():
            tree = queue.get()
            size += getsizeof(tree.node)
            size += getsizeof(tree.balance)
            size += getsizeof(tree.popped)
            size += getsizeof(tree.height)
            if tree.node is None:
                continue
            if tree.node.right is not None:
                queue.put(tree.node.right)
            if tree.node.left is not None:
                queue.put(tree.node.left)

        return size

    def count_hash_table_size(self, htd):
        size = htd.size
        size += htd.count
        size += self.count_array_size(htd.buckets)
        for bucket in htd.buckets:
            size += self.count_array_size(bucket)
        return size
