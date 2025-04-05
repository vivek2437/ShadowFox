# 1. Write a program to determine the BMI Category based on user input.
# Ask the user to:
# Enter height in meters
# Enter weight in kilograms
# Calculate BMI using the formula: BMI = weight / (height)2
# Use the following categories:
# If BMI is 30 or greater, print "Obesity"
# If BMI is between 25 and 29, print "Overweight"
# If BMI is between 18.5 and 25, print "Normal"
# If BMI is less than 18.5, print "Underweight"

print("Enter your height in meters:")
height = float(input())
print("Enter your weight in kilograms:")
weight = float(input())

bmi = weight / (height ** 2)
print("Your BMI is:", bmi)

if(bmi >= 30):
    print("Obesity")
elif(bmi >= 25):
    print("Overweight")
elif(bmi >= 18.5):
    print("Normal")
else:
    print("Underweight")
    
