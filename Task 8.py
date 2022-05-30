'''
Task 1
n = int(input('Enter number: '))
numbers = [n // 1000000, (n // 100000) % 10, (n // 10000) % 10, (n // 1000) % 10, (n // 100) % 10, (n // 10) % 10,
           n % 10]
chet = 0
nechet = 0

for number in numbers:
    if number % 2 == 0:
        chet += 1
    else:
        nechet += 1

if chet > nechet:
    print(sum(numbers))
else:
    print(numbers[0] * numbers[2] * numbers[5])
'''

'''
Task 4
import random

n = int(input("Сколько будет чисел? "))
d = int(input("Какую цифру считать? "))
count = 0
for i in range(1, n + 1):
    m = random.randint(1, 100)
    print(m, end=' ')
    while m > 0:
        if m % 10 == d:
            count += 1
        m = m // 10
print()
print("Было введено %d цифр %d" % (count, d))
'''

'''
Task 5
s = input('Введите строку: ')
l = len(s)
integ = []
i = 0
while i < l:
    s_int = ''
    a = s[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < l:
            a = s[i]
        else:
            break
    i += 1
    if s_int != '':
        integ.append(int(s_int))
print(integ)
'''

'''
Task 6
text = 'HjkzLM'
pair_lower = 0
pair_upper = 0
for i in range(1, len(text)):
    if text[i - 1].islower() and text[i].islower():
        pair_lower += 1
    if text[i - 1].isupper() and text[i].isupper():
        pair_upper += 1
print('Cколько пар (стоят рядом) верхнего регистра:', pair_upper)
print('Cколько пар (стоят рядом) нижнего регистра:', pair_lower)
'''

'''
Task 2
n = input("enter text: ")
gl='aeiyou'
count = 0
sogl = 0
s = " "
for i in n:
    if i in gl:
        count+=1
        s+=i
    elif i not in gl and not i == " ":
        sogl+=1
if count == sogl:
    print(s)
'''

import random

s = random.randint(1, 20)
s1 = random.randint(1, 20)
a = int(input('Введите число от 1 до 20: '))
a1 = int(input('Введите число от 1 до 20: '))
count = 0
f
if s < a and s1 < a1:
    count += 1
    print(count)
