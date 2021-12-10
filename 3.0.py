hrs = input("Enter Hours:")
h = float(hrs)
rate = input ("Enter Rate:")
r = float(rate)

if h > 40 :
    reg = (40*r)
    otp = (h-40)*(r*1.5)
    pay= reg + otp
    
else:
    pay = (h*r)
    
print (pay)

#Con la ayuda de Sarah Gabriela
