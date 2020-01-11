'''
this game plays the hangman game
'''
import random
COUNT_WRONG = 0
CHARACTER_GUESSED = ""
WIN = 0
print("Howdy! I know you don't know me, but help me save this innocent man's life! The sheriff is going to hang this man if you don't beat his word game! Guess all the letters in the word that the sheriff  is guessing before this innocent man's life is over! ")
NAME_PLAYER= input("what's your username: ").upper()
while len(NAME_PLAYER) > 6 or len(NAME_PLAYER) == 0:
    print("please username can't be longer 6 characters or empty")
    NAME_PLAYER = input("what's your username: ").upper()
def main():
    '''
    this is the main function for the game, it plays the game when called
    '''
    words = {1:"Awkward", 2:"Bagpipes", 3:"Banjo", 4:"Bungler", 5:"Croquet", 6:"Crypt", 7:"Dwarves", 8:"Fervid", 9:"Fishhook", 10:"Fjord", 11:"Gazebo", 12:"Gypsy", 13:"Haiku", 14: "Haphazard", 15:"Hyphen", 16:"Ivory", 17:"Jazzy", 18:"Jiffy", 19:"Jinx", 20:"Jukebox"}
    wrong_guess = []
    chosen_word_array = []
    correct_guess = []
    number = random.randint(1, 20)
    chosen_word = words[number].upper()
    for i in chosen_word:
        chosen_word_array.append(i)
    def turn():
        global COUNT_WRONG
        global CHARACTER_GUESSED
        global WIN
        CHARACTER_GUESSED = input("\nGuess a character in the word ").upper()
        while not CHARACTER_GUESSED.isalpha() or len(CHARACTER_GUESSED) != 1 or (CHARACTER_GUESSED in correct_guess):
            print("please enter an alphabet that you haven't already inserted")
            CHARACTER_GUESSED = input("\nGuess a character in the word ").upper()
        if CHARACTER_GUESSED in chosen_word:
            for i in range(chosen_word.count(CHARACTER_GUESSED)):
                correct_guess.append(CHARACTER_GUESSED)
            for k in chosen_word:
                if k in correct_guess:
                    print(k, end='')
                else:
                    print(' _', end="")
            if len(correct_guess) == len(chosen_word):
                WIN += 1
                print("\nyou won the game")
                option = input("Do you want to play a new game? Y/N ").upper()
                while option not in ("Y", "N"):
                    print("PLease enter a valid input")
                    option = input("Do you want to play a new game? Y/N ").upper()
                newgame(option)
            else:
                turn()
        else:
            wrong_guess.append(CHARACTER_GUESSED)
            COUNT_WRONG += 1
            hangman_art(COUNT_WRONG)
    def leaderboard():
        DICT_PLAYER_WINS = {}
        with open('leaderboard.txt', "a+") as file:
            file.write(NAME_PLAYER +"\t"+ str(WIN) + "\n")
        with open('leaderboard.txt', "r+") as file:
            for line in file:
                words = line.split()
                if words[0] in DICT_PLAYER_WINS:
                    DICT_PLAYER_WINS[words[0]] += int(words[1])
                else:
                    DICT_PLAYER_WINS[words[0]] = int(words[1])
            sortitems = sorted(DICT_PLAYER_WINS.items(), reverse=True, key=lambda x: x[1])
            print("PLAYER       WINS")
            for item in sortitems:
                print(item[0].ljust(13, '-'), item[1])
    def newgame(option):
        global COUNT_WRONG
        global CHARACTER_GUESSED
        if option == "Y":
            COUNT_WRONG = 0
            CHARACTER_GUESSED = ' '
            main()
        elif option == "N":
            print("game over")
            leaderboard()
    def hangman_art(COUNT_WRONG):
        print(' -------')
        if COUNT_WRONG == 1:
            print(" |    |\n \n |    o \n \n |\n \n |\n\n |\n\n-|-")
            turn()
        elif COUNT_WRONG == 2:
            print(" |    |\n \n |    o \n \n |    |\n \n |\n\n |\n\n-|-")
            turn()
        elif COUNT_WRONG == 3:
            print(" |    |\n \n |    o \n \n |   /|\n \n |\n\n |\n\n-|-")
            turn()
        elif COUNT_WRONG == 4:
            print(" |    |\n \n |    o \n \n |   /|\\\n \n |\n\n |\n\n-|-")
            turn()
        elif COUNT_WRONG == 5:
            print(" |    |\n \n |    o \n \n |   /|\\\n \n |   /\n\n |\n\n-|-")
            turn()
        elif COUNT_WRONG == 6:
            print(" |    |\n \n |    o \n \n |   /|\\\n \n |   / \\\n\n |\n\n-|-")
            print(("You lost the game, man is hanged!"))
            option = input("Do you want to play a new game? Y/N ").upper()
            while option not in ("Y", "N"):
                print("PLease enter a valid input")
                option = input("Do you want to play a new game? Y/N ").upper()
            newgame(option)
    turn()
main()
