#Day7 Hangman 


#import replit clear to clear the screen 
# from replit import clear 
import random 


#TODO-1: Update the word list to use the 'word_list' from hangman_words.py


import hangman_words
import hangman_art


choose_word = random.choice(hangman_words.word_list)


#Create a variable called 'lives' to keep tack of the number 
# of lives left. Set 'Lives' to equal 6. 
lives = 6


#Testing code 
# print(f'Pssst, the solution is {choose_word}.')


#Setup the game 
display = []
for _ in range(len(choose_word)):
    display += "_"

#Define the state of the game 
end_of_game = False 

print(hangman_art.logo)


#While loop to keep running the game until the play win/lose 
while(end_of_game == False):

    #Get the input from the user 
    guess = input("Guess a letter: ").lower()

    #clear the screen to have a cleanner UI
    # clear()


    #check if the guess is correct. If not, reduce the life of the player
    if guess not in choose_word: 
        lives -= 1
        print(hangman_art.stages[lives])
        

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the
# display at that position. 

    for position in range(len(choose_word)):
        letter = choose_word[position]


        if letter == guess: 
            display[position] = letter

    print(display)
 
    if "_" not in display:
        end_of_game = True
        print("You win")
    elif lives == 0:
        end_of_game = True
        print("You've lost")
    





    