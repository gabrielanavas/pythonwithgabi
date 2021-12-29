#Chapter 9- Dictionaries
#List- a linear collection of values that stay in order
#Dictionary- a "bag" of values, each with its own label

#key -value pairs

#Dictionaries are like lists except that they use keys instead of number to look up values

while True:
    print("Menu \n1. Dictionary \n2. Update Variables \n3. Histogram Problem \n4. New Entry \n5. Get Method \n6. Simplified Counting  \n7. Counting Patterns \n8. Definite loops \n9. Two iteration variables")
    option = input(">> ")

    if option == "1":
    #Dictionary
        purse = dict()
        purse["money"]=12
        purse["candy"]=3
        purse["tissue"]=75
        purse["Lipstick"]=5
        print(purse)
        print(purse["Lipstick"])


    elif option == "2":  
    #update variables
        purse = dict()
        purse["money"]=12
        purse["candy"]=3
        purse["tissue"]=75
        purse["Lipstick"]=5
        print(purse)
        print(purse["Lipstick"])
        purse["candy"]= purse["candy"]+2
        print(purse)

    elif option == "3":
    #most common word or histogram problem
        #counters with a dictionary
        ccc= dict()
        ccc["hunter"] = 1
        ccc["snoopy"]=1
        print(ccc)

        ccc["snoopy"]=ccc["snoopy"]+1
        print(ccc)

    elif option == "4":
    #new entry
        counts= dict()
        names=["snoopy","hunter","snoopy","lobo", "hunter"]
        for name in names:
            if name not in counts:
                counts[name]=1
            else:
                counts[name]= counts[name]+1
        print(counts)
    
    elif option =="5":
    #Get Method for Dictionaries
        counts= dict()
        names=["snoopy","hunter","snoopy","lobo", "hunter"]
        for name in names:
            if name in counts:
                x=counts[name]
            else:
                x=0

        x=counts.get(name,0)
        print(x)

    elif option =="6":
    #Simplified counting with get()
        counts= dict()
        names=["snoopy","hunter","snoopy","lobo", "hunter"]
        for name in names:
            counts[name]= counts.get(name,0)+1
        print(counts)

    elif option =="7":
    #Counting Patterns

        counts= dict()
        print("Enter a line of text:")
        line = input("")
    #The general pattern to count the words in a line of text is to split the line into words, then loop through the words and use a dictionary to track the count of each independently.
        words= line.split()
        print("Words:",words)
        print("Counting...")
        for word in words:
            counts[word]=counts.get(word,0)+1
        print("Counts",counts)

    elif option =="8":
    #Definite loops and dictionaries
        counts= {"chuck":1,"fred":42,"jan":100}
        for key in counts:
            print(key, counts[key])
        
    elif option =="9":
    #Two iteration variables
        jjj= {"chuck":1, "zambos":50, "jan":85}
        for aaa,bbb in jjj.items():
            print(aaa,bbb)


    else:
        break
        print("amo")

stuff = dict()
print(stuff['candy'])





