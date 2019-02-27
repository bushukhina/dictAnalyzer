from collections.abc import MutableMapping
from dict_classes.ParentDictClass import ParentDict
from dict_classes.subClasses import DictItem


class LinearSearchDictionary(ParentDict, MutableMapping):
    def __init__(self):
        super().__init__()

    def __setitem__(self, key, value):
        self.elements.append(DictItem(key, value))
        self.k_list.append(key)
        self.v_list.append(value)

    def __getitem__(self, key):
        for item in self.elements:
            if item.key == key:
                return item.value
        raise KeyError(key)

    def __delitem__(self, key):
        val = None
        for i in range(len(self.elements)):
            if self.elements[i].key == key:
                val = self.elements.pop(i).value
                self.k_list.pop(i)
                self.v_list.pop(i)
                break
        if val is None:
            raise KeyError(key)


class BinarySearchDictionary(ParentDict, MutableMapping):
    def __init__(self):
        super().__init__()

    def __setitem__(self, key, value):
        self.elements.append(DictItem(key, value))
        self.elements.sort(key=BinarySearchDictionary.sort_by_key)
        self.k_list.append(key)
        self.v_list.append(value)

    def __getitem__(self, key):
        index = self.binary_search(key)
        if index is not None:
            return self.elements[index].value
        raise KeyError(key)

    def __delitem__(self, key):
        val = None
        index = self.binary_search(key)
        if index is not None:
            val = self.elements.pop(index).value
            self.k_list.remove(key)
            self.v_list.remove(val)
        if val is None:
            raise KeyError(key)

    def binary_search(self, key):
        """ finds index of element with key in list of elements """
        first = 0
        last = len(self.elements) - 1
        while first <= last:
            midpoint = (first + last) // 2
            if self.elements[midpoint].key == key:
                return midpoint
            else:
                if key < self.elements[midpoint].key:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        return None

    @staticmethod
    def sort_by_key(item):
        return item.key
