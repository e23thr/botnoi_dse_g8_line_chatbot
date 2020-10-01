import os

# Function หาค่า BMI
def BMI_Calculator(weight, height):
    bmi = weight/((height/100) ** 2)

    return bmi
