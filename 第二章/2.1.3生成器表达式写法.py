#生成器：
#   生成器准确的来说就是一个生成器表达式。
#   他的格式与列表推导差别不大，只不过把方括号换成圆括号。

#生成器的作用：
#   因为列表生成器的作用就一个：生成列表，因此想生成其他类型的序列，生成器就派上了用场。
#   生成器表达式是比列表推导表达式更好的选择，因为生成器协议背后遵循了迭代器协议，可以逐个地产出元素。
#   列表推导是先生成一个完整的列表，再把列表传递到某个构造函数里面。
#   相较于生成器来说，列表推导占用的内存更多。

#举例：
symbols = '@#$%^&*'
tuple(ord(symbol) for symbol in symbols)              #如果只有一个参数则不需要额外的括号
#array.array类型：
import array
array.array('I',(ord(symbol) for symbol in symbols))  #如果作为两个参数中的一个则需要加上括号


#用生成器表达式计算笛卡尔积：
colors = ['white', 'black']
sizes = ['S', 'M', 'L']
for Shirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(Shirt)
'''
运行结果如下：
    white S
    white M
    white L
    black S
    black M
    black L
'''