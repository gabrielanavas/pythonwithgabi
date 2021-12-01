# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence: 0.8475"
a=text.find('0.8475')
print(float(text[a:]))


#Worked Exercise
str = "X-DSPAM-Confidence: 0.8475"

ipos =str.find(":")
print(ipos)
piece=str[ipos+2:]
print(piece)
value=float(piece)
print(value)