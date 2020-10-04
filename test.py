from dseg8.gsheets import GoogleSheet


sheet = GoogleSheet()

sheet.read_friends()
print(sheet.friends_pd)
print(type(sheet.friends_pd))
sheet.friends_pd = sheet.friends_pd.append(
    {"LineID": "b", "Name": "test"}, ignore_index=True)
sheet.write_friends()
