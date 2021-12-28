#Exercise 2
name = input("What is your name?")
print("Hello", name)

#Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay
hour =input("Enter Hours:")
rate =input("Enter rate:")

hours= float(hour)
rates=float(rate)

pay = (hours*rates)
print(pay)

#Exercise 4 write the value and type of the expression 
width =17
height = 12.0

test1= (width//2)
print(test1)

test2 =(width/2.0)
print(test2)

test3= (height/3)
print(test3)

test4= (1+2*5)
print(test4)

#Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

celsius= int(input("Enter the temperature in Celsius:"))
fahren = (celsius *9/5)+32
print(fahren)


