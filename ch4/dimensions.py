# 4、5   元组  不可变的列表
print("元组")
# 4、5、1 定义


dimensions = (200, 50)
# 不可更改
# dimensions[1] = 111
print(dimensions[0])
print(dimensions[1])

for di in dimensions:
    print(di)

print("================")
dimensions = (200, 40)
print("Original dimensions")
for dimension in dimensions:
    print(dimension)
#  此时的赋值是合法的
dimensions = (400, 100)
print("\nModified dimensions")
for dimension in dimensions:
    print(dimension)






print("================")
print("练习 4-13")
buffet = ('冰淇淋', '刨冰', '经典风爪', '肥肠', '黑胡椒猪肉')
print("Original buffet")
for buffet in buffet:
    print(buffet)
#  此时的赋值是合法的
buffet = ('冰淇淋', '蜜汁猪肉', '经典风爪', '巧克力蛋糕', '黑胡椒猪肉')
print("\nModified buffet")
for buffet in buffet:
    print(buffet)