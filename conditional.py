#comparision programming 4 everybody 
x = 5
if x == 5 :
    print("Equals 5") 
if x > 4:
    print ("Greater than 4")
if x >= 5:
    print ("Greather than or equals 5")
if x < 6 : 
    print ("Less than 6") 
if x <= 5 :
    print("Less than or equals 5")
if x != 6 :
    print ("Not equal 6")


# One way decisions 
x= 5
print ("Before 5")
if x==5 :
    print ("Is 5")
    print ("Is still 5")
    print ("Third 5")
print ("Afterwards 5")
print ("Before 6")
if x == 6:
    print ("Is 6")
    print ("Is still 6")
    print ("Third 6")
print("Afterward 6")

#Think about begin/end of blocks with indentions
x =5
if x>2 :
    print ("Bigger than 2")
    print ("Still bigger")
print("Done with 2")

for i in range (5) :
    print (i)
    if i >2 :
        print ("Bigger than 2")
    print ("Done with i", i)
print("All done")

# Nested decisions 
x = 42 
if x > 1 :
    print ("More than one")
    if x < 100 :
        print("Less than 100")
print ("All done")

#Two way decisions with else
x = 4
if x > 2:
    print ("Bigger")
else  :
    print ("Smaller")
print("ALL DONE")