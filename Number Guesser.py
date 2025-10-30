import random
r = random.randint(1,30)
input=int(input("Enter a Number between 1-30."))
if r==21:
    print("You are correct!")
else:
    print("Your answer is false")
    print("Hint! It is a multiple of 7.")
