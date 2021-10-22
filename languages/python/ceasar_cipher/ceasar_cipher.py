import ceasar_art as art

alphabets= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

start=True

while start==True:
  execute=input("Type 'encode' to encrypt , type 'decode' to decrypt \n")
  text=input("Enter you message \n").lower()
  shift=int(input("Type the shift number \n"))
  shift=shift%26


  def ceasar(message,shift_amount,execute):
  
    cipher_text=""
 
    # if user want to decode then this if statement will execute else jumps to for loop.
    if execute=="decode":
      shift_amount*=-1
  
    for letter in message:
      # if 'letter' is an alhpabet it satisfies if condition and executes
      if letter in alphabets:
        position=alphabets.index(letter)
        new_position=position+shift_amount
        cipher_text+=alphabets[new_position]
      # if 'letter' contains numbers , symbols or white spaces there will be added at the same postion without any decoding/encoding 
      else:
        cipher_text+=letter
    print(f"Here's the {execute} result: {cipher_text}")

  ceasar(text,shift,execute)

  run_again=input("Type 'Yes' if you want to code again.otherwise type 'No' \n").lower()
  if run_again=="no":
    start=False
    print("Good Bye")

