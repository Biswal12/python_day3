n1= int(input("no.of 5 rupee coin:"))
n2= int(input("no.of 1 rupee coin:"))
n3= int(input("amount to be paid:"))
m=((n1*5)+(n2*1))
print(m)

if (m<=n3):
    t=(n3//n1)+(n3%n1)
    print(t)
else:
    print("-1")