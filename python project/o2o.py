__author__ = '绍文'


class Employee:
    """my first class!"""
    # 类变量
    en_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.en_count += 1

    def display_count(self):
        print(self.en_count)

    def display_emplyee(self):
        print("name ", self.name, "salary ", self.salary)

    def __del__(self):
        class_name = self.name
        print(class_name)

emp1 = Employee("bob", 8000)
emp2 = Employee("han", 9500)

emp1.display_count()
emp2.display_emplyee()
print(Employee.en_count)

emp1.age = 24
print(emp1.age)

print("Employee __doc__ is ", Employee.__doc__)
print("Employee __dict__ is ", Employee.__dict__)
print("Employee __module__ is ", Employee.__module__)
print("Employee __base__ is ", Employee.__base__)

emp1.__del__()
del emp2