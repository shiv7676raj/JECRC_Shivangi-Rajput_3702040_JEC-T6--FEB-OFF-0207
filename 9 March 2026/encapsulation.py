#Encapsulation-provide security to data(variables and methods present inside a class)
#access specifiers- 1.public,
#(who can access)   2.protected(soft barrier '_'),
#(the class members)3.private

#PUBLIC-
'''class Temp:
    a,b,*c,d='HELLO'
    def greeting(self):
        print("Good afternoon!")

class c2(Temp):
    pass
t=c2()
print(t.greeting())

#PROTECTED-
class Temp:
    _a=10
    _b='Python'
obj=Temp()
print(obj._a)
print(obj._b)'''

#PRIVATE-
class Temp:
    __a=100
    def __status(self):
        print('Private Method!')
obj=Temp()
#print(obj._a)
#obj._status()
'''
1.by using Syntax
2.get and set method
3.By using @property decorator(setter)

#Using syntax
#obj_name/class_name._CN__prop_name/__method_name (Accessing)
#obj_name/class_name._CN__Member_name=NewValue (Modifying)
print(obj._Temp__a)
print(Temp._Temp__a)
obj._Temp__status()
def new_method():
    print('Method definition got changed')
obj._Temp__a='0123456789'
obj._Temp__status=new_method
print(obj._Temp__a)
obj._Temp__status()

#using get and set method
class Temp:
    __a=67
    def __status(self):
        print('Get and set method!')
    def get(self):
        print(self.__a)
    def set(self,new_val):
        self.__a=new_val
obj=Temp()
obj.get()
obj.set(1)
obj.get()
print(obj._Temp__a)

#Using @property method
class Temp:
    __a=67
    @property
    def get(self):
        print(self.__a)
    @get.setter
    def set(self,new_val):
        self.__a=new_val
obj=Temp()
obj.get
obj.set=10000
obj.get
print(obj._Temp__a)'''
