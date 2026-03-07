# def add_nums(*args):
#     print(args, type(args))
#     total=0
#     for num in args:
#         total+=num
#     print(f'added total: {total}')

# add_nums(1,2,3)

# def add_nums(*args):
#     args=list(args)
#     print(args, type(args))
#     total=0
#     for num in args:
#         total+=num
#     print(f'added total: {total}')

# add_nums(1,2,3)

# create a function which will take n no of inputs and return only int and floating point numbers. please make sure that user is capable of passing all type of values like list, tuple, set, dict, string, bool etc. and you need to return only int and float point numbers.


# def filter_int_float(*args):
#     args=list(args)
#     # print(args, type(args))
#     sum=0
#     for item in args:
#         if type(item) == int or type(item) == float:
#             sum+=item
#     print(sum)

# filter_int_float(*eval(input("Enter list of values: ")))
##

# def func_name(**kwargs):
#     print(kwargs, type(kwargs))


# func_name(name="John", age=30, city=['Eppelheim','Berlin'])



#CREATE A FUNCTION WHICH WILL RETURN A LIST OF PRIME NUMBERS ALSO MAKE SURE THAT USER CAN PASS N NUMBER OF INPUTS .FOR CHECKING WHETHER A NUMBER IS PRIME OR NOT , YOU CAN CREATE ONE FUNCTION

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(*args):
    primes = []
    for num in args:
        if is_prime(num):
            primes.append(num)
    return primes

print(get_primes(*eval(input("Enter numbers: "))))