import os


os.system("tput setaf 1")
print("\t\t\t\t\tHERE IS MY TUI") 



os.system("tput setaf 7")
print("""\t\t\tCONTROL THE WHOLE LINUX JUST BY TYPING DIGITS\n
\t\t\t\t\tBY ABHIJEET PATHAK""") 





while True :
  print("""Press 1 :  For Adding user
press 2 : To update the whole system
press 3 : Making dir
press 4 : Connect to server/other system using ssh
press 5 : Make a file executable 
press 6 : To  configure web server 
press 7 :  Listing all the storage attached 
press 8 :  Troubleshoot Network Connectivity 
press 9 :  List all the hidden files in present directory
print 10 : Install particular package
print 11 : To exit""")
  print("enter your choice")
  ch=input()

  if ch == "1" :
        us = input("Name the user :")
        os.system("sudo adduser {} " .format(us))
        
  elif ch == "2" :
        os.system("sudo apt-get update && upgarde")
  elif ch == "3" :
        
         print("Dir name : " , end = "" )
         file_name= input()
         os.system("mkdir {}".format(file_name))
  elif ch == "4" :
    
           x , y = input("enter the user and ip : " ).split()
           os.system("ssh {}@{} " .format(x , y))
  elif ch == "5" :
           exe = input("Name the file : ")
           os.system("chmod +x {} " .format(exe))
           
  elif ch == "6" :
            print("place your files and data in  /var/www/ directory ")
            os.system("service apache2 start")
             
            
  elif ch == "7" :
          os.system("sudo fdisk -l && lsblk ")
  elif ch == "8" :
          os.system("sudo service NetworkManager restart")
  elif ch == "9" :
          os.system("ls -al")
  elif ch == "10" :
          pack = input("name the package/software :")
          os.system("sudo apt-get install {} " .format(pack)) 
  elif ch == "11" :
          print("Exiting...")
          exit()
                            
            
  else :
        print("Please enter a valid option")

 


