# class ParentClass:
#
#     def summary_of_two_numbers(self, num1, num2,):
#         return num1 + num2  # sends the result back to summary_of_numbers. Return returns driver objects of elements
#     def summary_of_three_numbers(self, num3, num4, num5):
#         return num3 + num4 + num5
#
# obj = ParentClass()
#
# print(obj.summary_of_two_numbers(30, 55))
# print(obj.summary_of_three_numbers(39, 39, 39))

class ParentClass:
    Emil_number = 400
    Emil_number2 =500

    def summary_of_two_numbers(self, num1, num2):
        return num1 + num2

    def summary_of_three_numbers(self, num3, num4, num5):
        return num3 + num4 + num5


obj = ParentClass()
print(obj.summary_of_two_numbers(15, 45))
print(obj.summary_of_three_numbers(20, 40, 60))
