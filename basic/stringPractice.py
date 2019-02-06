astring = "Hello world!"
print(astring)

## Length
length = len(astring)
print(length)

## Find index
ind = astring.index("o")
print(ind)

## Count number of time an alphabet appears
num = astring.count("l")
print(num)

##Substring
substr = astring[3:7]
print(substr)
substr = astring[3:7:2]
print(substr)

##String reverse
strrev = astring[::-1]
print(strrev)

##Upper and Lower case

upercase = astring.upper()
lowercase = astring.lower()
print(upercase)
print(lowercase)

##Starts with and ends with
stars = astring.startswith("Hello")
print(stars)
ends = astring.endswith("rld!")
print(ends)

##Spliting words

tokens = astring.split(" ")
print(tokens)

##Practice
s = "Hey there! what should this string be?"
print(len(s))

##Find first occurance of 'a"
firsta = s.index("a")
print(firsta)

counta = s.count("t")
print(counta)

##Substrings
substr = s[:5]
print(substr)
substr = s[5:10]
print(substr)

##Characters with odd indices

oddindi = s[1::2]
print(oddindi)

##Get last n characters

lastchars = s[-5:]
print(lastchars)

#Concatenation

str1 = "Hello"
str2 = "World"

print((str1+str2))
print(str1*3)


#Replace

before = "here."
after = before.replace(".", "")
print(after)

#Strip

testString = "I am in Hattiesburg"
striptString = testString.strip()
print(striptString)

alpha = "a"
digi = "3"
space = " "
isAlpha = alpha.isalnum()
isDigit = digi.isdigit()
isSpace = space.isspace()

print(isAlpha)
print(isDigit)
print(isSpace)

find = testString.find('Hattiesburg')
print(find)

stringHello = "Hello"
print(stringHello[1:4])
print(stringHello[-4:])
print(stringHello[:-3])

