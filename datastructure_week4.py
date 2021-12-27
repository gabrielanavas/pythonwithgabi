#Programming
#Algorithms: A set of rules or steps used to solve a problem
#Data Structures: a particular way of organizainf data in a computer



#lists are surroundend by square brackets, can be any python objects
friends= ["Sarah", "Jenn", "Lorri", "Andrea", " Astrid"]
print(friends[1])

#lists a re mutable, meaning we can change 

#The range function returns a list of numbers that range from zero to one less than the parameter

print(range(4))

friends= ["Sarah", "Jenn", "Lorri", "Andrea", " Astrid"]
print(len(friends))
print(range(len(friends)))

#concatenating list using +
a= [1,2,3]
b=[4,5,6]
c= a+b
print(c)

#Slicing lists
t= [9,41,12,3,74,15]
t[1:3]


#building lists from scratch 
#The list stays in order and new elements are added at the end of the list
stuff= list()
stuff.append("BOOK")
stuff.append("99")
print(stuff)
stuff.append("cookie")
print(stuff)

#Something in a list 
some =[1,9,21,10,16]

print (9 in some)
print(4 in some)
print (13 not in some)

# Lista are in order 
friends =["Jenn", "Sarah", "Mayra", "Johnnie", "Mary", "Andrea"]
friends.sort()
print(friends)


nums= [3,41,25,5,21]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

#strings and lists
abc= "With three words"
stuff= abc.split()
print(stuff)


#The double split pattern
word =("From stephen.marquad@uct.ac.za Sat Jan 5 09:14:16 2008")
words= word.split()
print(words)
email= words[1]
print(email)
pieces = email.split("@")
print(pieces)

x = list(range(5))
print(x)

fruit = 'Banana'
fruit[0] = 'b'
print(fruit)
