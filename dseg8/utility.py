import os

# Function หาค่า BMI
def BMI_Calculator(weight, height):
    bmi = weight/((height/100) ** 2)

    return bmi

# Function อ่านผลของ BMI
def BMI_Result(bmi):
    if bmi < 18.50:
        return "น้ำหนักน้อยไปหน่อย"
    elif (bmi >= 18.50 and  bmi <23):
        return "น้ำหนักกำลังพอดีเลยคะ"
    elif (bmi >= 23 and  bmi < 25):
        return "น่าจะเริ่มท้วมๆ แล้วนะพี่ขา ดูแลสุขภาพหน่อย"
    elif (bmi >= 25 and  bmi < 30):
        return "อ้วนไปนิดนึงนะคะอันนาว่า ลดน้ำหนักสักหน่อย"
    elif (bmi >=30):
        return "พี่คะน้ำหนักพี่อยู่ในเกณฑ์เสี่ยงมากแล้วนะคะ รีบลดน้ำหนักด่วนเลย"
