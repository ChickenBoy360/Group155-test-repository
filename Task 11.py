'''
# 6
lst = [int(i) for i in input().split()]
lst2 = []
if len(lst) == 1:
    lst2 = lst[::1]
else:
    for i in range(len(lst)-1):
        lst2.append(lst[i - 1] + lst[i + 1])
    lst2.append(lst[-2] + lst[0])
print(lst2)
'''

'''
# 9
lst = ['aaads', 'adsds', 'asdaa', 'adsds']
lst.sort(key=lambda x: x.count('a'), reverse=True)
print(lst)
'''

'''
tup = (1, 4, 5, 6, 4)
if 4 in tup:
    print(tup.index(4))
else:
    print('8 not in tup')
'''

'''
tup = (1, 4, 5, 6)
print(len(tup))
for el in tup:
    print(el)
print('четные')
for i in range(len(tup)):
    if tup[i] % 2 == 0:
        print(tup[i])
print('--------------------------')
for ind, el in enumerate(tup):
    print(ind, el)
'''

'''
s = 'hello world'
tup = tuple(s)
print(tup)
'''

'''
lst = [int(i) for i in input().split()]
tup = tuple(lst)
print(tup)
'''

'''
info = ('Jhon', 'Watson', 31)
name, surname, age = info
print(name)
print(surname)
print(age)
'''

'''
lst = [i for i in range(0, 10)]
print(lst)
tup = tuple(lst)
print(f'Сумма цифр: {sum(lst)}')
'''

'''
long_word = ('т', 'т', 'и', 'и', 'а', 'а', 'а')
print('Количествол букв т: ', long_word.count('т'))
print('Количествол букв и: ', long_word.count('и'))
print('Количествол букв а: ', long_word.count('а'))
'''

'''
week_temp = (26, 29, 34, 32, 28, 26, 23)
sum_temp = sum(week_temp) 
days = len(week_temp)
mean_temp = sum_temp / days
print(int(mean_temp))
'''
























