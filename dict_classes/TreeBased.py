from dict_classes.subClasses import DictItem, BalancedTree
from collections.abc import MutableMapping
from dict_classes.ParentDictClass import ParentDict


class BinaryTreeDictionary(ParentDict, MutableMapping):
    def __init__(self):
        super().__init__()
        self.peek = None
        self.popped = None

    def __setitem__(self, key, value):
        if self.peek is None:
            self.peek = DictItem(key, value)
            self.elements.append(DictItem(key, value))
            self.k_list.append(key)
            self.v_list.append(value)
            return
        curr_leaf = self.peek
        while True:
            if key < curr_leaf.key:
                if curr_leaf.left is None:
                    curr_leaf.left = DictItem(key, value)
                    break
                curr_leaf = curr_leaf.left
            else:
                if curr_leaf.right is None:
                    curr_leaf.right = DictItem(key, value)
                    break
                curr_leaf = curr_leaf.right
        self.elements.append(DictItem(key, value))
        self.k_list.append(key)
        self.v_list.append(value)

    def __getitem__(self, key):
        if self.peek is None:
            raise KeyError(key)
        curr_leaf = self.peek
        while True:
            if key == curr_leaf.key:
                return curr_leaf.value
            elif key > curr_leaf.key:
                if curr_leaf.right is None:
                    raise KeyError(key)
                curr_leaf = curr_leaf.right
            else:
                if curr_leaf.left is None:
                    raise KeyError(key)
                curr_leaf = curr_leaf.left

    def __delitem__(self, key):
        self.build_tree_without_leaf(self.peek, key)
        if self.popped is None:
            raise KeyError(key)
        self.elements.remove(DictItem(key, self.popped))
        self.k_list.remove(key)
        self.v_list.remove(self.popped)
        self.popped = None

    def build_tree_without_leaf(self, curr_leaf, key):
        """ recirsively looks for item and rewrites links to him """
        if curr_leaf is None:
            return
        if key < curr_leaf.key:
            curr_leaf.left = \
                self.build_tree_without_leaf(curr_leaf.left, key)
        elif key > curr_leaf.key:
            curr_leaf.right = \
                self.build_tree_without_leaf(curr_leaf.right, key)
        else:
            is_peek = None
            if self.peek == curr_leaf:
                is_peek = True
            self.popped = curr_leaf.value
            left_tree = curr_leaf.left
            right_tree = curr_leaf.right
            if right_tree is None:
                return left_tree
            if left_tree is None:
                return right_tree
            new_leaf = self.find_the_most_left(right_tree)
            new_leaf.right = self.build_new_right_tree(right_tree)
            new_leaf.left = left_tree
            if is_peek:
                self.peek = new_leaf
            return new_leaf
        return curr_leaf

    def find_the_most_left(self, curr_leaf):
        """Finds the most left tree(which has no left child) and returns it"""
        if curr_leaf.left is None:
            return curr_leaf
        return self.find_the_most_left(curr_leaf.left)

    def build_new_right_tree(self, curr_leaf):
        """Finds the most left tree(which has no left child)
         and puts link on his right child instead of him"""
        if curr_leaf.left is None:
            return curr_leaf.right
        curr_leaf.left = self.build_new_right_tree(curr_leaf.left)
        return curr_leaf


class BalancedTreeDictionary(ParentDict, MutableMapping):
    def __init__(self):
        super().__init__()
        self.tree = BalancedTree()

    def __setitem__(self, key, value):
        self.tree.add(key, value)
        self.elements.append(DictItem(key, value))
        self.k_list.append(key)
        self.v_list.append(value)

    def __getitem__(self, key):
        node = self.tree.node
        while node is not None:
            if key == node.key:
                return node.value
            elif key > node.key:
                node = node.right.node
            else:
                node = node.left.node
        raise KeyError(key)

    def __delitem__(self, key):
        deleted = self.tree.delete(key)
        if deleted is None:
            raise KeyError(key)
        self.k_list.remove(key)
        self.v_list.remove(deleted)
        self.elements.remove(DictItem(key, deleted))
