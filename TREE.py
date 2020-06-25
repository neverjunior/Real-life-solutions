import os

def abhi( path , fil  , depth):
      print('|'+depth*"--" ,fil)
      if os.path.isdir(path):
         for obj in os.listdir(path):            
        
            abhi(path+'/' +obj, obj , depth+1 )
           
        



abhi("" , "" , 0 )#write the directory full path in first place and the pwd in second.                          
