'''
Task 1
lst = [2, 5, 4, 8, 10, 10, 4, 'ff', 'aa', 'aa']
for i in range(len(lst)):
    for j in range(len(lst)):
        if i != j and lst[i] == lst[j]:
            break
    else:
        print(lst[i], end=' ')
'''

'''
Task 2
a = [1, 1, 2, 2, 3, 4, 5, 6, 6]
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            counter += 1
print(counter)
'''

'''
Task 3 so so 
C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
if sum(C_1) > sum(C_2):
    print(f'Сумма больше в кортеже - C_1: {sum(C_1)}')
else:
    print(f'Сумма больше в кортеже - C_2: {sum(C_2)}')
'''

'''
Task 4
str1 = 'An apple a day keeps the doctor away'
str2 = str1.replace(' ', '')
my_dict = {i: str2.count(i) for i in str2}
print(my_dict)
'''

'''
Task 6
lst1 = set(map(int, input().split()))
lst2 = set(map(int, input().split()))
b = lst1 & lst2
print(len(b))
'''

'''
Task 7
my_dict = {"a": 1, "b": 2, "c": 3}
try:
    value = my_dict["d"]
except KeyError:
    print("A KeyError occurred!")
finally:
    print("The finally statement has executed!")
'''


with open('class.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    content = content.split("\n")
pupils = []
for line in content:
    line = line.split(" ")
    pupils.append([line[0], line[1], int(line[2])])
srednia = 0
print("Ниже 3 баллов:")
for p in pupils:
    srednia += int(p[2])
    if p[2] < 3:
        print(f"{p[0]} {p[1]}: {p[2]}")
        srednia /= len(pupils)
print(f"Средняя оценка по классу: {srednia}")