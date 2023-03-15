def check_double(number):
    num1=str(number*2)
    number=str(number)
    count=0
    for x in number:
        if x in num1:
            count+=1
        else:
            return False
    if count==len(number):
        return True
print(check_double(245))
print(check_double(125874))

n=input()
n2=(int(n)*2)
n3=" ".join(sorted(str(n)))
n4=" ".join(sorted(str(n2)))
print(n3)
print(n4)
if len(str(n))==len(str(n2)) and n3==n4:
    print(True)
else:
    print(False)


num=input("ENTER THE NUMBER:")
num1=(int(num)*2)
num2=[int(x) for x in str(num)]
num3=[int(x) for x in str(num1)]
sort1=sorted(num2)
sort2=sorted(num3)
if len(str(num))==len(str(num1)) and sort1==sorted:
    print(True)
else:
    print(False)


