#!/bin/bash 
echo "For Adding and Deletion and Search choose  from giben below
       1) Adding Student records
       2) Deletion of Student records 
       3)  Search Student records " 
    read -p  "Enter the choose " n
   case $n in
      1)
        read -p "Enter the student name " nam 
       read -p "Enter the rollno . "  roll 
       read -p "Enter the semster " sem
       read -p "Enter the marks sub1 " sub1
       read -p "Enter the marks sub2 " sub2
      read  -p " Enter the marks sub3 " sub3
   echo -n  "Name =  " $nam  "roll no = " $roll  "Semster = " $sem
          echo -n  "subj 1 = "  $sub1  "subj 2 = " $sub2   "subj 3 = " $sub3 >>record.txt
         sort -n record.txt
        ;;
 2)
    read -p "Enter the rollno for Deletion of record" roll
    sed -i "/$roll/d" record.txt
        cat  record.txt
       ;;
     3) 
read -p "Enter the roll no. for Search " roll
 grep -i '$roll' record.txt
   ;;
  *)
     echo  "Invlid entry"
     ;;
 esac
