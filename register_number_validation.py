# Register number validation
# There will be N test cases 
# register no. is of size 10
# cond 1:first values should be in range between 10 -22 both inclusive
# cond 2:next 2 values should be alphanumeric (3rd value should be char in upper case and 4th value should be a digit in range 0-9 )
# cond 3:5th value should be a digit in range between 0-9 both inclusive
# cond 4:6th charecter should be ie, A,B,C,D.
# cond 5:next 2 value should range between 01-19 both inclusive
# cond 6:9th value can be an alphabet of upper case or a digit in range 0-9
# cond 7:10th value should be a number in range 0-9


test_cases=int(input())
while(test_cases>0):
  reg=input()
  if int(reg[0:2]) in range(10,23):
    if reg[2:4].isalnum and reg[2:4].isupper():
      if int(reg[4]) in range(0,10):
        if reg[5] in ['A','B','C','D']:
          if (int(reg[6]) in range(0,2))and (int(reg[7]) in range(0,10)):
            if (reg[8].isalpha()) and (reg[8].isupper()) or (int(reg[8]) in range(0,10)):
              if int(reg[9]) in range(0,10):
                print("Valid")
              else:
                print("Invalid")  
            else:
              print("Invalid")    
          else:
            print("Invalid")  
        else:
          print("Invalid")     
      else:
        print("Invalid")       
    else:
      print("Invalid")        
  else:
    print("Invalid")
  test_cases-=1
