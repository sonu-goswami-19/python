#table of any number taken by user
'''
num=int(input("enter a number"))
for i in range (1,11):
   # print(str(num) + "x" +str(i) +"="+ str(num*i)) either we use this or 
   print(f"{num} X {i}={num*i}")
   '''
l1=["harry","sachin" ,"rahul" ,"sohan"]
for name in l1:
    if name.startswith("s"):
        print("hello" + name )

num=int(input("enter a number"))
i=1
while i<=10:
    print(str(num) + "x" +str(i) +"="+ str(num*i))
    i=i+1