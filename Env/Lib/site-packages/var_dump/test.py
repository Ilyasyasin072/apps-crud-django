__author__ = 'sha256'

from var_dump import var_dump
from datetime import datetime
from decimal import Decimal

try:
    from enum import Enum
except ImportError:
    Enum = type(str)


class Base(object):

    def __init__(self):
        self.baseProp = (33, 44)
        self.fl = 44.33


class Bar(object):

    def __init__(self):
        self.barProp = "I'm from Bar class"
        self.boo = True


class Foo(Base):

    def __init__(self):
        super(Foo, self).__init__()
        self.someList = ['foo', 'goo']
        self.someTuple = (33, (23, 44), 55)
        self.anOb = Bar()
        self.no = None
        self.color = Color.RED


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


if __name__ == '__main__':
    foo = Foo()
    var_dump(datetime(2017, 9, 9).date())
