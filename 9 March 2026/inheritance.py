#types of Inheritance:
#1.Single level-single child and parent, one time derivation only
#Constructor chaining-calling parent's class constructor from inside child calss's constructor
'''class Parent:
    bal=100000
    def __init__(self,members):
        self.members=members
    def desc(self):
        print("Parent class")

class Child(Parent):
    def __init__(self,child_name, *args):
        self.child_name=child_name
        super().__init__(args)

    def display(self):
        super().desc()

c=Child('Mom','Dad')
print(c.bal)    #Inherited class variable
c.desc()        #Inherited instance method
print(c.members)
print(c.child_name)'''

#2.Multi level(sequential)-deriving properties from one class to another by 
# considering more than one level
'''class Class1:
    a='class_1'

class Class2(Class1):
    b='class_2'

class Class3(Class2):
    c='class_3'

class Class4(Class3):
    d='class_4'

class Class5(Class4):
    e='class_5'

obj=Class5()
print(obj.a,obj.b,obj.c,obj.d,obj.e)'''

#3.Multiple level-multiple parent class and one single child
'''class Parent1:
    a=10
class Parent2:
    b=100
class Parent3:
    c=1000
class Parent4:
    d=10000
class Child(Parent1,Parent2,Parent3,Parent4):
    pass
print(Child.a,Child.b,Child.c,Child.d)'''

#4.Hierarchical-single parent class and multiple child class
'''class Parent():
    gold='2kg'
    silver='10kg'
    nflats=12

class youngest(Parent):
    name='Michael'
class Eldest(Parent):
    e_name='Rob'
class sis(Parent):
    s_name='Sophia'

print(youngest.gold)
print(Eldest.silver)
print(sis.nflats)'''

#5.Hybrid-mix of more than one type of inheritance

#--------------------------------------------------------------------------

#Polymorphism-a method name or operator used to perform two or more different operations
#method overloading(based upon no of arguments,the respective method block will be executed) 
# will act as method overriding in python
#Method overriding-overriding the previous method's address with the latest one
#Monkey Patching-process of storing the prev method's address inside a variable before 
# overriding the method area's address.Using that variable we can access the prev's method method area.
'''class Temp:
    def sum(self, a,b):
        return a+b
    add_two_numbers=sum
    def sum(self, a,b,c):
        return a+b+c
    
t=Temp()
print(t.add_two_numbers(1,2))
print(t.sum(1,2,3))'''

#Operator Overloading-
class MyDataType:
    def __init__(self,val):
        self.val=val
    def __add__(self, ano_obj):
        return self.val+ano_obj.val

obj1=MyDataType(10)
obj2=MyDataType(20)
print(10+20)
print(obj1+obj2)

