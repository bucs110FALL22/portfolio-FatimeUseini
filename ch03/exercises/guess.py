import random
number_range= (1,2,3,4,5,6,7,8,9,10)
print("Number List:", number_range)
chosen_number= random.choice(number_range)
num=int(input("Enter a number between 1 and 10?:"))
if chosen_number=num:
  print("correct!")
elif  chosen_number >num:
  print("too low")
else chosen_number <num:
  print("too high")
