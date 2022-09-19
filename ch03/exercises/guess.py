import random
number_range= (1,2,3,4,5,6,7,8,9,10)
print("Number List:", number_range)
chosen_number= random.choice(number_range)
while True: 
  num=int(input("Enter a number between 1 and 10?:"))
  if chosen_number==num:
    print("correct!")
    break
  elif  chosen_number>num:
    print("too low")
    continue
  elif chosen_number<num:
    print("too high")
    continue