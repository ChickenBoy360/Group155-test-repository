
'''
for i in range(1000, 0, -1):
    if i % 13 == 0 and i % 17 == 0:
        print(i, end=' ')
'''

'''
s = 0
for i in range(11):
    s += i
    # s = s + i
    print(s)
'''

'''
number = int(input())
count = 0
for i in range(1, number + 1):
    if number % i == 0:
        count += 1
if count == 2:
    print('Простое')
else:
    print('Составное')
'''

'''
s = 0 #сумма
for i in range(1, 6):
    number = int(input('Enter number: '))
    if number == 5:
        continue
    if number == 0:
        break
    print(i)
    s += number
print(s)
'''

'''
s = 0
for i in range(5):
    number = int(input('Введите оценку: '))
    s += number
print(s / 5)
'''

'''
for i in range(100, 1000, 1):
    if i % 111 == 0:
        print(i, end=' ')
'''

'''
s = 'hello'
# поэлементный вывод строки
for elem in s:
    print(elem)
# вывод строки по индексам
for i in range(len(s)):
    print(s[i], end=' ')
'''

'''
# вывести все буквы п за которыми идет буква а
s = input()
for i in range(len(s)-1):
    if s[i] == 'п' and s[i+1] == 'а':
        print(i, s[i])
'''

# Дана строка. Вывести все слова на новой строке
s = 'привет              я ваша                           тетя'
s += ' '
s1 = ''
for elem in s:
    if elem != ' ':
        s1 += elem
    elif s1:
        print(s1)
        s1 = ''
