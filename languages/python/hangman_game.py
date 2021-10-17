import random
import word_list as w
import hangman_art as A

print(A.logo)

print("GUESS THE WORD IF U CAN  \n")

lives=6

# choosing a random word from list
choosen_word=random.choice(w.list)

# an empty list is created and for each letter in choosen word "_" (blank) is added to the list.
display=[]
length=len(choosen_word)
for _ in range(length):
  display+="_"

# we can also use append method to add blanks to a list 
# for i in range(length):
#   display.append("_")

end_game=False

# this while loop will run until all blanks get filled.
while not end_game:
  
  guess=input("guess a letter :   ").lower()
  
  # if player had already guessed the letter.giving feedback that they have already guessed.
  if guess in display:
    print(f"You have already guessed the letter {guess}")

  # if letter guessed is present in the choosen_word replacing the blank with the letter in the postion that it have to be.
  for position in range(len(choosen_word)):
    if guess==choosen_word[position]:
      display[position]=choosen_word[position]


  #if the gueesed letter is not there in the choosen_word then the player will loose one life
  if guess not in display:
    lives-=1
    print(f"You guessed {guess},that's not in the word.You lose a life.")


    # if lives is equal to zero before the player guess the word the game will end and player will lose the game
    if lives==0:
      end_game=True
      print("\nYou Lost")


  # using join statement the "display" list will be displayed as string i.e; instead of ['_','_'] it will be displayed as _ _  .
  print(f"{' '.join(display)}")


  # if all blanks filled before the lives equal to 0 then game ends and the player will win .
  if "_" not in display:
    end_game=True
    print("\nYou Win")
  
  print(A.stages[lives])





 

    

    