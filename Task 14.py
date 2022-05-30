'''
a = [[1, 2, 4], [5, 2, 5], [1, 5, 2]]
print(a)
print(a[0][0])
for i in range(len(a)):
    for j in range(len(a[i])):
        print(f'[a{i}][{j}]={a[i][j]}', end=' ')
    print()
'''

'''
a = []
for i in range(3):
    lst = []
    for j in range(3):
        x = int(input())
        lst.append(x)
    a.append(lst)
print(a)
'''

'''
a = []
for i in range(3):
    a.append([int(input()) for j in range(3)])
print(a)
'''

'''
a = [[int(input()) for i in range(3)] for j in range(3)]
print(a)
'''

'''
b = [[0] * 3 for i in range(3)]
print(b)
for i in range(len(b)):
    for j in range(len(b[i])):
        if i == j:
            b[i][j] = i
        elif i > j:
            b[i][j] = 3
print(b)
'''

'''
a = [[i + 1 for i in range(4)] for j in range(4)]
print(a)
b = [[i * j for i in range(4)] for j in range(4)]
print(b)
for i in range(len(b)):
    s = 0
    for j in range(len(b[i])):
        s += b[i][j]
    print(s)
'''

'''
import random

a = [[random.randint(-100, 100) for i in range(3)] for j in range(3)]
print(a)
min_el = max_el = a[0][0]
imin = jmin = imax = jmax = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
        if min_el > a[i][j]:
            min_el = a[i][j]
            imin = i
            jmin = j
        if max_el < a[i][j]:
            max_el = a[i][j]
            imax = i
            jmax = j
    print()
print(max_el, min_el)
a[imin][jmin], a[imax][jmax] = a[imax][jmax], a[imin][jmin]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
'''

import random

n = int(input())
numb = random.randint(1, n)
main_set = {i for i in range(1, n + 1)}
print(numb)
while True:
    print(*main_set)
    print('Enter guess:', end=' ')
    set1 = {int(i) for i in input().split()}
    if numb in set1:
        print('YES:', end=' ')
        main_set = set1
    else:
        print('NO:', end=' ')
        main_set = main_set - set1

    if (len(set1) == 1 and numb in set1) or len(main_set) == 1:
        print(f'YES  {numb}is correct. You answered on the try')
    count += 1
