# n=int(input("enter the number:"))
# if(n%3)==0 and (n%5)==0:
#     print("multiple of 3 and 5")
# elif(n%3)==0:
#     print("multiple of 3 ")
# elif(n%5)==0:
#     print("multiple of 5")
# else:
#     print("invalid")
# FUNCTIONS
# def function1():
#     print("its a function1")
# function1()
# def function2(num1,num2) :
#     print("num1=",num1,"num2=",num2)
#     #print()_str_
# function2(10,20)
# def function2(num1,num2) :
#      num3= num1+num2
#      return num3
#     #print()_str_
# print("value returned",function2(100,200))
# def function2(num1,num2) :
#      num3= num1+num2
#      return num3
#     #print()_str_
# print("value returned",function2(10,20.2))
# def function2(num1,num2) :
#      num3= float(num1)+num2
#      return num3
#     #print()_str_
# print("value returned",function2('10',20.2))
# categories of functions
# based on arguments
# 1 :positional arguments
# def function1(num1,num2,num3,num4):
#     print("num",num1,"num2", num2,"num3", num3, "num4",num4)
# function1(10,20,30,40)
# function1(100,'200',300,400)
# KEYWORDS ARGUMENTS
# def function2(num1,num2,num3,num4):
#     print("num",num1,"num2", num2,"num3", num3, "num4",num4)
# function2(num4=10,num1=20,num2=30,num3=40)
# function2(num4=10,num1=10,num2=30,num3=30)
# data is send to right to left...across any language.
# DEFAULT ARGUMENTS
# def functions ( name ,rollno ,branch="cse",collegename='GIET',):
#     print(name,rollno,branch,collegename)
# functions("basudev",11,)
# functions("basu123",12,)
# functions("basu",13,'ECE')
# VARIABLE NO. FO ARGUMENTS
def function4(*var):  # tuple==
    for i in var:
        print(i, end=' ')


function4(10, 20)
print()
function4(10, 20, 30, 40)
print()
function4(10, 20, 40, 50, 60, 70)
print()
function4(10, 20, 30, 40, 50, 60, 70, 80)
print()


def add(*var):  # tuple==
    sum1 = 0
    for i in var:
        sum1 = sum1 + i
        print(sum1)  # return sum1


add(10, 20)
print()
add(10, 20, 30, 40)
print()
add(10, 20, 40, 50, 60, 70)
print()
add(10, 20, 30, 40, 50, 60, 70, 80)
print()


#############
def add(*var):  # tuple==
    sum1 = 0
    for i in var:
        sum1 = sum1 + i
    return sum1


print(add(10, 20))
print(add(10, 20, 30, 40, 50))     