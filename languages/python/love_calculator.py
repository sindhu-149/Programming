print("Welcome to the love calculator")
name1=input("what is your name? ")
name2=input("what is their name? ")
name1=name1.lower()
name2=name2.lower()
name=name1+name2
true=0
true+=name.count("t")
true+=name.count("r")
true+=name.count("u")
true+=name.count("e")
love=0
love+=name.count("l")
love+=name.count("o")
love+=name.count("v")
love+=name.count("e")
score=str(true)+str(love)
score=int(score)
if score<10 or score>90:
  print(f"your score is {score},you go together like coke and mentos")
elif score>40 and score<50:
  print(f"your score is {score},you are alright together")
else:
  print(f"your score is {score}")