# OOPS
class Person:
    #These are setters
    #SELF HAS TO BE THER IN INPUT AND WHEN STATING VARIABLES
    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        self.__age = age

        #THESE ARE GETTERS
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age


    #No need to show self outside class
p1 = Person()
p1.set_name("John")
p1.set_age("23")
print(p1.get_name(),p1.get_age())

p2 = Person()
p2.set_name("name")
p2.set_age(25)
print(p2.get_name(),p2.get_age())






# it provides security (OOPS)
#varaible with (self.__) cannot be changed outside the class


# 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 #

class Person:
    __nump =0 #this is a class object
    #used constructor isntead of setters
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__class__.__nump +=1
        #THESE ARE GETTERS
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_nump(self):
        return self.__class__.__nump


    #Now you can put them directly when instializing
p1 = Person("John",45)
print(p1.get_name(),p1.get_age())
print(p1.get_nump())
p2 = Person("ann",32)
print(p2.get_name(),p2.get_age())
print(p2.get_nump())
print(p1.get_nump())

#HERE NUMP is like adding the numebr of ppl that is there, (total number of peopl)
#print(Person.get_nump())#())#())#())#))


#its not that u might not need setters when there is init but u can have it if thats needed
#things like age changes as years pass so u might need setter for that and not constructor (initalizer)







# 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 #

class Person:
    __nump =0 #this is a class object
    #used constructor isntead of setters
    def __init__(self,name,age):
        self.name = name
        self.age = age
       # self.Person.__nump +=1
        #THESE ARE GETTERS
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_nump(self):
        return Person.__nump#You can specify the places with the class name instead of that __class__ and things


    #Now you can put them directly when instializing
p1 = Person("John",45)
print(p1.get_name(),p1.get_age())
print(p1.get_nump())
p2 = Person("ann",32)
print(p2.get_name(),p2.get_age())
print(p2.get_nump())
print(p1.get_nump())

#HERE NUMP is like adding the numebr of ppl that is there, (total number of peopl)
#print(Person.get_nump())#())#())#())#))


#its not that u might not need setters when there is init but u can have it if thats needed
#things like age changes as years pass so u might need setter for that and not constructor (initalizer)



# 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 #



class Employee(Person):#every variables ni person is now in empolyee
    def __init__(self,name,age,role):
        Person.__init__(self,name,age)
        self.__role = role
    def get_role(self):
        return self.__role

e1 = Employee("John",45,"Manager")
print(e1.get_name(),e1.get_age(),e1.get_role())
e2 = Employee("Bill",32, "CEO")
print(e2.get_name(),e2.get_age(),e2.get_role())


