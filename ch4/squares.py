#  1-10 的平方

squares = []
for value in range(1,11):
    print(value)
    square = value**2
    squares.append(square)

print(squares)


# 优化代码

squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

# 对数字列表简单统计计算

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))


# 列表解析

squares = [value**2 for value in range(1,10)]
print(squares)

#  联系

# 1、数到 20
numbers = [num for num in  range(1,21)]
print(numbers)

# 2、一百万
numbers = [num for num in  range(1,10**6+1)]
print(numbers)

# 3、计算1到 1000 000 的综合
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4、1-20 的奇数
odd = [odd for odd in  range(1,21,2)]
print(odd)

# 5、 3-30 3的倍数
multiple3 = [num for num in  range(3,31,3)]
print(multiple3)

# 6、 1-10 的立方
cube  = [num**3 for num in  range(1,11)]
print(cube )
