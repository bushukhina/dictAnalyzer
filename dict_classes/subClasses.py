class DictItem:
    def __init__(self, key, value):
        self._key = key
        self.value = value
        self.right = None
        self.left = None

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        if self._key is not None:
            raise KeyError
        self._key = key

    def __eq__(self, other):
        return (self.key, self.value) == (other.key, other.value)


class BalancedTree:
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0
        self.popped = None

    def add(self, key, value):
        if self.node is None:
            self.node = DictItem(key, value)
            self.node.left = BalancedTree()
            self.node.right = BalancedTree()
        elif key < self.node.key:
            self.node.left.add(key, value)
        elif key > self.node.key:
            self.node.right.add(key, value)
        self.rebalance()

    def rebalance(self):
        self.update_heights(recursive=False)
        self.update_balances(recursive=False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.rotate_left()
                    self.update_heights()
                    self.update_balances()
                self.rotate_right()
                self.update_heights()
                self.update_balances()
            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rotate_right()
                    self.update_heights()
                    self.update_balances()
                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def update_heights(self, recursive=True):
        if self.node is not None:
            if recursive:
                if self.node.left is not None:
                    self.node.left.update_heights()
                if self.node.right is not None:
                    self.node.right.update_heights()
            self.height = \
                1 + max(self.node.left.height, self.node.right.height)
        else:
            self.height = -1

    def update_balances(self, recursive=True):
        if self.node is not None:
            if recursive:
                if self.node.left is not None:
                    self.node.left.update_balances()
                if self.node.right is not None:
                    self.node.right.update_balances()
            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def rotate_right(self):
        new_root = self.node.left.node
        new_left_sub = new_root.right.node
        old_root = self.node

        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root

    def rotate_left(self):
        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node

        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root

    def delete(self, key, write_deleted=True):
        deleted = None
        if self.node is None:
            return None

        if self.node.key == key:
            if write_deleted:
                deleted = self.node.value
            if self.node.left.node is None and self.node.right.node is None:
                self.node = None
            elif self.node.left.node is None:
                self.node = self.node.right.node
            elif self.node.right.node is None:
                self.node = self.node.left.node
            else:
                successor = self.node.right.node
                while successor.left.node is not None:
                    successor = successor.left.node

                # key is not possible to change, make new node
                right = self.node.right
                left = self.node.left
                self.node = DictItem(successor.key, successor.value)
                self.node.right = right
                self.node.left = left

                # del successor from it's original position
                self.node.right.delete(successor.key, write_deleted=False)
        elif key < self.node.key:
            deleted = self.node.left.delete(key)
        elif key > self.node.key:
            deleted = self.node.right.delete(key)

        self.rebalance()
        return deleted
