'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random
from site import check_enableusersite
from typing import Counter

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):

        self.word = random.choice(word_list) # Gets a random word from the word_list
        print("The mystery word has",len(self.word), "characters") # Telling user how many letters in the word
        self.word_guessed = list('_' * len(self.word)) # Displaying the hidden letters in the word
        print(self.word_guessed)
        self.list_letters = []
        self.num_lives = num_lives
        self.num_letters = len(Counter(self.word).keys()) # Gets the number of unique letter in the word by using 'key' method
        pass

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''

        if self.letter in self.word: # Checks the letter to see if it contains in the word
            dupe_letter_count = self.word.count(self.letter) #Checks for the total number of letter is in the word
            self.letter_index=0
            for x in range(dupe_letter_count): # Loop around and setting the display of the letters.
                self.letter_index = self.word.find(self.letter, self.letter_index)
                self.word_guessed[self.letter_index] = self.letter # Replace the '_' with the letter
                self.letter_index+=1 
            else:
                print("Nice!",self.letter,"is in the word!")
                print(self.word_guessed)
                self.num_letters -= 1 # Reduce the unique letter by 1
        else:     
            print("Sorry,",self.letter, "is not in the word. :( ")
            self.num_lives -= 1 # Reduces live by 1 when letter is not in word
            print("You have",self.num_lives, "lives left!")
            print(self.word_guessed)
        pass

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        # Asking for a single character input
        while True:
            try:
                self.letter = input("Enter a letter: ").lower()
                if len(self.letter) == 1 and self.letter.isalpha() == True:
                    if self.letter in self.list_letters: # Check to see if the same letter has entered.
                        print(self.letter,"was already tried")
                        print(self.word_guessed)
                        print(self.draw_hangman(self.num_lives))           
                    else:
                        self.list_letters.append(self.letter)
                        self.check_letter(self.letter) # Letter valid calls check_letter
                        print(self.draw_hangman(self.num_lives))
                        if self.num_letters == 0: # Win condition
                            print("Congratulations, you won!")
                            break
                        if self.num_lives == 0: # Lose condition
                            print("You ran out of lives. The word was",self.word)
                            break
                else:            
                    if self.letter.isalpha() == False:
                        print("Please enter an alphabet letter")
                    else:
                        print("Please, enter just one character")
                    print(self.word_guessed)
                    print(self.draw_hangman(self.num_lives))
            except:
                print("An exception occured")
        pass

    def draw_hangman(self, num_life): # Displaying the hangman
        
        stages = [ """
                ---------
                |       |
                |       0
                |      \\|/
                |       |
                |      / \\
        ""","""
                ---------
                |       |
                |       0
                |      \\|/
                |       |
                |      /
        ""","""
                ---------
                |       |
                |       0
                |      \\|/
                |       |
                |      
        ""","""
                ---------
                |       |
                |       0
                |      \\|
                |       |
                |      
        ""","""
                ---------
                |       |
                |       0
                |      
                |       
                |      
        ""","""
                ---------
                |       |
                |       
                |      
                |       
                |      
        """
        ]
        return stages[num_life]
        pass

def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    print(game.draw_hangman(num_life=5))
    game.ask_letter() # Testing the method
    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
