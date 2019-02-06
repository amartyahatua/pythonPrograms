a = [5, 1, 4, 3]
a.sort()
print(a)

strs = ['aa', 'BB', 'zz', 'CC']

strs.sort()
print(strs)
strs.sort(reverse=True)

print(strs)

strs = ['ccc', 'aaaa', 'd', 'bb']
sorted(strs,key=len)

print(strs)

sorted(strs,key=str.lower)
print(strs)

strs = ['xc', 'zb', 'yd' ,'wa']

def MyFn(s):
    return s[-1]

print(sorted(strs,key=MyFn))

##Tuple

tuple = (1,2,'hi')
tuple = (1,2,'bye')

nums = [1,2,3,4]
squares = [n*n for n in nums]
print(squares)

strs = ['hello', 'and', 'goodbye']
shouting = [ s.upper() + '!!!' for s in strs ]
print(shouting)

nums = [2, 8, 1, 6]
small = [ n for n in nums if n <= 2 ]

print(small)


small = [n for n in nums if n <=2]
