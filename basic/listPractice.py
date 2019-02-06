colors = ['red', 'blue', 'green']

print(colors[0])
print(colors[1])
print(colors[2])

squares = [1,4,9,16]
sum = 0
for num in squares:
    sum = sum+num

print(sum)

list = ['lary', 'curly', 'moe']
if 'curly' in list:
    print('hello')

for i in range(10):
    print(i)
i = 0
while i < (10):
    print(i)
    i=i+1

##Append

list1 = [1,2,3,4]
list2 = [5,6,7,8]

list1.append(10)
list1.insert(2,100)
list1.extend(list2)
print(list1)

list1.remove(10)
print(list1)

list1.sort()
print(list1)

list1.reverse()
print(list1)

print(list1.pop())

