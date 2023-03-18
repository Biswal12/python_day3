import  math
def hpprime(n):
    l=[]
    for i in range(2,n+1):
        flag=True
        for j in range(2,int(math.sqrt(i))+1):
            if(i%j==0):
                flag=False
                break
        if flag==True:
            l.append(i)
    for i in l:
        if n%i==0:
            large=i
    return large
n=int(input())
l=[]
for i in range(n,n+9):
    l.append(hpprime(i))
print(l)
print(sum(l))