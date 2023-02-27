# coding:utf-8
'''来自http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example'''

class MetaClass(type):

    def __new__(meta, name, bases, dct):
        print("-----------------------------------")
        print("Allocating memory for class", name)
        print(meta)
        print(bases)
        print(dct)
        return super(MetaClass, meta).__new__(meta, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print('-----------------------------------')
        print("Initializing class", name)
        print(cls)
        print(bases)
        print(dct)
        super(MetaClass, cls).__init__(name, bases, dct)


class Myclass(object):
    __metaclass__ = MetaClass

    def foo(self, param):
        print(param)


p = Myclass()
p.foo("hello")



# 注意：此例子只能在python2下执行