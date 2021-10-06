print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
print("Welcome to the Tressure Island. ")
print("Your metion is to find the treasure")
first_step=input('You\'re at a cross road.Where do you want to go?Type "left" or "right"?').lower()
# lower() is used because the user may type Right or right or RIGHT,this function is coverts any of this in lower  
if first_step=="left":
  second_step=input('You come to lake.There is an island in the middle of the lake.Type "wait" to wait for a boat.Type "swim" to swim across. ').lower()
  if second_step=="wait":
    third_step=input('you arrive at thr island unharmed.There is a house with 3 doors.One red,one yellow and one blue.Which color do you choose. ').lower()
    if third_step=="yellow":
      print("You Win!")
    else:
      print("Game Over.")
  else:
    print("You have caught by crocodile. Game Over. ")
else:
  print("You have fallen into ditch. Game Over. ")