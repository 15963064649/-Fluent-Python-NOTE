#此处介绍元组用作“没有字段名的记录”的作用，因为大多数教程把元组成为不可变得列表，所以元组的这个作用没有被介绍过。

#   如果只把元组用作不可变的列表，那么元组其他的信息（如：总数和位置）就变得可有可无。
#   如果只把元组当做一些字段的集合，那么数量和位置信息就变得非常重要了。

##########讲解一些把元组用作记录的例子：
#   首先声明几条数据：
lax_coordinates = (33.9425, -118.408056)                          #洛杉矶国际机场的经纬度
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)   #东京市的一些信息，市名，年份，人口，人口变化和面积。
traveler_ids = [('USA', '31195855'),
                ('BRA', 'CE342567'),
                ('ESP', 'XDA205856')]                             #一个元组列表，格式为(country_code, password_code)

######################################对数据的一些操作：

#元组拆包：
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)                                     #‘%’格式运算符能被匹配到对应的元素上。

for country, _ in traveler_ids:                                   #元组中第二个元素被占位符 ‘_’ 覆盖
    print(country)
#拆包操作对比city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)一行：
#   后者一行声明完成赋值。
#   前者一个‘%’运算符就把passport元组里的元素对应到了print函数 的 格式字符串空挡 中。
'''三者都是对元组拆包的应用'''

#   元组拆包的一些应用：
#       1.平行赋值：
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates                             #执行元组拆包
print(latitude)
print(longitude)

#       2.无中间变量地交换两个变量的值：
b, a = a, b

#       3.还可以用*运算符把一个可迭代对象拆开作为函数的参数：
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))
qoutient, remainder = divmod(*t)
print(qoutient, remainder)


'''一个例子'''
#获取str中的路径和文件名
import os
_, fireName = os.path.split('home/luciano/.ssh/idirsa.pub')
print(fireName)