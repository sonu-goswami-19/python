import random 
def game_win(comp,you):
    if comp == you :
        return None 
    else :
        if comp == 'r':
            if you =='p':
                return True
            elif you=='s':
                return False 

        if comp == 'p':
            if you =='s':
                return True
            elif you == 'r':
                return False 

        if comp == 's':
            if you =='r':
                return True
            elif you == 'p':
                return False 


#print(comp turn : rock(r),paper(p),scissiors(s)??")
randNo = random.randint(1,3)
print(randNo)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

while True:
    ask = input("do you wanna play?  (y/n) ")
    if ask =='y':
        you = input("your's turn : rock(r),paper(p),scissiors(s)??    ")
        a =game_win(comp,you)

        print(f"computer choice is {comp}")
        print(f"your choice is {you}")

        if a==None :
            print("its a tie ")
        elif a==True:
            print("you won")
        else:
            print("you lose")
    elif ask == 'n':
        print("thank you")
        break
    else:
        print("wrong input")