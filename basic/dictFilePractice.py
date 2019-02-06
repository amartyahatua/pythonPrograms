dict= {}

dict['a'] = 'alpha'
dict['b'] = 'beta'
dict['c'] = 'gamma'

print(dict)

if 'a' in dict:
    print("yes")
    print(dict['a'])

print(dict.get('c'))

print(dict.keys())

print(dict.values())

print(dict.items())

for k,v in dict.items():
    print(k,v)


f = open("foo.txt", 'rU')
for line in f:
    print(line)