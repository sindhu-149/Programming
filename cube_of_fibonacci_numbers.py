# find cube of fibanacci numbers starting with 0 and using map and lambda functions and print out the list

cube = lambda x: x**3 

def fibonacci(n):
    a,b=0,1
    l=[]
    i=0
    while i<n:
        l.append(a)
        a,b=b,a+b
        i+=1
    return l
n = int(input())
print(list(map(cube, fibonacci(n))))
