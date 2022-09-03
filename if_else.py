a=int(input("enter your age \n"))
if (a>=18 and a<=59):
    print("yes, you are eligible \n")
elif (a<18 and a>=12):
    print("you are minor\n") 
elif (a<12 and a>0):
    print("kids") 
elif (a>59 and a<=80):
    print("are budhau kaise ho ")
elif (a>80 and a<=100):
    print("kya baat h sir ,kuch tips btaiye \n")

else:
    print("enter a valid age")