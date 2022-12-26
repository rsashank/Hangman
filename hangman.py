import random

from hangmanwords import wordslist
word = random.choice(wordslist).upper()

from hangmanart import hangmanasciiart
from hangmanart import hangmanstages

print(hangmanasciiart)
print("Welcome to Hangman! You have 6 lives, guess the correct word to win.")
wordblanks=[]
consonants = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
vowels = ["A","E","I","O","U"]
letters = []
lives = 6
hangmanstage = 0
flag = 0

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
    if letters !=[]:
        print("Used Letters: ", letters)
    if lives <4 and flag!=1:
        hint = input(f"Would you like a Hint? You have {lives} lives left. (Yes/No)").upper()
        if hint == "YES":
            flag=1
            vowel=0
            consonant=0
            for z in range(0,len(word)):
                    if word[z] in vowels:
                        vowel+=1
                    elif word[z] in consonants:
                        consonant+=1
            print(f"Hint: The word has {vowel} vowels and {consonant} consonants.")
    alphabet = input(f"You have {lives} lives left. Guess an alphabet: \n").upper()
    if alphabet not in consonants + vowels:
        alphabet = input(f"Please enter an ALPHABET only. You have {lives} lives left.\n").upper() 
    elif alphabet in letters:
        print("Used Letters: ", letters)
        alphabet = input(f"You have already used that alphabet, choose another. You have {lives} lives left.\n").upper()
    letters.append(alphabet)
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