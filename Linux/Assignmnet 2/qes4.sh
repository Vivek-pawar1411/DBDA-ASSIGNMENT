#!/bin/bash
min=1000
max=0
for ((i=1;i<=5;i++))
do
read -p " Enter the number " a
  if [ $a -gt $max ]
   then 
       max=$a
  elif [ $a -lt $min ]
  then 
    min=$a
  fi 
done
echo " the max = $max "
echo " the min = $min "
