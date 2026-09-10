weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

height_in_meters = height / 100
BMI = weight / (height_in_meters ** 2)

print("Your BMI is:", BMI)

if BMI < 16:
    print("You are severely underweight.", BMI)

elif BMI >= 16 and BMI < 18.5:
    print("You are underweight.", BMI)

elif BMI >= 18.5 and BMI < 24:
    print("You are healthy.", BMI)

elif BMI >= 24 and BMI < 30:
    print("You are overweight.", BMI)

elif BMI >= 30:
    print("You are obese.", BMI)