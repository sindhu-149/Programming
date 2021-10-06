# program to find th body mass index ,formula : weight/height^2
height= input("Enter your height in meters: ")
weight=input("Enter your weight in kilo grams:  ")
# here weight is convering into 'int' type where as height is converting in float  because by default the input assumes any value ant takes it as string  (here height should of type float only )  
BMI = int(weight)/float(height)**2
# converting BMI into 'int' gives the round values
print(int(BMI))
