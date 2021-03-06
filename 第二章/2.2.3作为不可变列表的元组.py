#介绍一下元组用作不可变列表时与列表的区别和相似之处。
#--------------------------------------------------------------------------------------------------
#                                列表            元组                   作用
#s.__add__(s2)                    *               *                 s+s2，拼接
#s.__iadd__(s2)                   *                                 s+=s2，就地拼接
#s.append(s2)                     *                                 在尾部添加一个新元素
#s.clare()                        *                                 删除所有元素
#s.__contains__(e)                *               *                 s是否包含e
#s.copy()                         *                                 列表的浅复制
#s.counte(e)                      *               *                 e在s中出现的次数
#s.__delitem__(p)                 *                                 把位于p的元素删除
#s.extend(it)                     *                                 把可迭代对象it追加给s
#s.__getitem__(p)                 *               *                 s[p],获取p位置的元素
#s.__getnewargs__()                               *                 在pickle中支持更加优化的序列化
#s.index(e)                       *               *                 在s找到第一次出现e的位置
#s.insert(p, e)                   *                                 在p之前插入e元素
#s.__iter__()                     *               *                 获取s的迭代器
#s.__len__()                      *               *                 len(s),获取元素的数量
#s.__mul__(n)                     *               *                 s*n,n个s的重复拼接
#s.imul(n)                        *                                 s和n就地拼接
