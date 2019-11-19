# Section04-3
# Python Data Type(자료형)
# List, Tuple

# List(순서o, 중복o, 수정o, 삭제o)

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# Indexing
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])

# Slicing
print(d[0:2])
print(e[2][1:3])

# operation
print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')

# list edit, delete
c[0] = 77
print(c)
c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)

del c[-1]
print(c)
print()
print()
print()

# list function
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)

y.sort()
print(y)
y.reverse()
print(y)
y.insert(2, 7)
print(y)

y.remove(2)
print(y)
y.remove(7)
print(y)

y.pop()
print(y) # LIFO(Last In First Out)

ex = [88, 77]
y.extend(ex)
print(y)
# y.append(ex)
print(y)

# 삭제 : del, remove, pop

# Tuple (순서o, 중복o, 수정x, 삭제x)

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][1])

print(d[2:])
print(d[2][0:2])

print(c + d)
print(c * 3)

print('*' * 40)
# Tuple Function
z = (5, 2, 1, 3, 1)

print(z)
print(3 in z)
print(z.index(5))
print(z.count(1))
