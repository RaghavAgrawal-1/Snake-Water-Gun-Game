import random
computer = random.choice([-1,1,0])
youstr=input("Enter Your Choice S/W/G :")
youdict = {"s":1,"w":-1,"g":0}
reversedict={1:"Snake",-1:"Water",0:"Gun"}
you=youdict[youstr]
print (f"You Chose {reversedict[you]}\nComputer Chose {reversedict[computer]}")
if(computer==you):
    print("It's a Draw!")
else:
    if(computer ==-1 and you ==1):
        print("You Win!")
    elif(computer ==-1 and you ==0):
        print("You Lose!")
    elif(computer ==1 and you ==0):
        print("You Win!")
    elif(computer ==1 and you ==-1):
        print("You Lose!")
    elif(computer ==0 and you ==1):
        print("You Lose!")
    elif(computer ==0 and you ==-1):
        print("You Win!")
    else:
        print("Something Went Wrong!")