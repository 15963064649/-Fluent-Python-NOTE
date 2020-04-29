#python标准库用C实现了丰富的序列类型：
#容器序列(引用类型):
#    list、tuple、collections.deque     可存放不同类型的数据
#扁平序列(值类型)：
#    str、byte、bytearray、memoryview和array.array
#
#列类型还可以按照能否被修改来划分：
#变序列：
#   list、bytearray、array.array、collections.deque和memoryview
#可变序列：
#   tuple、str、bytes


#python列表推导：
#与传统写法的差异：
#    传统：
symbols = '@#$%^'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

#列表推导写法：
symbol = '@#$%^&*('
codes = [ord(symbol)for symbol in symbols]
print(codes)

'''
注意：通常只用列表推导创建新的列表
Python3之后的版本使用列表推导之后原数组的列表也被保留了，不会再发生变量泄露
'''


#实际上python内置的filter和map也能实现列表推导的效果：即对可迭代类型中的元素过滤或加工，但是其可读性大打折扣
symbols = '@#$%^&*('
codes = [ord(symbol)for symbol in symbols]
print(codes)
#############
codes = list(filter(lambda c: c > 27, map(ord, symbols)))
print(codes)