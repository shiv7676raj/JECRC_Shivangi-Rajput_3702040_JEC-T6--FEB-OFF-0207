
class Car:
    # Class Variables
    wheelers = 4
    engine = 'petrol'
    base_speed = '40kmph'
    max_speed = '120kmph'
    gears = 4

    # Constructor
    def __init__(self, air_bags, security, base_budget, varient, total_sale):
        self.air_bags = air_bags
        self.security = security
        self.base_budget = base_budget
        self.varient = varient
        self.total_sale = total_sale

    @classmethod
    def update_gears(cls, new_gears):
        cls.gears = new_gears
        print(f'No of Gears: {cls.gears}')

    def display_properties(self):
        print('--- Properties of TATA car ---')
        print(f'Number of wheelers: {self.wheelers}')
        print(f'Engine type: {self.engine}')
        print(f'Base speed: {self.base_speed}')
        print(f'Max speed: {self.max_speed}')
        print(f'Gears: {self.gears}')
        print(f'Air bags: {self.air_bags}')
        print(f'Security level: {self.security}')
        print(f'Base budget: {self.base_budget}')
        print(f'Number of variants: {self.varient}')
        print(f'Total sale: {self.total_sale}')

    def update_base_speed(self, new_speed):
        self.base_speed = new_speed
        print(f'New Base Speed: {self.base_speed}')

    def update_max_speed(self, new_speed):
        self.max_speed = new_speed
        print(f'New Max Speed: {self.max_speed}')

    @staticmethod
    def greeting(name):
        print(f"Good morning, {name}!")
# Object
TATA = Car(True, 'level 5', '2 lakhs', 12, 100000)

TATA.greeting("Alice")
print("Properties before updation:")
TATA.display_properties()


print("Properties after updation:")
TATA.update_base_speed('60kmph')
TATA.update_max_speed('150kmph')
TATA.update_gears(6)
TATA.display_properties()

Mahindra = Car(True, 'level 4', '3 lakhs', 10, 80000)
print("Properties of Mahindra car:")
Mahindra.display_properties()