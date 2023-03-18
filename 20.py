import sys
def Next_smallest_palindrome(num):
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
print(Next_smallest_palindrome(99))
print(Next_smallest_palindrome(1221))

