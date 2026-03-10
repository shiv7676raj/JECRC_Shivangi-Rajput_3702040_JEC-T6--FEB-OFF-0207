'''
Abstraction-hiding the internal implementation and showing only functionality to end user
Abstract method-functionor method only having declaration but ot definition
Abstract class-class consisting of at least one abstract method
Concrete class-consists of 0 abstract method
abc-Module
ABC-Abstract base class
'''
from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def generate_pin(self):
        pass
    @abstractmethod
    def forget_pin(self):
        pass
    @abstractmethod
    def check_bal(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def deposit(self):
        pass

class SBI_ATM(ATM):
    def generate_pin(self):
        print('To geenrate the ATM pin')
    def forget_pin(self):
        print('To change the pin')
    def check_bal(self):
        print('To check the balance')
    def withdraw(self):
        print('To withdraw the money')
    def deposit(self):
        print('To save the money by depositing')

obj=SBI_ATM()
obj.generate_pin()
obj.forget_pin()
obj.check_bal()
obj.deposit()
obj.withdraw()
