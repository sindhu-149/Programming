# print no.'s from 1 to 100
for number in range(1,101):
  # if no divisible by both 3 and 5 the print "FizzBuzz"
  if(number%3==0 and number%5==0):
    print("FizzBuzz")
  # if no. divisible by 3 then print "Fizz"
  elif number%3==0:
    print("Fizz")
  # if no. divisible by 5 then print "Buzz"
  elif number%5==0:
    print("Buzz")
  # else print number
  else:
    print(number)