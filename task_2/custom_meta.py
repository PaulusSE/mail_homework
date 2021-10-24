class CustomMeta(type):
    def __call__(cls, *args, **kwargs):
        obj = type.__call__(cls, *args, **kwargs)
        obj.__dict__ = cls.add_my_prefix(obj.__dict__)
        return obj

    def __new__(cls, name, bases, dct):
        dct_remake = cls.add_my_prefix(dct)
        return type.__new__(cls, name, bases, dct_remake)

    # def __new__(cls, *args, **kwargs):
    #     obj = cls.__call__(cls, *args, **kwargs)
    #     dict_remake = cls.add_my_prefix()

    @staticmethod
    def add_my_prefix(prev_dict):
        dict_remake = {}
        for key, value in prev_dict.items():
            if key.startswith('__') and key.endswith('__'):
                dict_remake[key] = value
            else:
                dict_remake[f'custom_{key}'] = value
        return dict_remake


# class CustomClass(metaclass=CustomMeta):
#     x = 50
#
#     def __init__(self, val=99):
#         self.val = val
#
#     def line(self):
#         return 100
#
#
# inst = CustomClass()
# inst.custom_x
# inst.custom_val
# inst.custom_line()
#
# inst.x  # ошибка
# inst.val  # ошибка
# inst.line()  # ошибка


class CustomClass(metaclass=CustomMeta):
    """Пробный класс"""
    x = 50

    def __init__(self, val=99):
        # print('CLASS INIT')
        self.val = val

    def line(self):
        """Test func line"""
        return 100

    def new_line(self):
        """Test func new line"""
        return self.custom_val + 100


if __name__ == '__main__':
    inst = CustomClass()
    # print(dir(inst))
    print('END --- ', [i for i in dir(inst) if not i.startswith('__')])
    print('custom_x', inst.custom_x)    # 50
    print('custom_line()', inst.custom_line())  # 100
    print('custom_val', inst.custom_val)    # 99
    print('custom_new_line', inst.custom_new_line()) # 199
    try:
        print(inst.val)
    except AttributeError:
        print('\nAttributeError: нет inst.val')
