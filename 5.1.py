#practice
num = 0
total = 0.0
while True :
    val = input ("Enter a number: ")
    if val == "done" :
        break
    try: 
        fval = float(val)
    except: 
        print ("Invalid Input")
        continue
    print(val)
    num = num +1
    total = total + fval

print ("All done")
print (total, num, total/num)