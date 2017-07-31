#first question
ques1 = input("you are walking into a bar. in the right, u see old man getting robbed. will you help him? (y/n)")
print("------------------------------------------------------------")
#what happens in different cases(ques1)
if ques1 == "y" or ques1=="yes":
    #second question
    ques2 = input("you are getting into a fight with anonymus robbers, you see a gun with your eye. if you want to fight press y. if you wanna run away, press n")
    print("------------------------------------------------------------")
    #what happens in different cases(ques2)
    if ques2 == 'y' or ques2 == 'yes':
        #third question
        ques3 = input('the robber pulled the gun on you. would you like to unarm him? if so press y!')
        print("------------------------------------------------------------")
        #what happens in different cases(ques3)
        if ques3 == 'y':
            print('you approched the robber.he aimed the gun towards you and you kicked the gun.you killed the robbers.you see that the old man is not an old man,and he took your wallet.')
            print('will you fight with him(he looks strong) (y), you are going to pick up the gun you kicked before in order to shoot him (n), you let him escape(z)')
            #fourth question
            ques4 = input()
            print("------------------------------------------------------------")
            #what happens in different cases(ques4)
            if ques4 == "y":
                print("he knocked you out, you woke up in antartica, NAKED, game over!")
                print("------------------------------------------------------------")

            elif ques4 == "n":
                #fifth question
                ques5 = input("you were running to pick the gun off the floor, but the old man escaped. you are going to your car, and when you are close to your home, ")
                print("------------------------------------------------------------")

            else:
                print("GAME OVER!")
        else:
            print("you are coward! GAME OVER!")
    else:
        print("he shot you in the nuts! GAME OVER!")
else:
    print("what if he was your grandpa? GAME OVER!")
                          
