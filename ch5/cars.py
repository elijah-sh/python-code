# 一个简单的实例

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

for car in cars:
    if car != 'bmw':
        print(car.upper())
    else:
        print(car.title())

for car in cars:
    if car not in cars:
        print(car.upper())
    else:
        print(car.title())