class CustomList(list):
    def __add__(self, item):
        result = []
        for i in range(max(len(item), len(self))):

            if i < min(len(item), len(self)):
                result.append(item[i] + self[i])
            if i >= min(len(item), len(self)) and len(item) > len(self):
                result.append(item[i] + 0)
            if i >= min(len(item), len(self)) and len(item) < len(self):
                result.append(self[i] + 0)

        return result

    def __radd__(self, item):
        result = []
        for i in range(max(len(item), len(self))):

            if i < min(len(item), len(self)):
                result.append(item[i] + self[i])
            if i >= min(len(item), len(self)) and len(item) > len(self):
                result.append(item[i] + 0)
            if i >= min(len(item), len(self)) and len(item) < len(self):
                result.append(self[i] + 0)

        return result

    def __sub__(self, other):
        result = []
        for i in range(max(len(other), len(self))):
            # print(i)
            # print(item[i], self[i])
            if i < min(len(other), len(self)):
                result.append(self[i] - other[i])
            if i >= min(len(other), len(self)) and len(other) >= len(self):
                result.append(0 - other[i])
            if i >= min(len(other), len(self)) and len(other) < len(self):
                result.append(self[i] - 0)

        return result

    def __rsub__(self, other):
        result = []
        for i in range(max(len(other), len(self))):
            # print(i)
            # print(item[i], self[i])
            if i < min(len(other), len(self)):
                result.append(self[i] - other[i])
            if i >= min(len(other), len(self)) and len(other) >= len(self):
                result.append(0 - other[i])
            if i >= min(len(other), len(self)) and len(other) < len(self):
                result.append(self[i] - 0)

        return result

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) >= sum(other)

    def __ge__(self, other):
        return sum(self) > sum(other)
