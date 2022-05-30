'''
Task2
lst1 = [1, 2, 3, 4, 8]
lst2 = [1, 2, 7, 9, 10]
m = None
for i in lst1:
    if i not in lst2:
        if  not m is None:
            if i < m:
                m = i
        else:
            m = i
print(m)
'''

'''
# 5
lst = [14, 5, 2, 188, 31, 10]
i = 0
while i < len(lst):
    if lst[i] % 2 == 0:
        s = str(lst[i])
        s = s[::-1]
        lst.insert(i + 1, int(s))
        i += 1
    i += 1
print(lst)
'''

'''
# 6
lst = [1, 2, 2, 5, 6, 7, 6, 7, 7]

for i in range(len(lst)):
    if i == lst.index(lst[i]):
        print(f'{lst[i]} - {lst.count(lst[i])}')
'''

'''
# 7
lst = [2, 5, -5, -7, 2, 1, 8, -1]
i = 0
l = len(lst)
while i < l:
    if lst[i] <= 0:
        lst.append(lst[i])
        del lst[i]
        i -= 1
        l -=1
    i += 1
print(lst)
'''

'''
# 9
lst = [1, 5, 6, 8, 9, 10, 2, 9, 1, 1]
for i in range(len(lst)):
    if i % 2 == 0 and lst[i] % 2 == 1:
        for j in range(i + 1, len(lst)):
            if lst[j] % 2 == 0:
                lst[i],lst[j]=lst[j], lst[i]
                break

    if i % 2 == 1 and lst[i] % 2 == 0:
        for j in range(i + 1, len(lst)):
            if lst[j] % 2 == 1:
                lst[i], lst[j] = lst[j], lst[i]
                break
print(lst)
'''

'''
# 10
lst = []
s = input()
while s != '.':
    s = s.split(maxsplit=1)
    if len(s) == 2:
        lst.append(s[1])
    elif s[0] == 'GET':
        print(lst[-1])
    elif s[0] == 'DELETE':
        del lst[-1]
    s = input()
'''

'''
lst = []
n = int(input())
for i in range(n):
    x = int(input())
    lst.append(x)
print(lst)    
'''

'''
import random

n = int(input())
print([i for i in range(1, n + 1)])
print([random.randint(1, 10) for i in range(1, n + 1)])
s = 'hello'
print([i for i in s])
print([int(i) for i in input().split()])
'''

'''
n = int(input())
print([i for i in range(1, n + 1) if i % 2 == 0])
print([i if i % 2 == 0 else 'hello' for i in range(1, n + 1)])
print([i**5 if i % 2 == 0 else i**0.5 for i in range(1, n + 1)])
'''


lst = [int(i) for i in input().split()]
lst.sort(key=abs)
print(lst)


'''
lst = [int(i) for i in input().split()]
lst.sort(key=lambda x: x % 10)
print(lst)
'''