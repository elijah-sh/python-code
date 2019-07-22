# 4、4、3   复制列表

my_foods = ['pizza', 'Spicy Soup', 'Meat sandwich']
friend_foods = my_foods[:]

#friend_foods = my_foods
# 如果这样用则两个值一样  是两个变量执行一个值

my_foods.append('Pancake Fruit')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend`s favorite foods are:")
print(friend_foods)



# 练习
print("=========练习============")

foods = ['pizza', 'Spicy Soup', 'Meat sandwich', 'Grilled cold noodles', 'The Brand']
# 打印前三个
for food in foods[:3]:
    print(food)

print("\n")
# 打印中间三个
for food in foods[1:4]:
    print(food)

print("\n")
# 打印末尾三个
for food in foods[-3:]:
    print(food)

# 你的披萨和我的披萨

my_pizza = ['pizza', 'Spicy Soup', 'Meat sandwich']
friend_pizza = my_pizza[:]

my_pizza.append('Pancake Fruit')
friend_pizza.append('ice cream')

print("My pizza foods are:")
for pizza in my_pizza:
    print(pizza)

print("\nMy friend`s pizza foods are:")
for pizza in friend_pizza:
    print(pizza)

numbers = [1, 2, 3, 4, 5, 6 ,7 ,8 , 9]
for number in numbers:
    for number in numbers:
        print(number)