# 3.3 组织列表 sort永久性排序排序
print("======================")
print("==========组织列表 =======")

# 3.3.1 sort永久性排序排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
# 正序 和 倒序
print(cars)

cars.sort(reverse=True)
print(cars)

# 3.3.2 sorted()临时性排序排序
print("\n======================\n")
print("3.3.2 sorted()临时性排序排序")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)

# 3.3.3 倒着打印列表 .reverse()
print("\n======================\n")
print("3.3.3 倒着打印列表")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
cars.reverse()
print(cars)

# 3.3.4 列表长度
print("\n======================\n")
print("3.3.4 列表长度")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

# 练习
print("\n======================\n")
print("练习")

trip = ['Dali', 'Japan', 'London', 'Xuchang', 'HongKong', 'Lasa']

# 原顺序
print(trip)
# 使用sorted（） 按字母临时排序
print(sorted(trip))
print(trip)
print("按字母相反的方向排")

# 使用sorted（） 按字母相反的方向排  不用修改
# TODO 不会写
print(  sorted(trip).reverse() )

#用reverse()修改顺序 再修改回来
print("用reverse()修改顺序 再修改回来")

print(trip)
trip.reverse()
print(trip)
trip.reverse()
print(trip)

# 用sort（） 排顺序 再排回来
print("用sort（） 排顺序 再排回来")

trip.sort()
print(trip)
trip.reverse()
print(trip)


# 索引错误
#print(trip[6])
print(trip[-6])

trip = []
print(trip[-1])