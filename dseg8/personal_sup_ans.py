import json
import pandas as pd
from dseg8.gsheets import GoogleSheet, SHEET_PERSONAL_SUPPLEMENTS





def Get_Personal_sup_ans(lineID):

    ans_file = open('personal_sup_q.json', 'rb')
    _answer = json.load(ans_file)
    ps = GoogleSheet(SHEET_PERSONAL_SUPPLEMENTS)
    ps.df.fillna("")
    ans_data = ps.df.loc[ps.df.lineId == lineID]

    if len(ans_data) == 0:
        raise Exception("Cannot find lineID {}".format(lineId))
    ## MapAge
    if(int(ans_data.iloc[0]["อายุ"])>=40 and ans_data.iloc[0]['เพศ']=="ชาย"):
        map_age=["วิตามินบีรวม","โสมทะเลทราย"]
    elif(int(ans_data.iloc[0]["อายุ"])>=40 and ans_data.iloc[0]['เพศ']=="หญิง"):
        map_age=[]
    ## Suncream
    if(str(ans_data.iloc[0]["การตากแดด"])=="มากกว่า 20 นาที"):
        if(ans_data.iloc[0]['ใช้ครีมกันแดด']=="ไม่ได้ทาเลย"):
           map_sunCream=["วิตามินบีรวม","โสมทะเลทราย"]
        elif(ans_data.iloc[0]['ใช้ครีมกันแดด']=="ไม่ได้ทาเลย" or ans_data.iloc[0]["ใช้ครีมกันแดด"]=="ไม่พบข้อมูล"):
           map_sunCream=[]


    #Map Ans
    answer_list = list(set(
        map_age+
        _answer["การออกกำลังกาย/ต่อสัปดาห์"][ans_data.iloc[0]["การออกกำลังกาย/ต่อสัปดาห์"]]+
        _answer["โซนที่พักอาศัย"][ans_data.iloc[0]["โซนที่พักอาศัย"]]+
        #map_sunCream+
        _answer["การดื่มแอลกอฮอล์"][ans_data.iloc[0]["การดื่มแอลกอฮอล์"]]+
        _answer["ปริมาณการทานผักผลไม้"][ans_data.iloc[0]["ปริมาณการทานผักผลไม้"]]+
        _answer["ประเภทอาหารที่ทานประจำ"][ans_data.iloc[0]["ประเภทอาหารที่ทานประจำ"]]+
        _answer["จำนวนครั้งที่ทานปลาทะเลต่อสัปดาห์"][ans_data.iloc[0]["จำนวนครั้งที่ทานปลาทะเลต่อสัปดาห์"]]+
        _answer["คำแนะนำเรื่องการเสริมธาตุเหล็กจากคุณหมอ"][ans_data.iloc[0]["คำแนะนำเรื่องการเสริมธาตุเหล็กจากคุณหมอ"]]+
        _answer["อยากดูแลด้านไหนเป็นพิเศษ"][ans_data.iloc[0]["special1"]]+
        _answer["อยากดูแลด้านไหนเป็นพิเศษ"][ans_data.iloc[0]["special2"]]+
        _answer["อยากดูแลด้านไหนเป็นพิเศษ"][ans_data.iloc[0]["special3"]]
    ))

    return answer_list

# print(Get_Personal_sup_ans("U90eedeb88d0c990cfa053c9c19a6d97cU90eedeb88d0c990cfa053c9c19a6d97c"))
