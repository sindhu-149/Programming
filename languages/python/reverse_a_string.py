# reverse a string without changing the position of special charecters.
n=input()
d=dict()
n=list(n)
l=[]
for i in range(len(n)):
  if n[i].isalpha():
    l.append(n[i])
  else:
    d[i]=n[i]
l.reverse()
for i in d:
  l.insert(i,d[i])
s="".join(l)
print(s)
