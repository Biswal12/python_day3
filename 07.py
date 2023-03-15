str1=input("enter the sentences:")
d=len(str1)
if d<2:
    print("-1")
elif d==2:
    print(str1*2)
else:
    print(str1[0:2],end="")
    print(str1[-2:len(str1)])
## l=str1[0:2]

# l1=str1[-2: len(str1)]

# l2=str(1) + str(11)
