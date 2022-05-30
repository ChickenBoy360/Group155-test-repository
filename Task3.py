''' улитка
h, up, down = map(int, input().split())
diff = h - up
day = up - down
days = (diff - 1) // day +2
print(days)
'''

s = 'hello eagle'
print(s.count('e', 3, len(s)))
print(s.replace('e', 'p'))
print(s.capitalize())
print(s.title())
print(s.find('e'))
print(s.rfind('e'))
print(s.index('e'))
print(s.rindex('e'))
print(s.lower())
print(s.islower())
print(s.upper())
print(s.isupper())
