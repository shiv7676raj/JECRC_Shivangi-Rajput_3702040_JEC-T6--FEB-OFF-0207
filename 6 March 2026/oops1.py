class Car:
    #Variables/Properties
    wheelers=4
    engine ='petrol'
    base_speed='40kmph'
    max_speed='120kmph'
    gears=4
#Objects
TATA=Car()
Mahindra=Car()
Suzuki=Car()
Toyota=Car()
#For accessing the properties

print(f' ---Properties of TATA car--- ')
print(f' Number of wheelers: {TATA.wheelers}')
print(f' Engine type: {TATA.engine}')
print(f' Base speed: {TATA.base_speed}')
print(f' Max speed: {TATA.max_speed}')
print(f' Gears: {TATA.gears}')
print()

print(f' ---Properties of Mahindra car--- ')
print(f' Number of wheelers: {Mahindra.wheelers}')
print(f' Engine type: {Mahindra.engine}')
print(f' Base speed: {Mahindra.base_speed}')
print(f' Max speed: {Mahindra.max_speed}')
print(f' Gears: {Mahindra.gears}')
print()
print(f' ---Properties of Suzuki car--- ')
print(f' Number of wheelers: {Suzuki.wheelers}')
print(f' Engine type: {Suzuki.engine}')
print(f' Base speed: {Suzuki.base_speed}')
print(f' Max speed: {Suzuki.max_speed}')
print(f' Gears: {Suzuki.gears}')
print()
print(f' ---Properties of Toyota car--- ')
print(f' Number of wheelers: {Toyota.wheelers}')
print(f' Engine type: {Toyota.engine}')
print(f' Base speed: {Toyota.base_speed}')
print(f' Max speed: {Toyota.max_speed}')
print(f' Gears: {Toyota.gears}')