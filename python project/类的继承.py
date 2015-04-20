__author__ = '绍文'


class Parent:

    def __init__(self):
        print("调用了父类的构造函数")

    def setattr(self, attr):
        Parent.attr = attr

    def getattr(self):
        print("调用了父类的方法",  Parent.attr)


class Child(Parent):

    def __init__(self):
        print("调用了子类的构造函数")

child = Child()
child.setattr(15)
child.getattr()