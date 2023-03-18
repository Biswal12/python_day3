s1=input("enter the string 1")
s2=input("enter the string 2")
ans=""
for i in s1:
    if i==" ":
        continue
    for j in s2:
        if (i==j and j not in ans):
            ans+=i
print(ans)