#get the name of the file and open it
name = input ("Enter file:")
handle = open(name, "r")

# count word frequency
counts = dict()
for line in handle :
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

#Find the most common word
bigcount = None
bigword = None 
for word,count in counts.items() :
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count

#Convert european floors
eup = input ("Europe Floor")
usf = int(eup) + 1
print ("US Floor", usf)       