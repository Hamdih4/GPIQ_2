import json
import random

print("Hangman Game 1.0")
with open('data.json') as json_data:
    score = "Score"
    level = "Level"
    d = json.load(json_data)
availableScore = int(d[score])
currentLevel = int(d[level])
print("Score: "+str(availableScore)+" Level: "+str(currentLevel))
ch='y'
choice = raw_input("Press 1 to play or 2 to quit")
if(str(choice) == "1"):
    while(ch=='y'):
        to_guess = random.choice(open('words.txt').readlines())
        guesses = 5
        guesses_left = 5
        to_guess = to_guess.split("\r")[0]
        to_guess = to_guess.split("\n")[0]
        length = len(to_guess)
        guessed  = ('*')*length
        new_guessed = ""       
        while((guesses_left != 0) and (guessed != to_guess)):
            print("\n\nGuess the word: "+guessed).lower()
            print((str(guesses_left)) +" tries left")
            x = raw_input("What is your next guess?")
            isMatched=0
            for i in range(0,length):
                if to_guess[i] == x:
                    isMatched=1
                    new_guessed += x                           
                else:
                    new_guessed += guessed[i]                               
            guessed = new_guessed
            new_guessed = ""
            if (isMatched != 1):
                guesses_left-=1               
        if(guessed == to_guess):
            print("Matched, the correct word is "+to_guess)
            availableScore+=10
            currentLevel+=1
            print("Score: "+str(availableScore)+" Level: "+str(currentLevel))                        
        if(guesses_left == 0):
            print("Sorry, you missed this one, the word was: "+to_guess)
            print("Score: "+str(availableScore)+" Level: "+str(currentLevel))            
        ch = raw_input("Do you want to continue(Y/N)")
        if(ch.lower()=='y'):
            continue
        else:
            d[score] = availableScore
            d[level] = currentLevel
            with open('data.json', 'w') as outfile:  
                json.dump(d, outfile)
            break
else:       
    print("Exit")
