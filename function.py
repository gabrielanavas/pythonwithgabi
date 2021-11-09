#A function is created using the def keyword wirh is followed by optional parameters in paretheses

x = 5 
print ("Hello")
def print_lyrics():
    print ("I'm a lumberjack, and I'm okay")
    print (" I sleep all night and I worl all day.")
print ("Yo")
print_lyrics()
x=x + 2
print (x)

#Parameter is a variable which we use in the function definition 
def greet(lang) :
    if lang == "es" :
        return ("Hola")
    elif lang == "fr" :
        return ("Bonjour")
    else:
        return("Hello")
print(greet("en"),"Glenn")
print (greet("es"), "Sally")
print(greet("fr"), "Michael")
    
#Return Values, to return a value to be used as the valude of the funcion
def greet () :
    return "Hello"
print (greet(), "Glenn")
print(greet(), "Sally")
#Arguments, parameters and results

def thing() :
    print ("Hello")
print ("There")