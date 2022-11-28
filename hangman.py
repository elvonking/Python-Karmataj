# import libraries
import random
import time

# intro to the game and get player details
print("\nWelcome to Hangman game by Elvis!\n")
name = input("What's your name?")
print(f"Hello {name}! Best of Luck!")
time.sleep(2)
print("The game is about to start!\nLet's play Hangman!")
time.sleep(3)

# game parameters
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game

    wordy = ["vibranium","seirra","longing","freight","mustang","desire","coder","techie","babes","black","panther"]

    word = random.choice(wordy)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

# the game loop after the first turn ends
def play_loop():
    global play_game
    play_game = input("Do you want to play again! y = yes, n= no \n")
    while play_game not in ["y","Y","n","N"]:
        play_game = input("Do you want to play again! y = yes, n= no \n")
    if play_game.lower() == "y":
        main()
    elif play_game.lower() == "n":
        print("Thanks for playing! See you soon!")
        exit()

# defining the game conditions and the logic
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5

    guess = input(f"This is the correct word: {display}. Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Input is invalid. Try again!\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(f"{display}\n")

    elif guess in already_guessed:
        print("Try another letter.\n")
    
    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
            print(f"Wrong guess. {str(limit - count)} guesses remaining.\n")
        
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                "  |      |\n"
                "  |      |\n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
            print(f"Wrong guess. {str(limit - count)} guesses remaining.\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                "  |      |\n"
                "  |      |\n"
                "  |      |\n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
            print(f"Wrong guess. {str(limit - count)} guesses remaining.\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                "  |      |\n"
                "  |      |\n"
                "  |      |\n"
                "  |      O\n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
            print(f"Wrong guess. {str(limit - count)} guesses remaining.\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                "  |      |\n"
                "  |      |\n"
                "  |      |\n"
                "  |      O\n"
                "  |     /|\ \n"
                "  |     / \ \n"
                "__|__\n")
            print(f"Wrong guess. You lose!\n")
            print(f"The correct word is: {already_guessed},{word}.")
            play_loop()
    if word == "_" * length:
        print("Congrats! You have guess the word correctly!")
        play_loop()
    
    elif count != limit:
        hangman()

main()

hangman()

# the end, with interdimensional powers, from Karma Taj, by Master Primordial Otas
