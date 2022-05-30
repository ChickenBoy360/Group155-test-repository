'''
Task1
number = input('Enter number: ')
mult = 1
s = 0
count1 = count2 = 0
for i in range(len(number)):

    if int(number[i]) % 2 == 0:
        count1 += 1
    else:
        count2 += 1

    s += int(number[i])

    if i == 0 or i == 2 or i == 5:
        mult *= int(number[i])

if count1 > count2:
    print(s)
else:
    print(mult)
'''

'''
Task 5
s = input()
s += ' '
s1 = ''
for i in s:
    if i != ' ':
        s1 += i
    elif s1:
        if s1.isdigit():
            print(s1)
        s1 = ''
'''

'''
Task 6 so so
s = input()
pair_lower = pair_upper = 0
for i in range(1, len(s)):
    if s[i - 1].islower() and s[i].islower():
        pair_lower += 1
    if s[i - 1].isupper() and s[i].isupper():
        pair_upper += 1
    print(pair_lower)
    print(pair_upper)
'''

# Списки

'''
lst = [1, 2, 2, 20, 5, 1, 3]
if 20 in lst:
    ind = lst.index(20)
    lst[ind] = 200
print(*lst)
'''

'''
count1 = count2 = 0
s = 0
lst = [1, 2, 2, 6, 20, 1, 3]
for i in range(len(lst)):
    if lst[i] % 2 == 0:
        count2 += 1
        s += lst[i]
    else:
        count1 += 1

if count2 > count1:
    print('summa = ',s)
else:
    print('Нечетных чисел больше')
'''

'''
a = ['ee', 5, [1, 2], 2, 'r', 4, 'ee']
b = [4, 'we', 'ee', 3, [1, 2]]
c = []
for el in a:
    if el in b:
        if el not in c:
            c.append(el)
print(c)
'''

'''
a = [4, 6, 'py', 'tell', 78]
b = [44, 'hello', 56, 'exept', 3]
c = a + b
c.insert(3, 6)
i = 0
while i < len(c):
    if isinstance(c[i],str):
        del c[i]
    else:
        i += 1
print(*c)
'''

'''
s = 'hello world'
lst = s.split()
print(lst)
'''

n = int(input('Введите количество элементов списка: '))
lst = []
for i in range(n):
    x = int(input('Введите элемент списка: '))
    lst.append(x)
print(lst)