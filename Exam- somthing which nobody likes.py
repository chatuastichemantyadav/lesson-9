import random
attendence=random.randint (-99, 99)
leave=random.randint(-99,99)

cause=input("you need a medical leave y/n :")

if cause=="Y" :
    print("leave granted!")
else:
    if attendence >= leave:
        print("leave granted!")
    else:
        print("leave denied!")
        print(attendence)