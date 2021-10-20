# def prime(number):
#   is_prime=True
#   for i in range(2,number):
#     if number%i==0:
#       is_prime=False
#   if is_prime:
#     print("prime")
#   else:
#     print("not prime")

def is_prime(num):

  if num>1:

    for i in range(2,num):
      if num%i==0:
        print(f" {num} is not a prime number")
        break
    else:
      print(f"{num} is a prime number")

  else:
    print(f"{num} is not a prime number")

n=int(input("Enter number: "))

is_prime(n)
