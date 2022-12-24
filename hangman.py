import random

from hangmanwords import wordslist
word = random.choice(wordslist).upper()

from hangmanart import hangmanasciiart
from hangmanart import hangmanstages

print(hangmanasciiart)
print("Welcome to Hangman! You have 6 lives, guess the correct word to win.")
wordblanks=[]
lives = 6
hangmanstage = 0

for i in range(0,len(word)):
     wordblanks.append("_")
for j in range(0,26):
    print(hangmanstages[hangmanstage])
    if lives == 0:
        print(f"You have lost all lives, the word was {word}. Game Over.")
        break
    if "_" not in wordblanks:
        print("Congratulations, you win!")
        print(wordblanks)
        break
    print(wordblanks)
    alphabet = input(f"You have {lives} lives left. Guess an alphabet: \n").upper()
    if alphabet not in word:
        lives+=-1
        hangmanstage+=1
        print(f"The letter {alphabet} is not in the word.")
        continue
    if alphabet in word:
        for k in word:
            if alphabet == k:
                wordblanks[word.index(k)] = f"{alphabet}"
                print(f"The letter {alphabet} is in the word.")
                continue