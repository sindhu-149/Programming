#Rock Paper Scissors Game
import random
print("Welcome to Rock Paper and Scissors ")

Rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
Scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
images=[Rock, Paper, Scissors]
user_choose=int(input("What do you want to choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
if user_choose>2 or user_choose<0:
  print("You have entered an invalid number. You lose!")
else:
  print("You choose\n")
  print(images[user_choose])
  computer_choose=random.randint(0,2)
  if user_choose==2 and computer_choose==0:
    print("computer choose:\n")
    print(images[computer_choose])
    print("\nYou lose")
  elif user_choose==0 and computer_choose==2:
    print("computer choose:\n")
    print(images[computer_choose])
    print("\nYou Won")
  elif computer_choose>user_choose:
    print("computer choose:\n")
    print(images[computer_choose])
    print("\nYou lose")
  elif user_choose>computer_choose:
    print("computer choose:\n")
    print(images[computer_choose])
    print("\nYou won")
  elif computer_choose==user_choose:
    print("computer choose:\n")
    print(images[computer_choose])
    print("\nIt's a draw")
