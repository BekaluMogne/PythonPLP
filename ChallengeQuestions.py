# Factorial of the numbers
base=input('enter the base')
expo=input('enter expo')
def sq(base,expo):
     if(int(base)**int(expo))>=500:
         return True
     else:
            return False
print(sq(base,expo))
