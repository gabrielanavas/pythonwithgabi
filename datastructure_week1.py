#Chapter 6

#remeber input number must be converted from strings
#Looking inside strings

fruit= "banana"
letter = fruit[1]
print(letter)

x= 3
w =fruit[x-1]
print(w)

x=len(fruit)
print(x)

#Looping through strings
fruit = "banana"
index = 0
while index < len(fruit):
    letter= fruit[index]
    print(index,letter)
    index= index +1

#A definite loop using a for statement is more elegant
fruit= "banana"
for letter in fruit:
    print(letter)

#Pro-Tip use the simplest bit of code to accomplish what you want./n It is easier to read, write, and debug a code. Also it is easier for others to understand.


#looping and counting
word= "telescope"
count = 0
for letter in word:
    if letter == "e" :
        count = count + 1
print(count)

#slicing strings

s= "Monty Python"
print (s[0:4]) #upto but not including 4 
print(s[6:7])
print(s[6:20])


#String Manipulation 
#using in as a logical operator
friend = "Sarah Gabriela"
"n" in friend
"m" in friend
"ah" in fruit
if "a" in fruit:
    print("Found it")

#string comparison 
if word == "banana" :
    print("All right, bananas")

if word < "banana":
    print("Your word,"+ word + ", comes before banana.") 
elif word > "banana" :
    print("Your word,"+ word +",comes after banana")
else:
    print("All right, banana")        

#Python has a number of string functions which are in the string library. These functions are built into
greet = "Hello Sarah"
zap =greet.lower()
print(zap)

stuff = "Hello There"
type(stuff)
dir(stuff) # The things it is capable of doing, methods in a class str
#look for that documentation 


#String Library -some examples
str.capitalize
str.center
str.find
str.replace
str.lower
str.upper

#You can make a copy if a string in lower case or upper case
#when we are searching for a string 

#searching a string
fruit= "banana"
pos= fruit.find("na")
print(pos)

# often to search a string using find we first convert the string to lowe case so we can search for a string regardless of case

#search and replace
greet= "Hello Charles"
nstr= greet.replace("Charles","Jane")
print(nstr)

nstr= greet.replace("C", "x")
print(nstr)


#stripping Whitespace
greet = "       Hola Sylvia       "
greet.lstrip()
print(greet)
greet.strip()
print()

#prefixes
line = "Please have a nice day"
line.startswith("Please")#true
print(line)
line.startswith("p")#false


#Parsing and extracting

data="From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find("@")
print(atpos)

sppos = data.find(" ", atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)

