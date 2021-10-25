""" Custom metaclass for refactoring names with prefixes """


class CustomMeta(type):
    """ custom metaclass which adding prefix "custom_" """
    def __call__(cls, *args, **kwargs):
        """ refactor call method with class type call method call """
        obj = type.__call__(cls, *args, **kwargs)
        obj.__dict__ = cls.add_my_prefix(obj.__dict__)
        return obj

    def __new__(cls, name, bases, dct):
        """ refactor new method """
        dct_remake = cls.add_my_prefix(dct)
        return type.__new__(cls, name, bases, dct_remake)

    @staticmethod
    def add_my_prefix(prev_dict):
        """ function which adding prefix "custom_" """
        dict_remake = {}
        for key, value in prev_dict.items():
            if key.startswith('__') and key.endswith('__'):
                dict_remake[key] = value
            else:
                dict_remake[f'custom_{key}'] = value
        return dict_remake


class CustomClass(metaclass=CustomMeta):
    """ example of using this metaclass """
    x = 50

    def __init__(self, val=99):
        """ initialization """
        self.val = val

    def line(self):
        """ return 100 """
        return 100


if __name__ == '__main__':
    inst = CustomClass()
    # inst.x  # ошибка
    # inst.val  # ошибка
    # inst.line()  # ошибка
    print('custom_x', inst.custom_x)    # 50
    print('custom_line()', inst.custom_line())  # 100
    print('custom_val', inst.custom_val)
