import io
import zlib

from .base import Field
from biwako import common


class Zlib(Field):
    def __init__(self, field, *args, **kwargs):
        super(Zlib, self).__init__(*args, **kwargs)
        self.field = field

    def decode(self, value):
        data = zlib.decompress(value)
        with common.AttributeInstance(self.instance):
            return self.field.decode(data)

    def encode(self, value):
        data = self.field.encode(value)
        return zlib.compress(data)

