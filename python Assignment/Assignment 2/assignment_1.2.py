""" 1.A student will not be allowed to sit in exam if his/her attendence is less than 75%.  
#Take following input from user Number of classes held Number of classes attended. And print percentage of class attended  
Is student is allowed to sit in exam or not."""

num=int(input("Enter the percentage of student"))
if(num>=75):
    print("Student sit in exam because he secured % ",num)
else:
    print("Student not sit in exam because he secured % ",num)

"""2. accept a from user and find the minimum number notes required to get the a a =512  
Notes: 2000,500,100,50,10,5,2,1  

500-1 note  
10  - 1 note  
2-  1 coin  

a=20550  
2000 – 10 note  
500 – 1 note  
50 -1 note """

a=int(input("Enter the number"))
note2000=a//2000
if(note2000>0):
    print("2000 = ",note2000)
rem=a%2000
note500=rem//500
if(note500>0):
    print("500 = ",note500)
rem=a%500
note200=rem//200
if(note200>0):
    print("200 = ",note200)
rem=a%200
note100=rem//100
if(note100>0):
    print("100 = ",note100)
rem=a%100
note10=rem//10
if(note10>0):
    print("10 = ",note10)
rem=a%10


#3. Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.
n=int(input("Enter the number"))
b=n%10
if(b%3==0):
    print("the num ",n,"is divisible by 3")
else:
    print("the num ",n,"is  not divisible by 3")
    
#4. Accept number from user and check whether it is divisible by 5 and 11 if divisible then display appropriate message.
n=int(input("Enter the number"))

if(n%5==0):
    print("the num ",n,"is divisible by 5")
elif(n%11==0):
    print("the num ",n,"is   divisible by 11")
else:
    print("the num is invalid")

#5. Modify the above question Q1 to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.  
A school has following rules for grading system:  
a.	Below 25 - F  
b.	25 to 45 - E  
c.	45 to 50 - D  
d.	50 to 60 - C  
e.	60 to 80 - B  
f.	Above 80 - A  
Ask user to enter marks and print the corresponding grade.  

mark=int(input("Enter the marks = "))
if(mark<=25):
    print("Sorry you are failed and get F grade")
elif(25>=mark and mark<=45):
    print("you passed and get D grade")
elif(45>=mark and mark<=50):
    print(" you are passed and get C grade")
elif(50>=mark and mark<=60):
    print(" you are passed and get D grade")
elif(60>=mark and mark<=80):
    print(" you are passed and get B grade")
elif(mark>=100):
    print(" you are passed and get A grade")
    
    
# 6.
x = 2
y = 5 
z = 0  
print(x == 2)  
print(x != 5)
print(x != 5 & y >= 5)  
print(z!= 0 | x == 2)
print(not(y < 10)) 
 
# 7.Write a program to check whether an years is leap year or not the year is leap if it satisfies following condition  
•	It the year is divisible by 100 o If it is divisible by 100, then it should also be divisible by 400 then it is leap year  
•	otherwise, all other years divisible by 4 and not divisible by 100 then it is leap year.   

year = int(input("Enter the year"))
if year%100==0:
    if year%400==0:
      print("year entered is leap year")
    else:
      print("year entered is leap year")
else:
    if year%4==0:
      print("year entered is leap year")
    else:
      print("year entered is leap year")


7.	Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :  
             Unit                                    Price    
First 100 units                                       no charge  
Next 100 units                                        Rs 5 per unit  
After 200 units                                       Rs 10 per unit  
(For example if input unit is 350 than total bill amount is Rs2000)

unit=int(input("Enter the units"))
charge=0
if unit>200:
    charge = charge + (unit - 200) * 10
    unit = 200

if unit > 100:
    charge = charge + (unit - 100) * 5
    unit = 100

if unit <= 100:
    charge = charge + unit * 0

print(charge)



10. Write a program to accept the price of a bike and display the road tax and insurance to be paid according to the following criteria . also display total amount to be paid.  
      
        Cost price (in Rs)           Tax                Inssurance  
        > 100000                     15 %                   20%  
        > 50000 and <= 100000        10%                    8%  
        <= 50000                     5%                     5%
        
a=int(input("Enter the price"))
tax=0
insu=0
if(a>100000):
    tax=a*15/100
    insu=a*20/100
    total=tax+insu+a
    print("the total amount to be paid = ",total)
if(a<=50000):
    tax=a*10/100
    insu=a*8/100
    total=tax+insu+a
    print("the total amount to be paid = ",total)
if(a>50000 and a<=100000):
    tax=a*5/100
    insu=a*5/100
    total=tax+insu+a
    print("the total amount to be paid = ",total)
        