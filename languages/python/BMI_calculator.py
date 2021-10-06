# program to find th body mass index ,formula : weight/height^2
height= input("Enter your height in 'meters' : ")
weight=input("Enter your weight in 'kilo grams' :  ")
# here weight is convering into 'int' type where as height is converting in float  because by default the input assumes any value ant takes it as string  (here height should of type float only )  
BMI = round(int(weight)/float(height)**2)
if BMI<18.5:
  print(f"Your BMI is {BMI}.you are underweight")
elif BMI<25:
  print(f"Your BMI is {BMI}.you have normal weight")
elif BMI<30:
  print(f"Your BMI is {BMI}.you are overweight")
elif BMI<35:
  print(f"Your BMI is {BMI}.you are obese. ")
else:
  print(f"Your BMI is {BMI}.you are clinically obese")