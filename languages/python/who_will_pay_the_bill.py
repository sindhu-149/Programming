
import random
names=input("Give me everybody's names seperated by comma.  ")
#splits input strings (names) into list
name=names.split(",")
# to find the no. of elements enetered
number_of_choices=len(name)
#to select a person
choice=random.randint(0,number_of_choices -1)
name_of_the_person=name[choice]
print(name_of_the_person + " is going to pay the meal today! ")
# we can also achieve this by simple using choice() method
# random.choice(name)