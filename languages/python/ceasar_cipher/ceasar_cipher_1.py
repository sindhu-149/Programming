alphabets= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
execute=input("Type 'encode' to encrypt , type 'decode' to decrypt \n")

text=input("Enter you message \n").lower()
shift=int(input("Type the shift number \n"))

def encrypt(text,shift):

  cipher_text=""

  for i in text:
    # hence the alphabets list had duplicate letters,the index() will give the 1st index value of a letter that it find.
    position=alphabets.index(i)
    cipher_text+=alphabets[position+shift]
  print(cipher_text)

def decrypt(text,shift):

  cipher_text=""

  for letter in text:
    position=alphabets.index(letter)
    new_position=position-shift
    cipher_text+=alphabets[new_position]
  print(cipher_text)

  
if execute=="encode":
  encrypt(text,shift)
else:
  decrypt(text,shift)