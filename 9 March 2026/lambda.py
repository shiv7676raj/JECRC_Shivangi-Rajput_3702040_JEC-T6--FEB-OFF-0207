'''
lambda(Anonymous function)->it is a keyword used to create anonymous function.
                          ->To call this, we can store the address of lambda inside a variable.
                          ->By invoking the var_name, we can call the function.
lambda args:<exp>
lambda args:<exp_1> if <condition> else <exp_2>

# res=lambda a,b:a+b
# print(res)
# print(res(1,2))

# (lambda a,b:print(a+b))(int(input('First Num:')),int(input('Second Num:')))

# WAP to find the square of a num if it is even.
# num=int(input('Enter a number:'))
# if num%2==0:
#     print(num**2)
#OR
res=lambda num:print(num**2) if num%2==0 else None
res(10)
#OR
(lambda num:print(num**2) if num%2==0 else None)(int(input()))'''

#WAP to find the square of a num if it is even otherwise print cube of it
res=lambda num:print(num**2) if num%2==0 else print(num**3)
res(3)

#check whether a num is positive, negative or zero
res=lambda num:print('POS') if num>0 else print('NEG') if num<0 else print('ZERO')
res(int(input()))