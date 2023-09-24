#!/bin/bash
pos=0
neg=0
zero=0
for((i=1;i<=10;i++))
do
echo " Enter the num = " 
read n
 
 if [[ $n -gt 0 ]];
then 
       pos=$((pos+1))
  elif [[ $n -lt 0 ]]
then  
  neg=$((neg+1))
else 
  zero=$((zero+1))
fi
done
echo " Positive = $pos "
echo " Negative = $neg "
echo " zero = $zero "
