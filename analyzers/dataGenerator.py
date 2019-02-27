import random


class DataGenerator:
    def __init__(self, size1, size2, size3, size4, size5):
        self.data_sets = []
        random.seed()

        random_data5 = [x for x in range(size5)]
        random.shuffle(random_data5)
        self.data_sets.append(random_data5)

        random_data4 = [x for x in range(size4)]
        random.shuffle(random_data4)
        self.data_sets.append(random_data4)

        random_data3 = [x for x in range(size3)]
        random.shuffle(random_data3)
        self.data_sets.append(random_data3)

        random_data2 = [x for x in range(size2)]
        random.shuffle(random_data2)
        self.data_sets.append(random_data2)

        random_data1 = [x for x in range(size1)]
        random.shuffle(random_data1)
        self.data_sets.append(random_data1)
