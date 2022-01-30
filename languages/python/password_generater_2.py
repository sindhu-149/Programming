'''
   Given input of array of string in format <emnp name> <emp number> separated by comas ,Emp
should contain only alphabets and employee number. You have to generate password for
Ex:
input: Robert: 36787, Tina: 68721, Jo:56389
Output: tiX
Conditions: len of robert is 6 and 6 is present in emp number
robert (36787), so return the alphabet at position 6 that is t.
Now len of tina is 4 and 3 is not present in the 68721 so select the number which is max and less than the len of tina so select 2 return the alphabet that is at position 2 that is i.
Now In of Jo is 2 it is not present in 56389 and there is not present any number which is less than 2 so return X.

'''


'''python
n=input().split(",")
print(n)
name=[]
id=[]
for i in n:
  x,y=i.split(":")
  name.append(x)
  id.append(y)
print(name)
print(id)
# password generating
password=""
for i in range(len(name)):
    length=len(name[i])
    l=[int(j) for j in id[i]]
    if length in l:
      password+=name[i][-1]
    elif length not in l:
      m=[]
      for k in l:
        if k<length:
          m.append(k)
      if len(m)!=0:
          password+=name[i][max(m)-1]
      else:
          password+="X"
print(password)

'''
