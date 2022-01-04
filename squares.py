#list comprehension to generate list of values
x =[ i for i in range(10,21)]

#counter for the output print statement
counter = 1

#empty list for output values 
x_out =[]

while len(x)>0:
    x_out.append(x[0]**2) # add value to the new list
    print(f"The square of entry {counter} of x is {x[0]**2}")
    counter += 1 #update counter

    x.pop(0) #removes the value once processed

    if len (x)== 0: # loop is complete
        print("The loop is complete and the list is available.")

x_out        