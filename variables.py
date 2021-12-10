#casting is used to specify the data type 
x= str(5)
y = int(5)
z = float(5)
print(x)
print(y)
print(z)
print()

#Use the function typw to get the data type
x= 5
y= "John"

print(type(x))
print(type(y))
print()

#many values in one line
x,y,z = "Orange","Banana","Cherry"
print(x)
print(y)
print(z)
print()

#unpack a collection of values in a list, tuple
fruits =["apple", "banana", "cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)
print()

#You can combine text and variable using + character 
# nevertheless you can't combine a number and a string
x= "smart"
print("Gabriela is "+ x)
print()

x= 5
y= 10
print(x+y)
print()

#Global Variables are the ones created outside of a function
x = "smart"

def myfunc():
    print("Gabriela is "+ x)
    print()
myfunc()


#create a variable with the same name inside a function and it will become local 


#to create  a gloabal variable inside a function we will use the keyword global
def myfun():
    global x
    x = "kind"
myfunc()
print("Gabriela is "+ x)

