'''
for i in range(1, 5):
    for j in range(1, 5):
        print(f'i={i} j={j}')
'''

'''
for i in range(1, 4):
    for j in range(1, 4):
        print(i, end=' ')
    print()
'''


for i in range(1, 4):
    for j in range(1, i + 1):
        print(i, end=' ')
    print()


# проверить простое ли число
'''
number = int(input('Enter number: '))
count = 0
for i in range(2, number // 2 + 1):
    if number % i == 0:
        count += 1
        print(i)
        break
if count == 0:
    print('простое')
else:
    print('составное')
'''

# Вывести все простые числа от 2 до 100
'''
for j in range(2, 100):
    count = 0
    for i in range(2, j // 2 + 1):
        if j % i == 0:
            count += 1
            break
    if count == 0:
        print(j, end=' ')
'''

'''
j = 2
while j <= 100:
    count = 0
    for i in range(2, j // 2 + 1):
        if j % i == 0:
            count += 1
            break
    if count == 0:
        print(j, end=' ')
    j += 1
'''

s = 'hello world'
# for elem in s:
#    print(elem)

# for i in range(len(s)):
#    print(s[i])

# i = 0
# while i < len(s):
#    print(s[i])
#    i += 1


# Задача с коровами

'''
n = int(input('Введите количество коров: '))
for i in range(1, n + 1):
    if i % 10 == 1 and i % 100 != 11:
        print(f'На лугу {i} корова')
    elif i % 10 == 2 and i % 100 != 12 or i % i % 10 == 3 and i % 100 != 13 or i % 10 == 4 and i % 100 != 14:
        print(f'На лугу {i} коровы')
    else:
        print(f'На лугу {i} коров')
'''

'''
# задача с фибаначи
# 1 1 2 3 5 8 13 21 34 55 89

num1 = num2 = 1
# num1: 1 1 2 3 5
# num2: 1 2 3 5 8
n = int(input('Введите количество чисел: '))
if n == 1:
    print(num1)
elif n == 2:
    print(num1, num2)
else:
    print(num1, num2, end=' ')
    for i in range(3, n + 1):
        num2, num1 = num1 + num2, num2
        print(num2, end=' ')
'''