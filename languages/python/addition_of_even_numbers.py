#To add all even numbers from 1 to 100
sum=0
# range(start value,end_value,step_size(no.of steps to jump))
# here start value is 0 because if we start with 1 and it jumps to 3 which is add no. when 0 it jumps to 2 or we can start with 2
# end_value is 101 because we want to include 100 also if end value is 100 the it will consider upto 99 only
for i in range(0,101,2):
  sum+=i
print(sum)