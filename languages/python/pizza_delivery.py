print("Welcome to Python Pizza Deliveries!")
size=input("What size of pizza do you want?S,M or L?")
#initally bill is equal to 0
bill=0
if size=="S":
 bill+=15
elif size=="M":
  bill+=20
elif size=="L":
  bill+=25
add_pepper=input("Would you like to add pepper? Y or N ? ")
if add_pepper=="Y":
  if size=="S":
    bill+=2
  else:
    bill+=3
extra_cheese=input("Do you want to add extra cheese? Y or N ? ")
if extra_cheese=="Y":
  bill+=1
print(f"your total bill is ${bill}")