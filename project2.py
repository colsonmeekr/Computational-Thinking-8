answer1 = input("its almost lunch time where do you go uvill or the mall")

if answer1 == "mall":
    answer2 = input("want to get pretzels")
    if answer2 == "yes":
        print ("you get pretzels yummm")
    elif answer2 == "no": 
        print ("you dcide to walk and talk instead")
    elif answer2 == "idk": 
        print ("you dcide to get pretzels and walk around")
    else:
        print ("answer only yes and no or you can answer idk")
if answer1 == "uvill":
    answer2 = input("want to get shake shack")
    if answer2 == "yes":
        print ("you get a vanilla shake")
    elif answer2 == "no":
        print ("you dont go to shake shack and go to apple store instead")
    elif answer2 == "idk":
        print ("you decide to buy clothes instead")
    else:
        print ("answer only yes and no")
        if answer1 == "nither":
            answer2 = input("want to play soccer or go home")
        if answer2 == "go home":
            print ("you go home and play video games")
        else:
            print ("you go and play soccer")
        if answer1 == "stay at school":
            print ("you stay at school and do homework")
        else:
            print ("you go to beach club")
