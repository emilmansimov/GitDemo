# from Inheritance import ParentClass
#
# x
# class ChildClass(ParentClass):
#     number1 = 100
#     number2 = 200
#     def summary_of_all_numbers(self):
#         return self.number1 + self.number2 + ParentClass.summary_of_two_numbers() + ParentClass.summary_of_three_numbers()
import numbers

from Inheritance import ParentClass


class ChildClass(ParentClass):
    number1 = 100
    number2 = 200 # 300
    def summary_of_all_numbers(self):
        return  self.number1 + self.number2 +\
                self.summary_of_two_numbers(100, 200) +\
                self.summary_of_three_numbers(50, 50, 40)


obj = ChildClass()
print(obj.summary_of_all_numbers())