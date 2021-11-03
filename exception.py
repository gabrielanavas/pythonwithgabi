a= 1
try:
    b = int(input("Please enter a number to divide a"))
    a= a/b
    print("Success a=", a)
except:
    print("There was an error")
#copy the output to introduce the number, paste it on the terminal 

#Example Except Specific
a=1
try:
    b=int(input("Please enter a number to divide a"))
    a= a/b
    print("Success a=", a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")

#Example Finally specific
a=1
try:
    b=int(input("Please enter a number to divide a"))
    a= a/b
    print("Success a=", a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("Success a=",a)
finally:
    print("Proccessing is complete")
