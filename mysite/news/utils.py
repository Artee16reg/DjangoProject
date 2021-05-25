# Модуль для примесей

class MyMixin(object):
    """
    Простой миксин для преобразования строки в верхний регистр :)
    """
    mixin_prop = ''

    def get_prop(self):
        return self.mixin_prop.upper()

    def get_upper(self, s):
        return s.upper()
