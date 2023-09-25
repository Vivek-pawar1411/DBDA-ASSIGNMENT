
a= [100, 200, 300, 400, 500]
print(a[::-1])


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
subList = ["h", "i", "j"]
list1[2][1][2].extend(subList)
print(list1)

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

list1 =["Ashish", "", "Atharva", "Amit", "", "Revati"]
res = list(filter(None,list1))
print(res)

list1 = [5, 10, 15, 20, 25, 50, 20]
index= list1.index(20)
list1[index] = 200
print(list1)

import math
list1 = [1,4,9,16,25,36,49]
l2=[]
for i in list1:
  l2.append(math.sqrt(i))
print(l2)


l1=[]
for i in range(150,200):
    if i%2==0:
        l1.append(i)
print(l1)
l2 =[if i%4==0 for i in l1]:
    
print(l2)