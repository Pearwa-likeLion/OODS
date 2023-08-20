# *** multiplication or sum ***
# Enter num1 num2 : 20 30
# The result is 600
print("*** multiplication or sum ***")
x,y = input("Enter num1 num2 : ").split()
if(int(x)*int(y)> 1000):
    print("The result is "+str(int(x)+int(y)))
else : print("The result is "+str(int(x)*int(y)))