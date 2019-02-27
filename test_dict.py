from TestDictParentClass import DictParentTest
from dict_classes.subClasses import DictItem
from dict_classes.ListBased import LinearSearchDictionary, \
    BinarySearchDictionary
from dict_classes.HashTableBased import HashTableDictionary
from dict_classes.TreeBased import BalancedTreeDictionary, BinaryTreeDictionary
from subClassesTests import TestItems, TestBalancedTree
import unittest


class TestLinearSD(DictParentTest, unittest.TestCase):
    dict_type = LinearSearchDictionary


class TestBinarySD(DictParentTest, unittest.TestCase):
    dict_type = BinarySearchDictionary


class TestHashTD(DictParentTest, unittest.TestCase):
    dict_type = HashTableDictionary


class TestBinaryTD(DictParentTest, unittest.TestCase):
    dict_type = BinaryTreeDictionary


class TestBalTD(DictParentTest, unittest.TestCase):
    dict_type = BalancedTreeDictionary


class TestSpecialOperations(unittest.TestCase):
    def test_binary_search(self):
        d = BinarySearchDictionary()
        d[1] = 'a'
        d[2] = 'b'
        d[3] = 'c'
        self.assertEqual(d.binary_search(3), 2)

    def test_get_key(self):
        item = DictItem('a', 'b')
        self.assertEqual(BinarySearchDictionary.sort_by_key(item), 'a')

    def test_resize(self):
        d = HashTableDictionary()
        for i in range(1, 6):
            d[i] = i + 1
        self.assertEqual(len(d.buckets), 8)
        d[9] = 10
        self.assertEqual(len(d.buckets), 32)


class TestBinaryTDSpecials(unittest.TestCase):
    def test_init(self):
        d = BinaryTreeDictionary()
        self.assertIs(d.peek, None)
        self.assertIs(d.popped, None)

    def test_add(self):
        d = BinaryTreeDictionary()
        d[10] = 'a'
        self.assertEqual(d.peek, DictItem(10, 'a'))
        d[5] = 'b'
        d[15] = 'c'
        self.assertEqual(d.peek.left, DictItem(5, 'b'))
        self.assertEqual(d.peek.right, DictItem(15, 'c'))
        d[18] = 'd'
        d[16] = 'e'
        d[19] = 'f'
        d[17] = 'g'
        self.assertEqual(d.peek.right.right, DictItem(18, 'd'))
        self.assertEqual(d.peek.right.right.left, DictItem(16, 'e'))
        self.assertEqual(d.peek.right.right.right, DictItem(19, 'f'))
        self.assertEqual(d.peek.right.right.left.right, DictItem(17, 'g'))

    def test_delete(self):
        d = BinaryTreeDictionary()
        d[10] = 'a'
        d[5] = 'b'
        d[15] = 'c'
        d[18] = 'd'
        d[16] = 'e'
        d[19] = 'f'
        d[17] = 'g'
        del d[10]
        self.assertSetEqual(set(d.values()),
                            {'b', 'c', 'd', 'e', 'f', 'g'})
        del d[18]
        self.assertSetEqual(set(d.values()), {'b', 'c', 'e', 'f', 'g'})
        del d[15]
        self.assertSetEqual(set(d.values()), {'b', 'e', 'f', 'g'})
        del d[19]
        self.assertSetEqual(set(d.values()), {'b', 'e', 'g'})
        del d[17]
        self.assertSetEqual(set(d.values()), {'b', 'e'})
        self.assertRaises(KeyError, d.__delitem__, 10)

    def test_most_left(self):
        d = BinaryTreeDictionary()
        d[10] = 'a'
        d[5] = 'b'
        d[3] = 'c'
        d[4] = 'd'
        d[1] = 'e'
        d[2] = 'f'
        leaf = d.find_the_most_left(d.peek)
        self.assertEqual(leaf, DictItem(1, 'e'))
        self.assertEqual(leaf.right, DictItem(2, 'f'))
        self.assertIs(leaf.left, None)

    def test_build_right_tree(self):
        d = BinaryTreeDictionary()
        d[18] = 'd'
        d[16] = 'e'
        d[19] = 'f'
        d[17] = 'g'
        tree = d.build_new_right_tree(d.peek)
        self.assertEqual(tree, DictItem(18, 'd'))
        self.assertEqual(tree.left, DictItem(17, 'g'))
        self.assertEqual(tree.right, DictItem(19, 'f'))

    def test_build_new_tree(self):
        self._test_no_left()
        self._test_no_right()
        self._test_no_such_key()
        self._test_both()

    def _test_no_left(self):
        d = BinaryTreeDictionary()
        d[10] = 'a'
        d[15] = 'c'
        d[18] = 'd'
        d[16] = 'e'
        d[19] = 'f'
        d.build_tree_without_leaf(d.peek, 15)
        self.assertEqual(d.peek, DictItem(10, 'a'))
        self.assertEqual(d.peek.right, DictItem(18, 'd'))
        self.assertEqual(d.peek.right.left, DictItem(16, 'e'))
        self.assertEqual(d.peek.right.right, DictItem(19, 'f'))

    def _test_no_right(self):
        d = BinaryTreeDictionary()
        d[10] = 'a'
        d[15] = 'c'
        d[18] = 'd'
        d[16] = 'e'
        d[17] = 'g'
        d.build_tree_without_leaf(d.peek, 18)
        self.assertEqual(d.peek, DictItem(10, 'a'))
        self.assertEqual(d.peek.right, DictItem(15, 'c'))
        self.assertEqual(d.peek.right.right, DictItem(16, 'e'))
        self.assertEqual(d.peek.right.right.right, DictItem(17, 'g'))

    def _test_no_such_key(self):
        d = BinaryTreeDictionary()
        d[10] = 'a'
        d[5] = 'b'
        d[15] = 'c'
        d[18] = 'd'
        d[16] = 'e'
        d[19] = 'f'
        d[17] = 'g'
        d.build_tree_without_leaf(d.peek, 1001)
        self.assertEqual(d.peek, DictItem(10, 'a'))
        self.assertEqual(d.peek.left, DictItem(5, 'b'))
        self.assertEqual(d.peek.right, DictItem(15, 'c'))
        self.assertEqual(d.peek.right.right, DictItem(18, 'd'))
        self.assertEqual(d.peek.right.right.left, DictItem(16, 'e'))
        self.assertEqual(d.peek.right.right.right, DictItem(19, 'f'))
        self.assertEqual(d.peek.right.right.left.right, DictItem(17, 'g'))

    def _test_both(self):
        d = BinaryTreeDictionary()
        d[10] = 'a'
        d[15] = 'c'
        d[13] = 'z'
        d[18] = 'd'
        d[16] = 'e'
        d[19] = 'f'
        d[17] = 'g'
        d.build_tree_without_leaf(d.peek, 15)
        self.assertEqual(d.peek, DictItem(10, 'a'))
        self.assertEqual(d.peek.right, DictItem(16, 'e'))
        self.assertEqual(d.peek.right.left, DictItem(13, 'z'))
        self.assertEqual(d.peek.right.right, DictItem(18, 'd'))
        self.assertEqual(d.peek.right.right.right, DictItem(19, 'f'))
        self.assertEqual(d.peek.right.right.left, DictItem(17, 'g'))


def make_suite():
    suite = unittest.TestSuite()
    for test in (TestItems, TestSpecialOperations, TestBinaryTD,
                 TestBalTD, TestHashTD, TestLinearSD,
                 TestBinarySD, TestBinaryTDSpecials, TestBalancedTree):
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test))
    return suite


if __name__ == '__main__':
    unittest.main()
