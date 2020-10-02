import os

# Function หาค่า BMI
def BMI_Calculator(weight, height):
    bmi = weight/((height/100) ** 2)

    return bmi

# Function อ่านผลของ BMI
def BMI_Result(bmi):
    if bmi < 18.50:
        return "น้ำหนักน้อย/ผอม"
    elif (bmi >= 18.50 and  bmi <23):
        return "ปกติ(สุขภาพดี)"
    elif (bmi >= 23 and  bmi < 25):
        return "ท้วม/โรคอ้วนระดับ 1"
    elif (bmi >= 25 and  bmi < 30):
        return "อ้วน/โรคอ้วนระดับ 2"
    elif (bmi >=30):
        return "อ้วนมาก/โรคอ้วนระดับ 3"
