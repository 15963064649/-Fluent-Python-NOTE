#此处用一个小例子展示嵌套元组的拆包操作
metro_areas = [
    ('Tokyo','JP',36.933,(35.689722,139.691667)),           #元组内四个元素，最后一个元素是一个坐标
    ('Delhi NCR','IN',21.935,(28.613889,77.208889)),
    ('Mexico','MX',20.142,(19.433333,-99.133333)),
    ('New York-Newark','US',20.104,(40.808611,-74.020386)),
    ('Sao Paulo','BR',19.469,(-23.547778,-46.635883))
]

print('{:15} | {:^9} | {:^9}'.format('','lat.','long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longtitude) in metro_areas:   #把输入元组的最后一个元素拆包到由变量构成的元组里，这样就获取了坐标
    if longtitude <= 0:                                     #此处把输出限制到西半球的城市。
        print(fmt.format(name, latitude, longtitude))

'''在python3之后的版本中不允许将元组作为函数参数。'''


############################################################

#用namedtupel函数给python元组命名：
#namedtupel函数介绍：
#   collections.namedtupel函数是一个工厂函数，用来构建构建一个带字段名的元组和一个有名字的类。
#       这个带名字的类对程序的调试起很大作用。
#   用namedtupel构建的类的示例所消耗的内存跟元组是一样的，因为字段名都被存在对应的类里面。
#       这个示例跟普通的实例比起来要小一些，因为python不会用__dict__来存储这些实例的属性。

from collections import namedtuple
City = namedtuple('City', 'name country population coordinates') #namedtuple需要两个参数，一个类名，一个字段名。
                                              #字段名需要是字符串组成的可迭代对象或是空格隔开的字段名组成的字符串。
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)                                          #可通过字段名获取信息。
print(tokyo[1])                                                  #可通过字段位置获取信息。

#具名元组的属性和方法如下：
print(City._fields)                   #一个包括所有字段名的元组。

LatLong = namedtuple('LatLong','lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)        #此处用一个可迭代对象来生成一个类的实例，作用与City(*delhi_data)一样。
delhi._asdict()                       #_asdict()把具名元组以collections.OrderedDict的形式返回。
for key, value in delhi._asdict().items():
    print(key + ':', value)