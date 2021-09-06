height = float(input(" enter your height (in m): "))
weight = float(input("enter your weight in kgs: "))

BMI = weight / height**2

if BMI > 35:
    print("clinically obese")
elif 30 < BMI < 35:
    print("obese")
elif 25 < BMI < 30:
    print("overweight")
elif 18.5 < BMI < 25:
    print("normal weight")
elif BMI < 18.5:
    print("underweight")
