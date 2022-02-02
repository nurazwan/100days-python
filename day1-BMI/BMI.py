while True:
    height=input('Please enter your height in cm: ')
    if height.isnumeric() == True:
        height=int(height)/100
        break

while True:
    weight=input('Please enter your weight in kg: ')
    if weight.isnumeric() == True:
        weight=int(weight)
        break

bmi = weight/(height**2)

def bmi_classification(bmi):
    if bmi < 18.5:
        return 'underweight'
    elif bmi >=18.5 and bmi < 25.0:
        return 'normal weight'
    elif bmi >= 25.0 and bmi < 30.0:
        return 'overweight'
    elif bmi >=30.0 and bmi < 35.0:
        return 'obese class I'
    elif bmi >=35.0 and bmi < 40.0:
        return 'obese class II'
    else:
        return 'obese class III'

print(f'Your BMI is {round(bmi,2)}.\nYou are {bmi_classification(bmi)}.')
