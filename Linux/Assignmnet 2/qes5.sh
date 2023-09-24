#!/bin/bash
read -p "Enter the string" a
 echo  $a>temp.txt
rvs="$(rev temp.txt)"
if [ $a = $rvs ]
then 
 echo " palindrome "
 else 
    echo " not palindrone "
 fi

