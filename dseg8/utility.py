import os

# Function หาค่า BMI
def BMI_Calculator(weight, height):
    bmi = weight/((height/100) ** 2)

    return bmi

# Function อ่านผลของ BMI
def BMI_Result(bmi):
    if bmi < 18.50:
        return "ผอมไปหน่อย"
    elif (bmi >= 18.50 and  bmi <23):
        return "สุขภาพดี"
    elif (bmi >= 23 and  bmi < 25):
        return "ท้วมไปหน่อย"
    elif (bmi >= 25 and  bmi < 30):
        return "อ้วนไปหน่อย"
    elif (bmi >=30):
        return "อ้วนมากๆ"
