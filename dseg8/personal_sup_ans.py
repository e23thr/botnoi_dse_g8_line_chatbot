import json
import pandas as pd
from dseg8.gsheets import GoogleSheet, SHEET_PERSONAL_SUPPLEMENTS





def Get_Personal_sup_ans(lineID):

    ans_file = open('personal_sup_q.json', 'rb')
    _answer = json.load(ans_file)
    ps = GoogleSheet(SHEET_PERSONAL_SUPPLEMENTS)
    ps.df.fillna("")
    ans_data = ps.df.loc[ps.df.lineId == lineID]
    # print(ans_data)
    # ans_data = ps.df.loc[ans_data]
    if len(ans_data) == 0:
        raise Exception("Cannot find lineID {}".format(lineId))
    ## MapAge
    if(int(ps.df.loc[ans_data,"อายุ"])>=40 and ps.df.loc[ans_data,'เพศ']=="ชาย"):
        map_age=["วิตามินบีรวม","โสมทะเลทราย"]
    elif(int(ps.df.loc[ans_data,"อายุ"])>=40 and ps.df.loc[ans_data,'เพศ']=="หญิง"):
        map_age=[]
    ## Suncream
    if(str(ps.df.loc[ans_data,"การตากแดด"])=="มากกว่า 20 นาที"):
        if(ps.df.loc[ans_data,'ใช้ครีมกันแดด']=="ไม่ได้ทาเลย"):
           map_sunCream=["วิตามินบีรวม","โสมทะเลทราย"]
        elif(ps.df.loc[ans_data,'ใช้ครีมกันแดด']=="ไม่ได้ทาเลย" or ps.df.loc[ans_data,"ใช้ครีมกันแดด"]=="ไม่พบข้อมูล"):
           map_sunCream=[]


    #Map Ans
    answer_list = list(set(
        map_age+
        _answer["การออกกำลังกาย/ต่อสัปดาห์"][ps.df.loc[ans_data,"การออกกำลังกาย/ต่อสัปดาห์"]]+
        _answer["โซนที่พักอาศัย"][ps.df.loc[ans_data,"โซนที่พักอาศัย"]]+
        #map_sunCream+
        _answer["การดื่มแอลกอฮอล์"][ps.df.loc[ans_data,"การดื่มแอลกอฮอล์"]]+
        _answer["ปริมาณการทานผักผลไม้"][ps.df.loc[ans_data,"ปริมาณการทานผักผลไม้"]]+
        _answer["ประเภทอาหารที่ทานประจำ"][ps.df.loc[ans_data,"ประเภทอาหารที่ทานประจำ"]]+
        _answer["จำนวนครั้งที่ทานปลาทะเลต่อสัปดาห์"][ps.df.loc[ans_data,"จำนวนครั้งที่ทานปลาทะเลต่อสัปดาห์"]]+
        _answer["คำแนะนำเรื่องการเสริมธาตุเหล็กจากคุณหมอ"][ps.df.loc[ans_data,"คำแนะนำเรื่องการเสริมธาตุเหล็กจากคุณหมอ"]]+
        _answer["อยากดูแลด้านไหนเป็นพิเศษ"][ps.df.loc[ans_data,"special1"]]+
        _answer["อยากดูแลด้านไหนเป็นพิเศษ"][ps.df.loc[ans_data,"special2"]]+
        _answer["อยากดูแลด้านไหนเป็นพิเศษ"][ps.df.loc[ans_data,"special3"]]
    ))

    return answer_list

# print(Get_Personal_sup_ans("U90eedeb88d0c990cfa053c9c19a6d97cU90eedeb88d0c990cfa053c9c19a6d97c"))
