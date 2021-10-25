""" Custom list with special properties """


class CustomList(list):
    """ Class of custom list """
    def __add__(self, item):
        """ Refactor method __add__ """
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
        """ Refactor method __radd__ """
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
        """ Refactor method __sub__ """
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
        """ Refactor method __rsub__ """
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
        """ Refactor method __lt__ """
        return sum(self) < sum(other)

    def __le__(self, other):
        """ Refactor method __le__ """
        return sum(self) <= sum(other)

    def __eq__(self, other):
        """ Refactor method __eq__ """
        return sum(self) == sum(other)

    def __ne__(self, other):
        """ Refactor method __ne__ """
        return sum(self) != sum(other)

    def __gt__(self, other):
        """ Refactor method __gt__ """
        return sum(self) >= sum(other)

    def __ge__(self, other):
        """ Refactor method __ge__ """
        return sum(self) > sum(other)
