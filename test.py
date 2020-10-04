from dseg8.gsheets import GoogleSheet, SHEET_TEST

# max_id = 10
# print("Name{}".format(max_id+1))

sheet = GoogleSheet(SHEET_TEST)

# (ถ้าจำเป็น) เปลี่ยน type ของแต่ละ column ให้ถูกต้องนะครับ เพราะว่าอ่านจาก googlesheet แบบนี้แล้วจะได้ column type = Object ทั้งหมดครับ
print(sheet.df.info())
sheet.df = sheet.df.astype({"id": int})
print(sheet.df.info())
max_id = sheet.df['id'].max()
next_id = max_id + 1
next_name = "Name{}".format(next_id)
sheet.df = sheet.df.append(
    {"id": next_id, "name": next_name}, ignore_index=True)
print(sheet.df)

# to update
# sheet.df.loc[sheet.df.id == "1", "name"] = "test"

print(sheet.df)
sheet.save()  # save data
