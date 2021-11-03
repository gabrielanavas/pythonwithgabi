#Sets are a tupe of collection, they are unordered,  they have unique elements

#duplicate items will become one when created
Set1={"pop", "rock", "soul", "hard rock", "rock", "R&B","rock", "disco"}
print(Set1)

#Convert a list to a set using set casting 
album_list = ["Michael Jackson", "Thriller", "Thriller", 1982]
album_set = set(album_list)
print(album_set)

#set operations
set2={"Thriller", "Back in Black", "AC/DC"}
set2.add("NSYNC")
print(set2)
set2.remove("NSYNC")
print(set2)

"AC/DC" in set2

#Sets in mathematical set operations 

album_set_1 = { "AC/DC",}
