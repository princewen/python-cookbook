"""
问题：
如果一个可迭代对象的元素个数超过变量个数时，会抛出一个ValueError，那么怎样才能从这个可迭代对象中解压出N个元素出来?

解决方案：
Python的星号表达式可以用来解决这个问题
"""


"""假设你现在有一些用户的记录列表，每条记录包含一个名字、邮件，接着 就是不确定数量的电话号码。 你可以像下面这样分解这些记录:"""

record = ('Dave','dave@example.com','773-555-1212','847-555-1212')
name,email,*phone_numbers = record

#output: Dave
print (name)

#output : ['773-555-1212', '847-555-1212']
#注意这里变量名不是*phone_numbers,返回值是一个列表
print (phone_numbers)

"""星号表达式也能用在列表的开始部分"""
*trailing,current = [10,8,7,1,9,5,10,3]
#Output : [10, 8, 7, 1, 9, 5, 10]
print (trailing)

"""星号表达式在迭代元素为可变长元组的序列时是很有用的"""
records = [('foo',1,2),('bar','hello'),('foo',3,4)]

#output :
# foo 1 2
# bar hello
# foo 3 4
def do_foo(x,y):
    print ('foo',x,y)

def do_bar(s):
    print ('bar',s)

for tag,*args in records:
    if tag=='foo':
        do_foo(*args)
    elif tag=='bar':
        do_bar(*args)

"""星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。"""

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
#Output : ['*', '-2', '-2', 'Unprivileged User']
print (fields)


"""有时候，你想解压一些元素后丢弃它们，你不能简单就使用*， 但是你可以使用一个普通的废弃名称，比如_或者ign。"""
record = ('ACME', 50, 123.45, (12, 18, 2012))
name,*_,(*_,year) = record
#Output : 2012
print (year)