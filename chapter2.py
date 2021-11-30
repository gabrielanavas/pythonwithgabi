while True:
    print("\n\n PAGINA PRINCIPAL \n1. Name \n2. Gross Pay\n3. Type \n4. Celsius \n5.salir Seleccione una opcion")
    opcion = input(">> ")

    if opcion == "1":
    #Exercise 1
        name = input("What is your name?")
        print("Hello", name)
    elif opcion == "2":  
    #Exercise 2: Write a program to prompt the user for hours and rate per hour to compute gross pay
        hour =input("Enter Hours:")
        rate =input("Enter rate:")

        hours= float(hour)
        rates=float(rate)

        pay = (hours*rates)
        print(pay)

    elif opcion == "3":
    #Exercise 3 write the value and type of the expression 
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
    elif opcion == "4":
    #Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.
        celsius= int(input("Enter the temperature in Celsius:"))
        fahren = (celsius *9/5)+32
        print(fahren)



    else:
        break
        print("amo")







