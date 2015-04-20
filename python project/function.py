__author__ = '绍文'


def my_new_function(parameter):
    """my new function"""
    print(parameter)
    return


def my_new_function2(*parameterlist):
    """可变参数"""
    for value in parameterlist:
        print(value)
    return

my_new_function2("hello", "bye", "hello again")


#匿名函数

sus = lambda operation1, operartion2: operation1+operartion2

print(sus(15, 20))