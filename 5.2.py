largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        num = float(num)
    except:
        print ("Invalid input")
        continue
    print (num)

    if smallest is None:
        smallest = num
        largest = num
    if num > largest :
        largest = num
        
    elif num < smallest:
        smallest = num
   
print("Maximum", largest)
print("Minimum", smallest)