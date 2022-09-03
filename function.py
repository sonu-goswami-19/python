'''
def greet(name ="stranger"):
    print("good day " + name)

def sum(num1, num2):
    return print(num1 + num2)
    '''

def ifprime(number):
    prime =True 
    for i in range(2,number):
        if number%i==0:
            prime=False
            break
    if prime:
        print(str(number) +" is prime number")
    else:
        print(str(number) + " is not prime number")

ifprime(12)
ifprime(17)
ifprime(56)

#sum(32, 6)



#greet("sonu")
#greet()