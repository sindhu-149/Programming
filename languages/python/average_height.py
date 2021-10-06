student_height=input("Enter a list of student's heights ").split( )
for height in range(0,len(student_height)):
  student_height[height]=int(student_height[height])
# finding total sum of heights without using sum() function
sum=0
for height in range(0,len(student_height)):
  sum+=student_height[height]
# finding total no. of students height inn list without using len() function
total_students=0
for n in range(0,len(student_height)):
  total_students+=1
average=round(sum/total_students)
print(f"Average height of students : {average}")