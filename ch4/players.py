# 4.4使用列表的一部分
# 切片

players = ['LiuXiang', 'YaoMing', 'DengYaping', 'LinShuhao', 'Michael']
print(players[0:3])
print(players[1:4])
# 前者省略是0位置  后着省略是length-1位置
print(players[:4])
print(players[2:])
#  负数 是到末尾的距离  -3 即 最后三个数
print(players[-3:])

# 4、4、2 遍历切片

players = ['LiuXiang', 'YaoMing', 'DengYaping', 'LinShuhao', 'Michael']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
# 用途： 统计游戏分数 先排序 再去前三个


