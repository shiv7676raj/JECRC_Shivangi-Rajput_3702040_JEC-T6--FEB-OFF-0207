#Operator Overloading-Asking the operator to work on user defined data types 
# by invoking respective magic methods.
#Magic method/dundar-special type of methods in which double underscores will 
# be there at the starting and ending of method's name
'''Syntax:-
class className:
    def __init__(self, val):
        self.val=val
    def __add__(self, other_obj):
        return self.val+other_obj.val
    
obj1=className(val1)
obj2=className(val2)
print(obj1+obj2)  #obj1.__add__(obj2)'''

class ops:
    def __init__(self, val):
        self.val=val
    def __str__(self):
        return str(self.val)
    def __add__(self, *other_obj):
        tot=self.val
        for i in other_obj:
            tot+=i.val
        return tot
    # def add(self, *args):
    #     tot=self.val
    #     for i in args:
    #         tot+=i.val
    #     return tot
    def __sub__(self, other_obj):
        return self.val-other_obj.val
    def __mul__(self, other_obj):
        return self.val*other_obj.val
    def __floordiv__(self, other_obj):
        return self.val//other_obj.val
    def __truediv__(self, other_obj):
        return self.val/other_obj.val
    def __mod__(self, other_obj):
        return self.val%other_obj.val
    
'''print(ops(10.10)+ops(20))
print(ops(100)-ops(20))
print(ops(10)*ops(20))
print(ops(100)//ops(20))
print(ops(100)/ops(20))
print(ops(100)%ops(20))'''
#print(ops.add(ops(100),ops(200),ops(300),ops(400),ops(500)))
print(ops(10)+ops(50))
