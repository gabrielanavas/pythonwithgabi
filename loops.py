#Python has two primitive loop commands while and for

#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
    print(x)
    print()
for x in range(0,3):
     print(x)

for x in ['A','B','C']:

  print(x+'A')
  print()

for i,x in enumerate(['A','B','C']):
    print(i,x)
    print()

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'weight'
    print("After square ", i, 'is',  squares[i])
    print()

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)


#Break Statement
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple","banana","cherry"]
for x in fruits:
    if x =="banana":
        break
    print()
    print(x)
    print()

#continue statement
fruits = ["apple", "banana","cherry"]
for x in fruits:
    if x =="banana":
        continue
    print(x)
    print()

cars = ["mazda","toyota","bmw"]
for x in cars:
    if x == "toyota":
        print(x)

#While
# if it is less than  6 exit the loop
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 1
Rating = PlayListRatings[0]
while(Rating >=6):
    print(Rating)
    Rating = PlayListRatings[i]
    i = i+1

    A=[1,2,3]



for i in range(1,5):
    if (i==2):
        print(i)