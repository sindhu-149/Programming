# remove special charecters from string and if there are even no.of special charecters then output should print the series starting with even followed by odd numbers if no. of special charecters or odd vise versa
def conc(a,b):
  i=0
  s=""
  while True:
    if i<len(a):
      s+=a[i]
    if i<len(b):
      s+=b[i]
    i+=1
    if i>max(len(a),len(b)):
      break
  return s
n=input()
n=list(n)
count=0
even=[]
odd=[]
for i in range(len(n)):
  # instead of counting specail char we are counting no. of alphabets and numbers.
  if n[i].isalnum():
    count+=1
  if n[i].isdigit():
    if int(n[i])%2==0:
      even.append(n[i])
    else:
      odd.append(n[i])
 
  
print(count)
print(even)
print(odd)
if count%2==0:
  print(conc(even,odd))
else:
  print(conc(odd,even))
   
  
