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
#   collections.namedtupel函数是一个工厂函数