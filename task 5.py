'''
Task 1
n = int(input('Введите число: '))
for i in range(1, n+1):
    print(i, end=' ')
'''

'''
Task 2
s = 0
n = int(input('Введите число: '))
for i in range(0, n + 1):
    if i % 2 == 0:
        print(i, end=' ')
        s += i
print('Сумма всех четных чисел: ',s)
'''

number = int(input('Введите число: '))
s = 1
while number != 0:
    number = number // 10
    if number % 2 == 0:
        s *= number % 10
print(s)
