#section04-4
# python data type(Type)
# dictionary, set type

# Dictionary : 순서x, 중복x, 수정o, 삭제o

# Key, Value (Json) -> MongoDB
# 선언(Declaration)

a = {'name': 'Kim', 'Phone': '010-7777-7777', 'birth': 870214}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]}

# print(type(a))

# 출력
print(a['name'])
print(a.get('name'))
print(a.get('address'))
print(c['arr'][1:3])

# Dictionary 추가
a['address'] = 'Seout'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3)
print(a)

# keys, values, items

print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))
print(a.items())

print(list(a.items()))
print(1 in b)
print(2 in b)
print('name' in a)
print('name2' not in a)