'''
def farh(c):
    return (c*(9/5)) + 32

c=-40
f=farh(c)
print("farenheit temperature " + str(f))
'''
def sum(num):
    num=0
    for i in range(0,num+1):
        sum=num+i

num=int(input("enter a number"))
s=sum(num)
print("sum of n natural numbers is" + str(sum))