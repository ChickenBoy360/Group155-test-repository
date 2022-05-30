'''
number = 1
while number <= 10:
    print(number)
    number += 1
'''

# все 3-ч значные числа сумма цифр которых равна 10-ти
'''
number = 100
while number <= 999:
    s = number // 100 + number % 10 + number // 10 % 10
    if s == 10:
        print(number, end=' ')
    number += 1
'''

# найти сумму 5-ти чисел введеных с клавиатуры с помощью while
'''
count = 1
s = 0
while count <= 5:
    number = int(input('Enter number: '))
    s += number
    count += 1
print(s)
'''
# посчитать сумму чисел пока не введем число 0
'''
number = int(input('Enter number: '))
s = 0
while number != 0:
    s += number
    number = int(input('Enter number: '))
print('s =', s)
'''
# посчитать сумму чисел пока не введем число 0, используя бесконечный цикл
'''
s = 0
while True:
    number = int(input('Enter number: '))
    if number % 5 == 0 and number != 0:
        continue
    if number == 0:
        print(s)
        break
    s += number
'''

'''
number = int(input('Enter number: '))
s = 0
while number != 0:
    s += number
    number = int(input('Enter number: '))
    if number == 5:
        break
else:
    print('Цикл не был прерван')
print('s =', s)
'''

# Сложить все цифры n - значного числа
'''
number = int(input('Enter number: '))
s = 0
while number != 0:
    s += number % 10
    number = number // 10
    print(number)
print(s)
'''

# Найти количество цифр 5 в n-значном числе
'''
number = int(input('Enter number: '))
count = 0
while number != 0:
    if number % 10 == 5:
        count += 1
    number = number // 10  # number //= 10
print(count)
'''

# Вывести все делители числа 12: 1 2 3 4 6 12
'''
number = int(input('Enter number: '))
i = 1
count = 0
while i <= number:
    if number % i == 0:
        count += 1
        print(i, end=' ')
    i += 1
print('count =', count)
if count == 2:
    print('Число простое')
'''

# Дано 2 числа, вывести их общие делители
'''
number1, number2 = map(int, input().split())
i = 1
while i <= number1 and i <= number2:
    if number1 % i == 0 and number2 % i == 0:
        print(i, end=' ')
    i += 1
'''

# Найди нод числа через алгоритм Евклида
'''
number1, number2 = map(int, input().split())
while number1 != 0 and number2 != 0:
    if number1 > number2:
        number1 = number1 % number2
    else:
        number2 = number2 % number1
nod = number1 + number2
print('nod =',nod)
'''

