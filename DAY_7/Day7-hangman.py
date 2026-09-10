#DAY 7: Random Word Generator
import random
from hangman import wordslist as words
lives = 6
word_list = words
random_word = random.choice(word_list)
print(random_word)

placeholder = "_" * len(random_word)
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
      
    guess = input("Guess the letter: \n").lower()
    display=""
    
    for i in random_word:
        if i == guess:
            display += i 
            correct_letters.append(i)
        elif i in correct_letters:
            display += i 
        else:
            display += "_"
    
    if guess not in random_word:
        print(f"Wrong guess! The letter '{guess}' is not in the word.")
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"Game Over! The word was '{random_word}'. Better luck next time!")
        
            
    print(display)
    if "_" not in display:
        game_over = True
        print("Congratulations! You've guessed the word correctly.")
    
    print(f"Lives remaining: {lives}")