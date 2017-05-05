"""
问题：现在有一个包含N个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给N个变量?
"""

"""
解决方案：任何的序列(或者是可迭代对象)可以通过一个简单的赋值语句解压并赋值给多个变量。 唯 一的前提就是变量的数量必须跟序列元素的数量是一样的。
"""

p = (4,5)
x,y = p
#output : 4
print (x)
#output : 5
print (y)

data = ['ACME',50,91.1,(2012,12,21)]
name,shares,price,date = data
#output : (2012, 12, 21)
print (date)

name,shares,price,(year,mon,day) = data
#output : 2012
print (year)
#output : 12
print (mon)
#output : 21
print (day)

"""如果变量个数和序列元素的个数不匹配，会产生一个异常。"""
p = (4,5)
#Output : ValueError: not enough values to unpack (expected 3, got 2)
#x,y,z = p

"""实际上，这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。 包括 字符串，文件对象，迭代器和生成器。"""
s='Hello'
a,b,c,d,e = s
#output : a
print (a)
#output : e
print (e)

"""有时候，你可能只想解压一部分，丢弃其他的值。对于这种情况Python并没有提供特殊 的语法。 但是你可以使用任意变量名去占位，到时候丢掉这些变量就行了。"""

data = ['ACME',50,91.1,(2012,12,21)]
_,shares,price,_ = data
#output :  50
print (shares)
#output : 91.1
print (price)

