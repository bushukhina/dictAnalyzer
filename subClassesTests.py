from dict_classes.subClasses import DictItem, BalancedTree
import unittest


class TestItems(unittest.TestCase):
    def test_item_creation(self):
        item = DictItem('anna', [1, 2, 3])
        self.assertEqual(item.key, 'anna')
        self.assertEqual(item.value, [1, 2, 3])

    def test_eq(self):
        item1 = DictItem('anna', 'danil')
        self.assertEqual(item1, item1)
        item2 = DictItem('anna', 'sara')
        self.assertNotEqual(item1, item2)
        item3 = DictItem('lora', 'danil')
        self.assertNotEqual(item1, item3)


class TestBalancedTree(unittest.TestCase):
    def test_init(self):
        tree = BalancedTree()
        self.assertIs(tree.node, None)
        self.assertIs(tree.popped, None)
        self.assertEqual(tree.balance, 0)
        self.assertEqual(tree.height, -1)

    def test_update_heights(self):
        tree = BalancedTree()
        tree.node = DictItem(20, 5)
        tree.node.right = BalancedTree()
        tree.node.left = BalancedTree()
        self.assertEqual(tree.height, -1)
        tree.update_heights(recursive=False)
        self.assertEqual(tree.height, 0)
        tree.node.right.node = DictItem(25, 5)
        tree.node.right.node.left = BalancedTree()
        tree.node.right.node.right = BalancedTree()
        tree.update_heights()
        self.assertEqual(tree.height, 1)
        tree.node.right.node.right.node = DictItem(35, 5)
        tree.node.right.node.right.node.left = BalancedTree()
        tree.node.right.node.right.node.right = BalancedTree()
        tree.update_heights()
        self.assertEqual(tree.height, 2)

    def test_update_balances(self):
        tree = BalancedTree()
        tree.node = DictItem(20, 5)
        tree.node.right = BalancedTree()
        tree.node.left = BalancedTree()

        self.assertEqual(tree.balance, 0)
        tree.update_heights(recursive=False)
        tree.update_balances(recursive=False)
        self.assertEqual(tree.balance, 0)

        tree.node.right.node = DictItem(25, 5)
        tree.node.right.node.left = BalancedTree()
        tree.node.right.node.right = BalancedTree()
        tree.update_heights()
        tree.update_balances()
        self.assertEqual(tree.balance, -1)

        tree.node.right.node.right.node = DictItem(35, 5)
        tree.node.right.node.right.node.left = BalancedTree()
        tree.node.right.node.right.node.right = BalancedTree()
        tree.update_heights()
        tree.update_balances()
        self.assertEqual(tree.balance, -2)

    def test_rotate_right(self):
        tree = BalancedTree()

        tree.node = DictItem('s', 5)
        tree.node.right = BalancedTree()
        tree.node.left = BalancedTree()

        tree.node.right.node = DictItem('z', 5)
        tree.node.right.node.left = BalancedTree()
        tree.node.right.node.right = BalancedTree()

        tree.node.left.node = DictItem('k', 5)
        tree.node.left.node.left = BalancedTree()
        tree.node.left.node.right = BalancedTree()

        tree.node.left.node.right.node = DictItem('m', 5)
        tree.node.left.node.right.node.left = BalancedTree()
        tree.node.left.node.right.node.right = BalancedTree()

        tree.node.left.node.left.node = DictItem('d', 5)
        tree.node.left.node.left.node.left = BalancedTree()
        tree.node.left.node.left.node.right = BalancedTree()

        self.assertIs(tree.node.key, 's')
        self.assertIs(tree.node.right.node.key, 'z')
        self.assertIs(tree.node.left.node.key, 'k')
        self.assertIs(tree.node.left.node.right.node.key, 'm')
        self.assertIs(tree.node.left.node.left.node.key, 'd')

        tree.rotate_right()

        self.assertIs(tree.node.key, 'k')
        self.assertIs(tree.node.right.node.key, 's')
        self.assertIs(tree.node.left.node.key, 'd')
        self.assertIs(tree.node.right.node.right.node.key, 'z')
        self.assertIs(tree.node.right.node.left.node.key, 'm')

    def test_rotate_left(self):
        tree = BalancedTree()

        tree.node = DictItem('s', 5)
        tree.node.right = BalancedTree()
        tree.node.left = BalancedTree()

        tree.node.right.node = DictItem('y', 5)
        tree.node.right.node.left = BalancedTree()
        tree.node.right.node.right = BalancedTree()

        tree.node.left.node = DictItem('k', 5)
        tree.node.left.node.left = BalancedTree()
        tree.node.left.node.right = BalancedTree()

        tree.node.right.node.right.node = DictItem('z', 5)
        tree.node.right.node.right.node.left = BalancedTree()
        tree.node.right.node.right.node.right = BalancedTree()

        tree.node.right.node.left.node = DictItem('q', 5)
        tree.node.right.node.left.node.left = BalancedTree()
        tree.node.right.node.left.node.right = BalancedTree()

        self.assertIs(tree.node.key, 's')
        self.assertIs(tree.node.right.node.key, 'y')
        self.assertIs(tree.node.left.node.key, 'k')
        self.assertIs(tree.node.right.node.right.node.key, 'z')
        self.assertIs(tree.node.right.node.left.node.key, 'q')

        tree.rotate_left()

        self.assertIs(tree.node.key, 'y')
        self.assertIs(tree.node.right.node.key, 'z')
        self.assertIs(tree.node.left.node.key, 's')
        self.assertIs(tree.node.left.node.right.node.key, 'q')
        self.assertIs(tree.node.left.node.left.node.key, 'k')

    def test_delete(self):
        tree = BalancedTree()

        tree.add('d', 5)
        tree.add('a', 5)
        tree.add('s', 5)
        tree.add('y', 5)
        tree.add('x', 5)
        tree.add('z', 5)
        tree.delete('x')
        self.assertEqual(tree.node.key, 'y')
        self.assertEqual(tree.node.right.node.key, 'z')
        self.assertEqual(tree.node.left.node.key, 'd')

    def test_add(self):
        tree = BalancedTree()

        tree.add('d', 5)
        self.assertEqual(tree.node, DictItem('d', 5))

        tree.add('a', 5)
        self.assertEqual(tree.node.left.node, DictItem('a', 5))

        tree.add('s', 5)
        self.assertEqual(tree.node.right.node, DictItem('s', 5))

        tree.add('k', 5)
        self.assertEqual(tree.node.right.node.left.node, DictItem('k', 5))

        tree.add('y', 5)
        self.assertEqual(tree.node.right.node.right.node, DictItem('y', 5))

        tree.add('z', 5)
        self.assertEqual(tree.node.right.node.right.node, DictItem('z', 5))
