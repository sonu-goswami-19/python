#__Typing_Speed_Calculator
from time import *
import random as r


def mistake(par_test,user_test):
    error = 0
    for i in range(len(par_test)):
        try:
            if par_test[i] !=user_test[i]:
                error = error + 1
        except :
            error = error + 1

    return error


def speed_time(time_s,time_e,user_input):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(user_input)/time_R
    return round(speed)
while True:
    chk = input("ready to test : yes/no ")
    if chk == 'yes':
        test = ["Don’t take rest after your first victory because if you fail in second, more lips are waiting to say that your first victory was just luck.",
        "All of us do not have equal talent. But , all of us have an equal opportunity to develop our talents.",
        "If you want to get something which you never had, you have to do something that you never did"]

        test1 =r.choice(test)
        print("   *****TYPING TEST*****")
        print(test1)
        print()
        print()

        time_1 = time()

        test_input=input("Enter : ")

        time_2 = time()

        print('speed : ',speed_time(time_1,time_2,test_input),"w/sec")
        print("error : ",mistake(test1,test_input))
    elif chk == 'no':
        print("thank you ")
        break

    else:
        print("wrong input")