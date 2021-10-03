print("Welcome to the tip calculator") 
bill=float(input("what was the total bill?: "))     
percentage_of_tip=float(input("what percentage tip would you like to give?10, 12 or 15?: ")) 
# caclulating tip amount and adding it to bill 
bill_with_tip=bill*(percentage_of_tip/100)+bill 
# bill_with_tip=bill*(1+12/100)  this will also give same result 
tot_members=int(input("How many peope to split the bill?")) 
amount=bill_with_tip/tot_members 
print(round(amount,2))