def maximum(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            return num1
            print("the greatest number is " +str(num1))
        else:
            return num3 
            print("the greatest number is " +str(num3))

    if num2>num1:
        if num2>num3:
            return num2 
            print("the greatest number is " +str(num2))
        else:
            return num3 
            print("the greatest number is " +str(num3))
  

num1=int(input("enter num1\n"))  
num2=int(input("enter num2\n"))  
num3=int(input("enter num3\n"))

m=maximum(num1,num2,num3) 

print("maximum is " + str(m) )
