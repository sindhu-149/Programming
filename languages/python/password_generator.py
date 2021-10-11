#pypassword generator
import random

letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers=['0','1','2','3','4','4','6','7','8','9']

symbols=['!','#','$','%','^','&','*','@']

n_letters=int(input("How many number of letters would you like in your passwors?  " ))

n_numbers=int(input("How many numbers would you like?  "))

n_symbols=int(input("How many symbols would you like?  "))

password=""

for i in range(0,n_letters):
    password+=random.choice(letters)
    i+=1
for i in range(0,n_numbers):
  password+=random.choice(numbers)
  i+=1
for i in range(0,n_symbols):
  password+=random.choice(symbols)
  i+=1

#this statement will shuffle the password which was in the order  letters numbers symbols(gd123#$) to (2g#b1&w)
# random.sample(string_name,len(string)) will chooses multiple items with in the given string of defintine length.
# this will return a list even the argument passed is string.so to want o/p as a string we have to use join() method to concatenate
# join() method syntax: string_name.join(iterable)  //string_name - can be "" (empty) // iterable - like list,tuple,string
password="".join(random.sample(password,len(password)))

print(password)
