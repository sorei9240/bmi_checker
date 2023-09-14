def bmi_calculator():
  height = float(input("What is your height in meters? "))
  weight = float(input("What is your weight in kilograms? "))
  bmi = weight/height**2
  rounded_bmi = round(bmi, 1)
  return rounded_bmi

def bmi_checker():
  bmi_value = bmi_calculator()
  while True:
    if bmi_value < 18.5:
      print(f"Your BMI of {bmi_value} indicates that you are underweight.")
    elif bmi_value > 18.5 and bmi_value < 25:
      print(f"Your BMI of {bmi_value} indicates that you are a healthy weight.")
    elif bmi_value > 25 and bmi_value < 30:
      print(f"Your BMI of {bmi_value} indicates that you are overweight.")
    else:
      print(f"Your BMI of {bmi_value} indicates that you are obese.")
    break

bmi_checker()