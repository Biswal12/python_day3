list_of_marks=(12,18,25,24,2,5,18,20,20,21)
def find_more_then_average():
    marks=0
    count=0
    for x in list_of_marks:
        marks+=x
    average=marks/len(list_of_marks)
    for x in list_of_marks:
        if x>average:
            count+=1
    percentage=(count*100/len(list_of_marks))
    return percentage
def sort_marks():
    list_of_marks=sorted(list_of_marks)
    return list_of_marks
def generate_frequency():
    freq=[]
    for x  in range(26):
        count=0
        for y in list_of_marks:
            if x==y:
                count+=1
        freq.append(count)
    return freq
print(find_more_then_average())
print(list_of_marks)
print(generate_frequency())