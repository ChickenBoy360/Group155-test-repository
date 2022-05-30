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