#functions take some input to produce some output or change

def function(a):
    "add 1 to a"
    b= a+1
    print(a,"+1=",b)
    return b

#Len function
album_ratings= [10.0,8.5,9.5,7.0,7.0,9.5,9.0,9.5]
L= len(album_ratings)
print(L)
print()


#Sum function
album_ratings= [10.0,8.5,9.5,7.0,7.0,9.5,9.0,9.5]
S= sum(album_ratings)
print(S)
print()

#sorted vs sort
album_ratings = [10.0,8.5,9.5,7.0,7.0,9.5,9.0,9.5]
sorted_album_rating = sorted(album_ratings)
print(sorted_album_rating)

album_ratings = [10.0,8.5,9.5,7.0,7.0,9.5,9.0,9.5]
album_ratings.sort()
print(album_ratings)
print()

#Making Functions
def Mult(a,b):
    c=a*b
    return(c)
    print("This is not printed")
result = Mult(2,3)
print(result)

def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)

a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0 
else:
    c1 = 5
print(c1) 


#global variable

myband = "ac/dc"

def getbandrating(bandname):
    if bandname == myband:
        return 10.0
    else:
        return 0.0
print ("ac/dc's rating is:",getbandrating("ac/dc"))
print ("deep purple's rating is:", getbandrating("deep purple"))  
print("My favourite band is:",myband)  
print()

#collections and functions

def printAll(*args):
    print("No of arguments:",len(args))
    for argument in args:
        print(argument)
printAll ("Hoesefeather", "adonis","bone")
printAll("Sidecar",'Long Island',"Mudslide","Carriage")
print()

#collections and functions packed in a dictionary

def printDictionary(**args):
    for key in args:
        print(key + ":"+ args[key])
printDictionary(Country ="Canada", Province ="Ontario", City= "Toronto")
print()
#accept an return data types

def addItems(list):
    list.append("Three")
    list.append("Four")
myList = ["One", "Two"]

addItems(myList)
print(myList)


a= 1
def do(x):
    a=100
    return(x+a)
print(do(1))



