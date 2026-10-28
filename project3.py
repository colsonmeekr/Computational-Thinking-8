soccer_points = 0
baseball_points = 0
basketball_points = 0
#this sets the points all to 0 at start 
# try getting 5 of one type!!!
answer1 = input ("would you rather A, buy a new bat. B, buy a new soccer ball. C, buy a new basket ball")
if answer1 == "A":
    baseball_points += 1
elif answer1 == "B":
    soccer_points += 1
elif answer1 == "C":
    basketball_points += 1
else :
    print ("please answer only with A,B,C")
    # next qustion
answer2 = input ("would you rather A, go to the baseball field. B, go to the soccer field. C, go to a basktball court")
if answer2 == "A":
    baseball_points += 1
elif answer2 == "B":
    soccer_points += 1
elif answer2 == "C":
    basketball_points += 1
else :
    print ("please answer only with A,B,C")
answer3 = input (" would you rather A, play for the dodgers. B, play for barcelona. C, play for lakers.")
if answer3 == "A":
    baseball_points += 1
elif answer3 == "B":
    soccer_points += 1
elif answer3 == "C":
    basketball_points += 1
else :
    print ("please answer only with A,B,C")
    
answer4 = input ("would you rather A, go to baseball stadium. B, go to soccer stadium. C, go to basketball stadium.")
if answer4 == "A":
    baseball_points += 1
elif answer4 == "B":
    soccer_points += 1
elif answer4 == "C":
    basketball_points += 1
else :
    print ("please answer only with A,B,C")
    
answer5 = input ("would you rather A meet aron judge.  B meet meesi and lebron.  C meet lebron and messi.")
if answer5 == "A":
    baseball_points += 1
elif answer5 == "B" or answer5 == "C":
    soccer_points += 1
elif answer5 == "C":
    # not needed becouse alresdy incorpprated with the or 
    basketball_points += 1
else :
    print ("please answer only with A,B,C")




print (f"your score is {basketball_points} basktball, {soccer_points} soccer, {baseball_points} baseball")
#basketball points endeing here
if basketball_points > soccer_points and basketball_points > baseball_points:
    print ("you are a basktball person!!!")
    #soccer points endeing here
elif soccer_points > basketball_points and soccer_points > baseball_points:
    print ("you are a soccer person!!!!")
    #basetball points endeing here
elif baseball_points > basketball_points and baseball_points > soccer_points:
    print ("you are a basball person")
else: 
    print ("i meesed up")