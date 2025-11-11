class person:
    __nump= 0
    def __init_(self):
        self.__class__.__nump+=1
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
         self.__age = age

p1 = person()
p1.name = "John"
p1.age = 45
print(p1.name,p1.age)


p2 = person()
p2.name = "Johnson"
p2.age = 25
print(p2.name,p2.age)