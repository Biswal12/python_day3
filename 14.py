#list comprehension
# #for loop version
# result=[]
# for i in range(11):
#     result.append(i)
# print(result)
# #list comprehension version
# print([i for i in range (11)])
# #for loop version -->odd elements
# result=[]
# for i in range(11):
#     if i%2!=0:
#         result.append(i)
# print(result)
# print([i for i in range(11)if i%2!=0])
#
# result=[]
# for i in range(11):
#     if i%2!=0:
#         result.append(i)
#     else:
#         result.append(i**2)
# print(result)
# print([i if i%2!=0 else i**2 for i in range(11)if i%2!=0])
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
for i in mat:
     i_data=[]
     for j in i:
         if j%2!=0:
          i_data.append(j**2)
         else:
          i_data.append(j**3)
     result.append(i_data)
print(result)
#list comprehension
print([j**2 if  j%2!=0 else j**3 for i in mat for j in i ])
print([[j**2 if  j%2!=0 else j**3 for j in i] for i in mat ])
