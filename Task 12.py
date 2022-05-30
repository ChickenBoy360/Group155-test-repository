'''
# 11  сгенерировать список всех простых чисел до 100 с помощью генератора
print([int(x) for x in range(2, 100) if
       x == 2 or x == 3 or x == 5 or x == 7 or x > 9 and x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0])
'''

'''
print([int(x) for x in range(2, 100) if all([x % y != 0 for y in range(2, x)])])
'''

'''
# 12
lst = [5, 2, 6, 1]
i = 0
while i < len(lst):
    if i % 2 == 1:
        lst.insert(i, 0)
        i += 1
    i += 1
print(lst)
'''

'''
# 13
lst = []
n = int(input('enter n: '))
for i in range(1, 100):
    for j in range(1, i + 1):
        if len(lst) == n:
            break
        print(i, end=' ')
        lst.append(i)
'''

'''
#добавления ключа и значения в пустой словарь
d = dict()
n = int(input())
for i in range(n):
    key = input()
    value = int(input())
    if key not in d:
        d[key] = value
print(d)
'''













