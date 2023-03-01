#Step 4

import random


end_of_game = False
import hangman_words
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)


import hangman_fig
print(hangman_fig.logo)
lives=6




print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f"you have already guessed {guess} letter")
    
    for position in range(word_length):
        letter = chosen_word[position]
       
        if letter == guess:
            display[position] = letter

   
    if guess not in chosen_word:
      print("you have chosen a word that's not in the list you have lost a life")
      lives-=1
      if lives ==0:
        end_of_game = True
        print("You lose")
  
    print(f"{' '.join(display)}")

   
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    from hangman_fig import stages
    print(stages[lives])