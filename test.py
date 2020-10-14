from dseg8.personal_sup_ans import Get_Personal_sup_ans

value = Get_Personal_sup_ans("Ua82605f32017a095c6a5e88839853bcc")
print(type(value))
print(value)
#  import json
# import pandas as pd
# from dseg8.gsheets import GoogleSheet, SHEET_PERSONAL_SUPPLEMENTS
# lineID = "Ua82605f32017a095c6a5e88839853bcc"
# ps = GoogleSheet(SHEET_PERSONAL_SUPPLEMENTS)
# ps.df.fillna("")
# ans_data = ps.df.loc[ps.df.lineId == lineID]
# # print(type(ans_data))
# # print(ans_data)
# print(ans_data.iloc[0]["อายุ"])
# from dseg8.gsheets import GoogleSheet, SHEET_TEST

# # max_id = 10
# # print("Name{}".format(max_id+1))

# sheet = GoogleSheet(SHEET_TEST)

# # (ถ้าจำเป็น) เปลี่ยน type ของแต่ละ column ให้ถูกต้องนะครับ เพราะว่าอ่านจาก googlesheet แบบนี้แล้วจะได้ column type = Object ทั้งหมดครับ
# print(sheet.df.info())
# sheet.df = sheet.df.astype({"id": int})
# print(sheet.df.info())
# max_id = sheet.df['id'].max()
# next_id = max_id + 1
# next_name = "Name{}".format(next_id)
# sheet.df = sheet.df.append(
#     {"id": next_id, "name": next_name}, ignore_index=True)
# print(sheet.df)

# # to update
# # sheet.df.loc[sheet.df.id == "1", "name"] = "test"

# print(sheet.df)
# sheet.save()  # save data
