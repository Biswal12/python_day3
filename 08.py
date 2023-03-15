str1=input("enter any word:")
d=str1[-3:len(str1)]
l=len(str1)
if d=="ing":
    print(str1+"ly")
   # print(str1.replace("ing","ly")) it will replace the "ing" with "ly"
elif l<3:
    print(str1)
else:
    print(str1+"ing")

