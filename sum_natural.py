num=int(input("enter a number"))
#print(num*(num+1)/2)
sum=0
for i in range(0,num+1):
    sum=sum+i
print(f"sum of {num} natural number is {sum}")