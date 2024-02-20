height = float(input("Whats your height in m? "))

weight = int(input("Whats your weight in kg? "))

bmi = round(weight / height**2,2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}: Underweight")
elif 18.5 <= bmi <25:
    print(f"Your bmi is {bmi}: Normal weight")
elif 25 <= bmi <30:
    print(f"Your bmi is {bmi}: Overweight")
elif 30 <= bmi < 35:
    print(f"Your bmi is {bmi}: Obesity")
else:
    print(f"Your bmi is {bmi}: Clinical obesity")
