# d = {
#    'Иванов Иван': [4, 1, 2, 5, 2],
#    'Петров Петр': [4, 6, 2, 6, 1],
#    'Сидоров Иван': [5, 1, 2, 3, 4]
# }
# lst = [2, 4, 5, 1, 51, 2, 1]
# f = open('test1.txt', 'a', encoding='utf-8')
# for i in range(3):
#    s = input('enter string: ')
#    f.write(s + '\n')
# f.write('Help me \n')
# f.write('Hello world')
# for el in lst:
#    f.write(str(el) + ' ')
# for key, value in d.items():
#    f.write(key + ':')
#    for el in value:
#        f.write(str(el) + ' ')
#    f.write('\n')
# f.close()
'''
try:
    f = open('test1.txt', 'r', encoding='utf-8')
    s = f.read()
    # repr - позволяет увидеть сырую строку
    # rstrip - убирает \n в конце
    s = s.replace('\n', ' ').rstrip()
    lst = s.split()
    #s = s[:-1]
    print(s)
    print(lst)
    f.close()
except FileNotFoundError:
    print('file not  found')
'''
# lst = []
# with open('test1.txt', 'r', encoding='utf - 8') as f:
# for line in f:
# lst.extend(line.rstrip().split())
# s = f.readline().rstrip().split()
# lst.extend(s)
# s = f.readline().rstrip().split()
# lst.extend(s)
# s = f.readline().rstrip().split()
# lst.extend(s)
# print(lst)
'''
d = {}
with open('test1.txt', 'r', encoding='utf-8') as f:
    for line in f:
        key = line.rstrip().split(': ')[0]
        value = line.rstrip().split(': ')[1].split(' ')
        value = list(map(int, value))
        d[key] = value
print(d)
'''
lst = []
with open('test1.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lst.append(line.rstrip().split())

p = []
for i in range(len(lst)):
    for j in range(len(lst[i])):
        p = list(lst[i][j])
        for k in range(len(p)):
            if p[k] == '0':
                p[k] = '1'
            elif p[k] == '1':
                p[k] = '0'
        lst[i][j] = ''.join(p)
        print(lst[i][j],end=' ')
    print()
with open ('test2.txt', 'w', encoding='utf-8') as f:
    for el in lst:
        s = ' '.join((el))
        f.write(s+'\n')