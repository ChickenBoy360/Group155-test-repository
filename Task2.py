s = 'hje@poe'
ind = s.find('@')
print(ind)
s2 = s[ind+1:] + s[ind] + s[:ind]
print(s2)