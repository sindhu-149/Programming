import os

# function to clear the console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

secret_auction={}

# to find the winner
def find_winner(secret_auction):
  max=0
  for key in secret_auction:
    if max < secret_auction[key]:
      max = secret_auction[key]
      winner=key
  clearConsole()    
  print(f"The Winner is {winner} with a bid of ${max}.") 

Auction_start = True

while Auction_start==True:
  key=input("What is your name? ")
  value=int(input("What's your bid? $"))
  secret_auction[key]=value
  members=input("Are there any other bidders ? Type 'Yes' or 'No' :  ").lower()
  if members=="yes":
    Auction_start = True
    clearConsole()
  else:
    Auction_start = False
   
find_winner(secret_auction)


