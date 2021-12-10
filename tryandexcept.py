#When the first conversion fails it just drops into the except clause and the program continues
astr = "Hello Bob"
try:
    istr = int(astr)
except:
    istr =-1
print ("First", istr)

astr = "1234"
try:
    istr = int(astr)
except:
    istr = -1
print ("Second", astr)


