# Hangman Project Documentation Guideline

> Created hangman game on Visual Studio Code using Python programming language

## Milestone 1 - User Input - Ask_letter method

- Answer some of these questions in the next few bullet points. What have you built? What technologies have you used? Why have you used those?
- Built a method which asks the user for its input making sure the input is correctly entered before calling another function. All the methods can only be called if the hangman class is created to ensure that the user is intended to play the hangman game (Object-Oriented Programming)

```python

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
```

> Insert an image/screenshot of what you have built so far here.

## Milestone 2 - Defining the initializer

- Does what you have built in this milestone connect to the previous one? If so explain how. What technologies are used? Why have you used them? Have you run any commands in the terminal? If so insert them using backticks (To get syntax highlighting for code snippets add the language after the first backticks).

- Example below:

```bash
/bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181
```

- The above command is used to check whether the topic has been created successfully, once confirmed the API script is edited to send data to the created kafka topic. The docker container has an attached volume which allows editing of files to persist on the container. The result of this is below:

```python
"""Insert your code here"""
```

> Insert screenshot of what you have built working.

## Milestone 3 - Check_letter and ask_letter methods

- Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.

- Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

- Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?
