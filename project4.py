import random 
#this is all the words
word_list = ["heart","loopy","audio","laugh","trial","sound","quick","jumpy","junky","pluck","goopy","truck","truth","snipe","daddy","crank","zesty","musty","dusty","brain","claim","prank","zoink","poise","plane","shame","plain","train","loser","monky",]
hidden_word = random.choice(word_list)
#remove the "#" to see the chosen word
#print (hidden_word) 


print ("gusse a five letter word you have five gusses good luck")

# number of gusses this loop goes from line 12 to line 58 and repets 5 times x 
for i in range(5):

    guess_word = input()
    output = ""


    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
     output += "🟨"
    else:
        output += "⬛"

    if guess_word[1] == hidden_word[1]:
     output += "🟩"
    elif guess_word[1] in hidden_word:
     output += "🟨"
    else:
        output += "⬛"

    if guess_word[2] == hidden_word[2]:
     output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"




    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
