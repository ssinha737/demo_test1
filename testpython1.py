num=1
while (num<100):
    if  num%3==0 or num%5==0 :
        num =num+1
    else :     
        print('Number is :' , num)
        num=num+1


i = 0
a = 'geeksforgeeks'
  
while i < len(a):  
    if a[i] == 'e' or a[i] == 's':  
        i += 1
        break
    print('Current Letter :', a[i]) 
    i += 1



print((6%3)==0)

i=1

while i<=4:
    #print("Inside outer for loop") 
    j=1
    while(j<=5):
          print( '#',end="",sep= ' ' )
          j=j+1 
    

    i=i+1
    print()


# Write your code here
num = int(input())                  # Reading input from STDIN
str = input()
print(num*2)
print (str)



# Python program to check if
# given number is prime or not
 
#To take input from the user
num = int(input("Enter a number: "))
 
# If given number is greater than 1
if num > 1:
 
    # Iterate from 2 to n / 2
    for i in range(2, num):
 
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
 
else:
    print(num, "is not a prime number")



print ('*****************Assignment 2********************')

#This program is to print first 50 fibonacci series
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

#range(4) means 0 to 3


