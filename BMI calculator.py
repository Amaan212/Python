height=float(input("Enter your Height in cm: "))
weight=float(input("Enter your weight in Kg: "))

BMI=weight / (height/100)**2
print("Your BMI is",BMI)
if BMI <= 18.4:
    print("You are Underweight")
elif BMI <= 24.9:
    print("You are Healthy")
elif BMI <= 29.9:
    print("You are Overweight")
elif BMI <= 34.9:
    print("You are Severly overweight")
elif BMI <= 39.9:
    print("You are obese")
else:
    print("You are Severly obese")
