from collections.abc import MutableMapping
from dict_classes.ParentDictClass import ParentDict
from dict_classes.subClasses import DictItem


class HashTableDictionary(ParentDict, MutableMapping):
    def __init__(self):
        super().__init__()
        self.buckets = []
        self.count = 0
        self.size = 8
        for i in range(self.size):
            self.buckets.append([])

    def __setitem__(self, key, value):
        if self.count == 2 * self.size // 3:
            self.resize()
        bucket_index = self.get_bucket_index(key)
        self.buckets[bucket_index].append(DictItem(key, value))
        self.count += 1
        self.elements.append(DictItem(key, value))
        self.k_list.append(key)
        self.v_list.append(value)

    def __getitem__(self, key):
        bucket_index = self.get_bucket_index(key)
        for item in self.buckets[bucket_index]:
            if item.key == key:
                return item.value
        raise KeyError(key)

    def __delitem__(self, key):
        bucket_index = self.get_bucket_index(key)
        bucket = self.buckets[bucket_index]
        index_in_bucket = 0
        val = None
        for item in bucket:
            if item.key == key:
                bucket.pop(index_in_bucket)
                self.count -= 1
                val = item.value
                self.k_list.remove(key)
                self.v_list.remove(val)
                self.elements.remove(DictItem(key, val))
            index_in_bucket += 1
        if val is None:
            raise KeyError(key)

    def get_bucket_index(self, key):
        return (hash(key) & 0x7FFFFFFF) % self.size

    def resize(self):
        if self.size < 5000:
            self.size *= 4
        else:
            self.size *= 2
        new_buckets = []
        for i in range(self.size):
            new_buckets.append([])
        for bucket in self.buckets:
            for item in bucket:
                bucket_index = self.get_bucket_index(item.key)
                new_buckets[bucket_index]\
                    .append(DictItem(item.key, item.value))
        self.buckets = new_buckets
