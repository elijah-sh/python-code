message = "Hello Python World! "
# 首字母大写
print(message.title())
# 转小写
print(message.lower())
# 转大写
print(message.upper())
# 换号
print(message.upper() + "\n" + message.lower())
# 制表符 table
print(message.upper() + "\t" + message.lower())
message = " Hello Python World! "
# 右去空格 删除空白
print(message.rstrip())
# 左去空格
print(message.lstrip())
# 两端去空格
print(message.strip())

#  练习1 将用户名存到变量中，并向改用户显示一条消息

name = "Shen Sai"
print("Hello " + name + ", would you like to learn some Python today?")

# 练习2 将用户名存到变量中，并用 小写 大写 和首字母大写的方式显示这个人吗

honey = "Shen Sai"
print(honey.lower())
print(honey.upper())
print(honey.title())

# 练习三 将名人和他说的名言打印出来
print("Jesus said,  \"I am truth,road and left.\"")

# 练习四  将名人的名字存到 famous_person 中，再创建要显示的消息，并将其储存在变量message中，然后打印

famous_name = "Jesus"
famous_message = famous_name + "said, \"I am truth,road and left.\""
print(famous_message)

# 练习五 剔除名字中的空白
person_name = " shen shuai hu \n  \t" + " "
print (person_name)
print (person_name.lstrip())
print (person_name.rstrip())
print (person_name.strip())