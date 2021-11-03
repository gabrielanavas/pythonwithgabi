# to get the length of a string, use the len()function
a= "Hello Gabriela"
print(len(a))

# to check if a certain prhase is present in a string
txt ="The best things in life are free"
print("free"in txt)
print()

txt = "The best things in life are free"
if "free" in txt:
    print("Yes, 'free' is present.")
    print()

# to check if it isn't in the string
txt="The best things in life are free"
print("expensive"not in txt)
print()
txt =" The best things in life are free"
if "expensive" not in txt:
    print("No, 'expensive' is Not present")

#returning a range of characters by using slice syntax

g="Hello Gabriela"
print(g[2:13])

#slice from the start