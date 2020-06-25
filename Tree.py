import os

def abhi( path , fil  , depth):
      print('|'+depth*"--" ,fil)
      if os.path.isdir(path):
         for obj in os.listdir(path):            
        
            abhi(path+'/' +obj, obj , depth+1 )
           
        



abhi("/home/neverjunior/Videos" , "Videos" , 0 )                          
