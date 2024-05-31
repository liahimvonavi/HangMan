import random
word = ["gypsy", "caramel" "star wars"]
chosen_word = random.choice(word)
shown_word = ["_"] *(len(chosen_word))
same_input = []
lives = 6
while "_" in shown_word:
    print(' '.join(shown_word))
    guessed = input("Guess a letter: \n").lower()
    if len(guessed)==1:

        if guessed in same_input:
            print("You have already picked this letter try again with another one.")

        else:
            same_input.append(guessed)
            if guessed in chosen_word:
                for index, letter in enumerate(chosen_word):

                    if letter==guessed:
                        shown_word[index]=letter

            else:
                lives-=1
                print(f"You have {lives} left\n")
                if lives == 0:
                    print("You Lose!Game Over!")
                    exit()
    else:
        print("Invalid input!You can only choose one letter at a time!")
fullword = ''.join(shown_word)
print(fullword)
print("You Win ")