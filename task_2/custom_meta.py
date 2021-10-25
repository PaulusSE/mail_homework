class CustomMeta(type):
    def __call__(cls, *args, **kwargs):
        obj = type.__call__(cls, *args, **kwargs)
        obj.__dict__ = cls.add_my_prefix(obj.__dict__)
        return obj

    def __new__(cls, name, bases, dct):
        dct_remake = cls.add_my_prefix(dct)
        return type.__new__(cls, name, bases, dct_remake)

    @staticmethod
    def add_my_prefix(prev_dict):
        dict_remake = {}
        for key, value in prev_dict.items():
            if key.startswith('__') and key.endswith('__'):
                dict_remake[key] = value
            else:
                dict_remake[f'custom_{key}'] = value
        return dict_remake


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100


if __name__ == '__main__':
    inst = CustomClass()
    # inst.x  # ошибка
    # inst.val  # ошибка
    # inst.line()  # ошибка
    print('custom_x', inst.custom_x)    # 50
    print('custom_line()', inst.custom_line())  # 100
