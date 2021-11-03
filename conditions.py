#Conditions and branching

age = (21)
if (age>18):
    print("you can enter 1")
print("move on")

#else statement
age = (21)
if (age>18):
    print("You can enter 2")
else:
    print("go see Meat Loaf")
print("Move on")

#elif statement
age =(18)
if (age>18):
    print("You can enter 3")
elif(age==18):
    print("Go see Pink Floyd")
else:
    print("Go see Meat Loaf")
print("Move on")

#Logical Operators OR
album_year =1990
if (album_year<1980) or (album_year>1989):
    print("The Album was made in the 70's or 90's")
else:
    print("The Album was made in the 1980's")

#Logical Operators AND
album_year = 1983
if(album_year>1979)and(album_year<1990):
    print("This album was made in the 80's")


# Condition statement example

album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")


#Quiz on Conditions
#Write an if statement to determine if an album had a rating greater than 8. 


rating = 8.5
if (rating>8):
    print("This album is amazing")