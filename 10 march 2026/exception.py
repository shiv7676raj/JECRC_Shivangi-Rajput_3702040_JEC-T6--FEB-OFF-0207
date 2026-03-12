'''Exception handling:-
Exception-unauthorized event due to which the flow of execution og program will be stopped.
Output error-1.errorname
             2.reason
             3.line no.
Methods:-
1.try block- Put the problem statement(block of code due to which we might get error)
2.else block- Alternative of try block.If any error is found inside 'try' block,interpreter 
             will move forward towards else block.(If code is correct-output, if not then error)
3.except block- Put the actual solution(resolution for error prone code) for error.Due to this block 
                we can prevent errors.(purple/pink-exception[class],red-error[object],purple-warning) 
4.finally block- The block of code which will be executed whether the code has an error or not and 
                 even after it is resolved.

Exception handling approaches:
1.Specific Exception handling
2.Generic Exception handling
3.Default Exception handling
'''
#1.Specific Exception handling-Used when we are aware of error/exception
# try:
#     problem statement
# except ErrorName:
#     resolution/solution code
'''n1,n2=21,0
try:
    res=n1/n2
    print(res)
except ZeroDivisionError:
    print("Don't choose 0 as second number")
print('Code after try and except!')'''

#2.Generic Exception handling-There is no need to pass any particular exception class name.
#                             We can use 'Exception' class for them
#Using it, we can't handle keyboard interruptions
'''try:
    a,b,c=1,2
except Exception:
    print('For performing MVC,no of variables should be equal to no of values!')
try:
    print(a,b,c)
except NameError:
    print('Identifiers are not there in memory')'''

#3.Default Exception handling-Used when we are not aware of error/exception
# import time
# try:
#     while True:
#         print(time.time())
# except:
#     print('Loop got stopped!')

'''raise:Keyword used to throw an error in between a program. It is used to create a custom exception.
Exception Creation:-
1.Custom Exception(raise)
2.User Defined Exception(raise)
3.Assertion Exception(assert)'''

#1.Custom Exception(raise)-We use prebuilt exception classes according to our requirement
# raise ValueError('message')-creates an object of ValueError class and passes the message to it. 
#                             This message will be printed when the error is raised.
# ValueError:message

'''num=17
if num>=18:
    print('You are eligible for voting!')
else:
    raise NameError('You are not eligible for voting!')'''

#2.User Defined Exception(raise)-We can create our own exception classes based upon our needs by 
# inheriting the 'Exception' class.We can also provide names to those classes according to user cases.
'''class MyException(Exception):
    pass

#raise MyException('This is a user defined exception!')

n1,n2=21,3
if n2==0:
    raise MyException('Second number should not be zero!')
else:    
    res=n1/n2
    print(res)'''

#3.Assertion Exception(assert)-Created by using a keyword named 'assert'.Used to check the 
#                              correctness of code by putting some conditions.
# assert<contdition>,print(ERROR)
# print('Output')
s=input('Enter a string: ')
assert s==s[::-1],print('Not palindrome')
print('Palindrome')