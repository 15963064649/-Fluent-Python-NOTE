#此处笛卡尔积的计算实现过程如下：

#加入你需要一个列表，表里是3种不同尺寸的T恤衫，每个尺寸有两个颜色，列表推导写法为：
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
Tshitr = [(color,size) for color in colors for size in sizes] #这里得到的是先以颜色排列，再以尺码排列顺序
print(Tshitr)

#迭代写法为：
for color in colors:
    for size in sizes:
        print((color,size))


'''
则第一章中的纸牌可以写为：
class Card:
    def __init__(self):
        self._cards = [Card(rank,suit)for rank in ranks for suit in suits]
'''