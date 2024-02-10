# Bmi Calculator 2.0

height = input("Please enter your height in m: ")

weight = input("Please input weight in KG: ")

weightint = int(weight)

heightflt = float(height)

bmi = (weightint) / (heightflt)**2

if bmi < 18.2678 :
    print(f"Your BMI is {bmi}. You are underweight")
elif bmi < 22.0:
    print(f"Your BMI is {bmi}. You are normal weight")
elif bmi < 28.50752:
    print(f"Your BMI is {bmi}. You are silghtly overweight")
elif bmi < 32.56189:
    print(f"Your BMI is {bmi}. You are obese")
else:
    print(f"Your BMI is {bmi}. You are Clinically Obese") 

 