# A string which is a mixture of letter and integer and special char from which find the largest even number from the available digit after removing the duplicates.
#  If an even number is not formed then return-1



n=input()
l=[i for i in n if i.isdigit()]
l=list(set(l))
l.sort()
for i in l:
  if int(i)%2==0:
    s=i
    l.remove(i)
    break
  else:
    pass
l.sort(reverse=True)   
l.append(s)
s="".join(l)
if int(s)%2==0:
  print(s)
else:
  print(-1)
