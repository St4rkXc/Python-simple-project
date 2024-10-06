import random
flag = True
while flag :
    num = input("type a number")
    if num.isdigit():
        print("lets go")
        num = int(num)
        flag = False
    else :
      print("Invalid input, Try Again")

secret = random.randint(1,num)
guess = None
count = 1

while guess != secret:
   guess = input("Please type a number between 1 and " + str(num + ": ") )
   if guess.isdigit():
      guess = int(guess)
      