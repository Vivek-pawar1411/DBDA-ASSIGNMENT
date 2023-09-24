  #!?bin/bash
  echo " Select one =
       1. add user
       2. delete user
       3. add group 
       4. delete group " 
 read  -p "Enter the choice "  a
case $a in 
  1)     
        read  -p "Enter the username = " usr
              sudo useradd $usr 
               ;;
    2)    
        read -p " Enter the username " usr
              sudo userdel $usr
               ;;
   3)  read -p "Enter the group name " grp 
              sudo groupadd $grp
               ;;
   4)
                read -p " Enter the group name " grp
                   sudo groupdel $grp
               ;;
  esac
