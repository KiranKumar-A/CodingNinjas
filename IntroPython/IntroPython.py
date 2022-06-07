#%%
from re import I


a = input()
b = input ()
s = a + b
print(s)
# %%
# Write your code here
o = int(input())

while o != 6:
    if o <= 5 and o >= 1:
        a = int(input())
        b = int(input())
    if o == 1:
        print(a + b)
    if o == 2:
        print(a - b)
    if o == 3:
        print(a * b)
    if o == 4:
        print(a // b)
    if o == 5:
        print(a % b)
    elif o < 1 or o > 6:
        print("Invalid Operation")
    
    o = int(input())
    
# %%
# Reverse a number
N = int(input())
Reverse = 0

while N > 0:
    Reminder = N % 10
    Reverse = (Reverse * 10) + Reminder
    N = N // 10
print(Reverse)




# %%
# Check Palindromic number:
def checkPalindrome(num):
    #Implement Your Code Here
    Reverse = 0
    Reminder = 0
    while num > 0:
        Reminder = num % 10
        Reverse = (Reverse * 10) + Reminder
        num = num // 10
        if Reverse == num:
            True
    return Reverse
		
num = int(input())
Reverse = checkPalindrome(num)
if(num == Reverse):
	print('true')
else:
	print('false')


# %%
N = int(input())
Reminder = N % 10
print(Reminder)
Reverse = (Reverse * 10) + Reminder
print(Reverse)
N = N // 10
print(N)


# %%
# Sum of even and odd numbers of N
print("Sum of even", "  ", "Sum of odd"),
N = int(input())

even_sum = 0
odd_sum = 0

while(N > 0):
    d = N % 10
    if d % 2 == 0:
        even_sum += d
    else:
        odd_sum += d
    N = N // 10
print(even_sum, odd_sum)


# %%
#Nth Fibonacci number
Number = int(input())
i = 0
First_Value = 1
Second_Value = 1
            
# Find & Displaying Fibonacci series
while(i < Number):
           if(i <= 1):
                      Next = i
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           
           i = i + 1
print(Next)
 
# This code is contributed by Saket Modi
# %%
n = int(input())

a = 0
b = 1

c = -1

for i in range(n):
    c = a + b
    a = b
    b = c
    
print(a)


# %%
