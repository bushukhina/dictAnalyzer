class ParentDict:
    def __init__(self):
        self.elements = []
        self.k_list = []
        self.v_list = []

    def items(self):
        return self.elements

    def keys(self):
        return self.k_list

    def values(self):
        return self.v_list

    def __contains__(self, item):
        try:
            self[item]
        except KeyError:
            return False
        return True

    def __eq__(self, other):
        return {item.key: item.value for item in self.elements} == other

    def __iter__(self):
        return

    def __len__(self):
        return
