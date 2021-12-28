#Loops (repeated steps)have iteration variables thta change each time through a loop
n= 5
while n > 0:
    print (n)
    n= n-1
print ("Blastoff!")
print (n)


#Break statement ends the current loop and jumps to the statement immediately followig the loop
#Continue statement ends the current iteration and jumps to the top of the loop and stats the nex iteration

for i in [ 5, 4, 3,2,1]:
    print (i)
print("Blastoff!")

friends = ["Michael", "Dwight", "Pam", "Jim"]
for friend in friends :
    print("Happy New Year", friend)
print ("Done")

#Looping through a set

print ("Before")
for thing in [9, 41,12,3,74,15] :
    print(thing)
print ("After")

# Finding the largest Value 
largest_so_far = -1
print ("Before", largest_so_far)
for the_num in [9,41,12,3,74,15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
print("After", largest_so_far)

# counting in a loop
zork = 0
print("Before", zork)
for thing in [9,41,12,3,74,15] :
    zork = zork + 1
    print (zork, thing)
print("After", zork)


# Summing in a Loop
zork = 0
print("Before", zork)
for thing in [9,41,12,3,74,15] :
    zork = zork + thing
    print (zork, thing)
print("After", zork)

#Finding the average in loop
count = 0
sum = 0
print ("Before", count, sum)
for value in [9,41,12,3,74,15]:
    count = count + 1
    sum= sum + value
    print (count, sum, value)
print("after", count, sum, sum/count)


#Filtering in a Loop 
print  ("Before")
for value in [9,41,12,3,74,15]:
    if value > 20:
        print ("Large number", value)
print("After")

#Search using a boolean variable 
found = False
print ("Before", found)
for value in [9,41,12,3,74,15]:
    if value == 3:
        found = True
    print(found, value)
print ("After", found)


# How to find the Smallest Value
smallest_so_far = None
print ("Before", smallest_so_far)
for value in [9, 41, 12, 3, 74,15] :
    if smallest_so_far is None :
        smallest_so_far = value
    elif value < smallest_so_far :
        smallest_so_far = value    
    print(smallest_so_far, value)
print ("After", smallest_so_far)


