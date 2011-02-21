import sys

from .base import Field


class Reserved(Field):
    def __init__(self, *args, **kwargs):
        super(Reserved, self).__init__(*args, **kwargs)

        # Hack to add the reserved field to the class without
        # having to explicitly give it a (likely useless) name
        frame = sys._getframe(2)
        locals = frame.f_locals
        locals[self.get_available_name(locals.keys())] = self

    def get_available_name(self, locals):
        i = 0
        while True:
            name = '_reserved_%s' % i
            if name not in locals:
                return name
            i += 1

    def set_name(self, name):
        if self.name:
            raise TypeError('Reserved fields must not be given an attribute name')
        super(Reserved, self).set_name(name)

    def encode(self, obj, value):
        return b'\x00' * self.size(obj)

    def decode(self, value):
        return None


