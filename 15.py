mylist = [9,3,6,1,5,0,8,2,4,7]
list_b = [6,4,6,1,2,2]
res=[]
for j in list_b:
    for i in mylist:
        if (i==j):
            res.append((j,mylist.index(i)))

print(res)
print([(i,mylist.index(i))for i in list_b])
#for i in list_b:
m=dict(res)
print(m)
result={}
for i in list_b:#dictionary comprehension
    result[i]=mylist.index(i)
print(result)
print({i:mylist.index(i)for i in list_b})