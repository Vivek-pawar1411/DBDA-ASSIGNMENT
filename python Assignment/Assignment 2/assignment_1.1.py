# 1 What will be output of printing following calculations
a=1.5e200 *2.0e210
print (a)
b=3.4e-320 / 1e100
print(b)



#Q2. What is output of printing following
a=1/3
b=format(1/3, '.3f')
c=format(1/3, '.1f')
d=6*1/3
e=1/3 + 1/3 + 1/3 + 1/3 + 1/3 + 1/3
print(a)
print(b)
print(c)
print(d)
print(e)


#Q4
#a print only first 5 decimal values of 22/7 
a=format(22/7, '.5f')
print(a)
#print Hello string with 5 spaces on right side, 'Hello     ' ( hint: use <)
a = "Hello {:<5}"
print(a.format(""))
 #print Hello string with 5 spaces on left side, '     Hello' ( hint: use <) 
a = "{:<5} Hello"
print(a.format(""))
#print Hello string with 5 '#' on left side and 5 '#' on right side, '     Hello    
#print(a.format("Hello":^15))
format('Hello','#^15')




#Q5. We can use ord() to print ASCII value of single character and chr() to convert given ASCII value to character. 
#a. find ASCII of characters'a' , 'A' , 'z' , 'Z' using ord() one by one
a=ord('A')
print(a)   
b=ord('a')
print(b)   
c=ord('z')
print(c)   
d=ord('Z')
print(d)   
#b. find ASCII of characters '0', '9', ' ', "\n" , "\t" using ord() one by one
a=ord('0')
print(a)   
b=ord('9')
print(b)   
c=ord(' ')
print(c)   
d=ord('\n')
print(d) 
e=ord('\t')
print(e)

#c. Find characters for ASCII values 35, 67, 50, 99
a=chr(35)
print(a)   
b=chr(67)
print(b)   
c=chr(50)
print(c)   
d=chr(99)
print(d)  
#d. Where ASCII value begin for lower case characters where it ends? also find same for digits and upper case characters
# The ASCII value for lower case character begin with 97 and end with 122.
# The ASCII value for upper case character begin with 65 and end with 96.
# The ASCII value for digit  begin with 48 and end with 57.


#Q6. Find how special chracters work inside print function
print("abc","\n","bcd")
print("abc\nbcd")
print(1,'\n',2)
print("hello \n\n!!")
print("This is '\t' means tab")

print("This","is","different",sep='\t')
print("This","is","different",sep='#')
print("This","is","different",sep='\n') 
print("This","is","different",end='\n')

#Q7. What is output of following statements and understand how operators work
print(10 / 2)
print(10 // 2.0)
print(101 / 3)
print(101 // 3)
print(101 % 3)
print(2 ** 4)
print(3 ** 2)
print(abs(-10)) # give absolute value
print(divmod(101,3)) # divmod gives two values , interger division and remainder
print(8 << 1)
print(8 << 2)
print(32 >> 2)
print(16 >> 1)



#Q8. Write a program to take marks of 3 subjects from a student. Calculate total in variable name 'total'.
#(NOTE: Don't use sum as variable name, it is built in function in python)
math =50
chem=80
phy=75
total=math+chem+phy
print("total = ",total)


#Q9. Manually calculate output of following expressions using precedence and associativity rules 
#and then verify output using python shell
print(2 + 3 * (4 -1))
print(2 + ((3 *4) - 8))
print((2 + 3) * 4)
print(-10 + 25 / (16 + 12))
print(2 ** 2 ** 2)
print((3 ** 2) ** 3)
#print(x = y = 3 + 5)
print(8/2*(2+2))


#Q10. Check output of following 
#print(x = y = 10)
#print(x1 = 20 = y1)

#Q11. What is output of following
#a. x=10
#y=34.4
#print(x and y)
#print(x or y)
