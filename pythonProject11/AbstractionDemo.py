from abc import ABC, abstractmethod


class AbstractClass(ABC):

    def secret(self):
        x = 150
        y = 160
        print(x, y)

    @abstractmethod
    def nigora(self):
        name = "Johny"
        name1 = "Tasha"
        name2 = "Artyom"
        name3 = "Lola"
        name4 ="Ferin"
        print("Hi, welcome to our bootcamp" + " " + name)
        print("Hi, welcome to our bootcamp" + " " + name1)
        print("Hi, welcome to our bootcamp" + " " + name2)
        print("Hi, welcome to our bootcamp" + " " + name3)
        print("Hi, welcome to our bootcamp" + " " + name4)




class Tojtech(AbstractClass):
    def nigora(self):
        print("The best bootcamp")


obj = Tojtech()
obj.secret()
obj.nigora()