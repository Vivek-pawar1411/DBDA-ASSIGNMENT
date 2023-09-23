#Accept 10 integers from user  and print their average value on the screen
avg=0
sum=0
for i in range(10):
    a=int(input("Enter the number"))
    sum+=a
    avg=sum/10
print(avg)

#To display the cube of the number upto given an integer. If the given integer is 5, then display cube of 1 to 4. 
cube=0
for i in range (1,6):
    cube=i*i*i
    print(cube)
    
#Accept 20 numbers from user and display sum of only even numbers. 
sum=0
even=0
for i in range(1,40):
    if(i%2==0):
        sum+=i
print(sum)

#Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.


c=input("Enter a number ( Press q to quit)")
while (c != 'q') and (c!='Q'):
    print(c)
    c=input("Enter a number ( Press q to quit)")
print("Outside")

#Given a number count the total number of digits in a number and also find sum of digits of the number.

n=(input("Enter the number "))
n_str=str(n)
print(len(n_str))
for i in n_str:
    d=int(i)

#Take a number from user and check if it is prime or not
no=int(input("Enter the num"))
for num in range(2,no):
    if no % num ==0:
        print("Not prime")
        break
else:
    print("Prime")

#Take a number from user and print sum of all odd numbers till that number.
sum=0
n=int(input("Enter the num"))
for i in range(2,n):
    if(i%2==1):
        sum+=i
print(sum)

"""Write a program in python to find the sum of the series [ x - x^3 + x^5 –x^7+x^9-x^11+ ......]. Go to the editor 
Test Data : 
Input the value of x :2 Input number of terms : 5 Expected Output : 
The values of the series:
2 
-8 
32 
-128 
512 
The sum = 410 
""" 



import math
z=0
n=int(input("Enter the num"))
for i in range(1,11,2):
   z=pow(n,i)
   print(z)


"""Write a program in python to display the sum of the series [ 1+x+x^2/2!+x^3/3!+....]. Go to the editor 
Test Data : 
Input the value of x :3 Input number of terms : 5 Expected Output : 
The sum is : 16.375000 """

import math
sum=0
n=int(input("Enter the number"))
r=int(input("Enter the range"))

for i in range(r):
        A =n**i/math.factorial(i)
        sum=sum+A
print(sum)


#pattern print 
"""" *
     * *
     * * *
     * * * *
     * * * * *
     """
     
for i in range (1,5):
    print('*'*i)
    
    """1010101          
        10101  
         101   
          1 """
n=int(input("enter no. "))
sp=0

for i in range(n-1,-1,-1):
    print(" "*sp,"1","01"*i,sep='')
    sp=sp+1