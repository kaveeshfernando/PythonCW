  # I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20200142        
  
# Date: 11/12/2020


import sys 
try:
      P = int(input("Enter pass credits:")) 
      if P not in [0, 20, 40, 60, 80, 100, 120]: 
         print("Range Error")                    
         sys.exit()                              
      D = int(input("Enter defer credits:")) 
      if D not in [0, 20, 40, 60, 80, 100, 120]:  
         print("Range Error")
         sys.exit()
      F = int(input("Enter fail credits:")) 
      if P not in [0, 20, 40, 60, 80, 100, 120]: 
         print("Range Error")
         sys.exit()

      if P + D + F == 120:    
         if (P==120 and D==0 and F==0):
                 print('Progress')

         elif (P==100 and F==0) or (P==100 and F==20):
            print('Progress - module trailer')

         elif (D==0 and F==80 or F==100 or F==120) or (D==20 and F==80 or F==100) or (D==40 and F==80):
            print('Exclude')

         else:
            print('Do not progress - module retiever')

      elif P + D + F != 120:  
         print("Total incorrect.")


except ValueError:
      print('Intergers Required')





