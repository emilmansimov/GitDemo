# class Constructor:
#     brand = "Ferrari"
#     # this is a class constructor. Whatever you create inside your constructor is an instance variable
#
#     def __init__(self, model, year):   # self is the obj/object that you're creating
#         self.model = model
#         self.year = year
#         print(model, year)
#
#
# obj = Constructor("f8", 2022)
# print(obj.brand)
# object2 = Constructor("f8", 2022)
# object1 = Constructor("599", 2021)
# print(object1.brand)
# #  Class variables aren't callable (can't change the value of a variable), unlike instance variables

class Const:
    make = "Lamborghini"

    num = 100
    def __init__(self, model, year):

        self.model = model
        self.year = year
        print(model, year)


        

obj = Const("Aventador", 2022)
print(obj.make)
object2 = Const("Urus", 2022)
object2.__init__("Urus", 2022)
object1 = Const("Hurracan", 2021)
print(object1.make)