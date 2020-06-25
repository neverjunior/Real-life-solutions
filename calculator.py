import re

print("Abhijeet's first calc..")
print("Type 'q' to quit\n")


previous = 0 
run = True

def performMath():
   global run
   global previous
   equation = "" 
   if previous == 0:
       equation = input("Enter eq..")
   else :
       equation = input(str(previous))
       print(equation)


   if equation == 'q':
        run = False
   else:
        equation = re.sub('[a-zA-Z]'  , "" , equation )

        if previous == 0 :
            previous = eval(equation)
            print(previous)
        else:
            previous = eval(str(previous) +  equation ) 
            print(previous)








while run:
    performMath()




