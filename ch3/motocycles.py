# 修改、添加和删除元素
print("======================")
print("==========修改、添加和删除元素=======")
motocycles = ['honda', 'yamaha', 'dayang']
print(motocycles)

# 改变第一个元素
motocycles[0] = 'xiaoniao'
print(motocycles)

# 列表末尾添加一个元素
motocycles.append('tengling')
print(motocycles)

# 先创建空列表 再添加元素

motocycles = []
print(motocycles)
motocycles.append('honda')
motocycles.append('yamoha')
motocycles.append('suzuki')
print(motocycles)

# 列表中插入元素

motocycles.insert(0,'xiaoniu')
print(motocycles)

# 1、删除元素
del motocycles[0]
print(motocycles)
del motocycles[1]
print(motocycles)

# 2、使用pop() 删除元素

motocycles = ['honda', 'yamaha', 'dayang']
print(motocycles)

popped_motocycles = motocycles.pop()
print(motocycles)
print(popped_motocycles)

# 3、弹出任何位置处的元素
motocycles = ['honda', 'yamaha', 'dayang']
last_owed = motocycles.pop()
print("The first motorcycle I owned was a  " + last_owed.title() + ".")

motocycles = ['honda', 'yamaha', 'dayang']
frist_owned = motocycles.pop(0)
print("The first motorcycle I owned was a  " + frist_owned.title() + ".")

# 4、根据值删除元素
motocycles = ['honda', 'yamaha', 'dayang']
motocycles.remove('dayang')
print(motocycles)


# 练习 邀请嘉宾进晚餐 3.4

guess = ['shensai', 'zhangfei', 'wancong']
print(guess)

# 3.5 万聪不来了， 3.6我又叫了成成
leave_guess = guess.pop()
print(leave_guess + " 去找对象了，不来吃饭了")
guess.append("chengcheng")
print(guess)

# 3.6 又换了一张大一点的餐桌  可以多邀请一些人
guess.insert(0, "chenchen")
guess.insert(0, "xinchun")
guess.insert(0, "tiantian")
guess.append("mengle")
print(guess)

# 3.7 不幸的消息  大餐桌不能用了 现在只能两个人

print(guess[0] + " and " + guess[1] + ", 只能邀请你们两个了")

to_sorry_guess = guess.pop()
print("I am Sorry:" + to_sorry_guess)
to_sorry_guess = guess.pop()
print("I am Sorry:" + to_sorry_guess)
to_sorry_guess = guess.pop()
print("I am Sorry:" + to_sorry_guess)
to_sorry_guess = guess.pop()
print("I am Sorry:" + to_sorry_guess)
to_sorry_guess = guess.pop()
print("I am Sorry:" + to_sorry_guess)

print(guess)

# 删除所有的
del guess[0]
del guess[0]
print(guess)