p = int(input("principle loan amount:"))
R = int(input("rate of interest:"))
n = int(input("duration of loan:"))

r = R/(12*100)

emi = p*r*((1+r)**n)/((1+r)**n-1)
for i in range(1,n):
    p = p-emi
    print("your balance is:",p)