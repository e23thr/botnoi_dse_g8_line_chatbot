import json
from flask_restful import Resource
from flask import request
from dseg8.gsheets import GoogleSheet, SHEET_PERSONAL_SUPPLEMENTS


ans_file = open('personal_sup_q.json', 'rb')
_answer = json.load(ans_file)



def Get_Personal_sup_ans(ans_data):

    ## MapAge
    if(ans_data["อายุ"]>=40 and ans_data["เพศ"]=="ชาย"):
        map_age=["วิตามินบีรวม","โสมทะเลทราย"]
    elif(ans_data["อายุ"]>=40 and ans_data["เพศ"]=="หญิง"):
        map_age=[]    
    ## Suncream
    if(ans_data["การตากแดด"]=="มากกว่า 20 นาที" and ans_data["ใช้ครีมกันแดด"]=="ไม่ได้ทาเลย"):
        map_sunCream=["วิตามินบีรวม","โสมทะเลทราย"]
    elif(ans_data["การตากแดด"]=="มากกว่า 20 นาที" and (ans_data["ใช้ครีมกันแดด"]=="ไม่ได้ทาเลย" or ans_data["ใช้ครีมกันแดด"]=="ไม่พบข้อมูล" )):
        map_sunCream=[]    


    answer_list = list(set(
        map_age+
        _answer["การออกกำลังกาย/ต่อสัปดาห์"][ans_data["การออกกำลังกาย/ต่อสัปดาห์"]]+
        _answer["โซนที่พักอาศัย"][ans_data["โซนที่พักอาศัย"]]+
        map_sunCream+
        _answer["การดื่มแอลกอฮอล์"][ans_data["การดื่มแอลกอฮอล์"]]+
        _answer["ปริมาณการทานผักผลไม้"][ans_data["ปริมาณการทานผักผลไม้"]]+
        _answer["ประเภทอาหารที่ทานประจำ"][ans_data["ประเภทอาหารที่ทานประจำ"]]+
        _answer["จำนวนครั้งที่ทานปลาทะเลต่อสัปดาห์"][ans_data["จำนวนครั้งที่ทานปลาทะเลต่อสัปดาห์"]]+
        _answer["คำแนะนำเรื่องการเสริมธาตุเหล็กจากคุณหมอ"][ans_data["คำแนะนำเรื่องการเสริมธาตุเหล็กจากคุณหมอ"]]+
        _answer["อยากดูแลด้านไหนเป็นพิเศษ"][ans_data["special1"]]+
        _answer["อยากดูแลด้านไหนเป็นพิเศษ"][ans_data["special2"]]+
        _answer["อยากดูแลด้านไหนเป็นพิเศษ"][ans_data["special3"]]        
    ))
    
    return answer_list

