from scipy.spatial.distance import cosine
import pandas as pd
import numpy as np

answer_array = np.array([
    'โปรตีน ช่วยซ่อมแซมส่วนที่สึกหรอ สร้างกล้ามเนื้อ',
    'วิตามินเกลือแร่รวมและไฟโตนิวเทรียนท์',
    'สารต้านอนุมูลอิสระ ช่วยกำจัดสารพิษต่างๆ',
    'น้ำมันปลา บำรุงสมอง สายตา ผิวพรรณ',
    'ใยอาหาร ช่วยเรื่องการขับถ่าย จากการทานผักผลไม้ไม่พอ',
    'วิตามินดี กระดูกแข็งแรง',
    'วิตามินซี เสริมภูมิคุ้มกัน แก้หวัด',
    'วิตามินบีรวม ให้คุณมีพลังงานตลอดทั้งวัน',
    'บำรุงกระดูก เช่น แคลเซียม วิตามินดี',
    'บำรุงข้อต่อ เช่น กลูโคซามีน คอนดอยติน',
    'บำรุงสมอง เช่น น้ำมันปลา',
    'บำรุงลำไส้ การย่อยอาหาร เช่น โปรไบโอติกส์ เอนไซม์ช่วยย่อย',
    'ช่วยเพิ่มพลังงาน เช่น วิตามินบี โสมไซบีเรีย',
    'บำรุงสายตา เช่น เบต้าแคโรทีน ลูทีนซีแซนทีน',
    'เพิ่มสมาธิและความจำ เช่น ซีสแทนเซ',
    'บำรุงหัวใจ เช่น กระเทียม โคคิวเท็น สารสกัดจากชาเขียว',
    'ภูมิต้านทาน เช่น เอกไคนีเซีย วิตามินซี สารสกัดจากอบเชย',
    'บำรุงต่อมลูกหมาก เช่น Saw Palmetto and Nettle Root',
    'ช่วยเรื่องการนอน เช่น เมลาโทนิน',
    'ช่วยเรื่องความเครียด เช่น เวอราเรียน'
])

answer_df = pd.Series(answer_array)
pre_train_df = pd.read_csv('pre_train.csv', index_col=[0])


def answer_similarity_text(answer=''):
    return answer_df.iloc[0]


def answer_is_in_answer_array(answer=''):
    if answer in answer_array:
        return True
    else:
        return False


def recommendation(input_text, number=5):
    my_feature = pd.DataFrame(np.zeros((1, len(answer_df))), columns=answer_df)
    my_feature[input_text] = 3

    similarity = []
    close_to_uid = 0

    # ค้นหา similarity ว่าคล้ายกับ id ไหน
    for idx in range(len(pre_train_df)):
        similarity.append(1 - cosine(my_feature, pre_train_df.iloc[idx].values))
        similarity = pd.Series(similarity).fillna(0).tolist()
        close_to_uid = np.argsort(similarity)[-1]

    res = list(pre_train_df.T[close_to_uid].sort_values(ascending=False)[0:number].index)
    return res


def get_recommendation(input_text='', number_of_recommend=1):
    # สร้าง data frame เปล่าแล้วใส่ feature ลงไปเป็นคะแนน 3
    if answer_is_in_answer_array(input_text):
        print(recommendation(input_text, number_of_recommend))
    else:
        print(recommendation(answer_similarity_text(input_text), number_of_recommend))


# input เป็น คำตอบของ anna
# get_recommendation('ช่วยเรื่องการนอน เช่น เมลาโทนิน',5)
# get_recommendation('ตอบ มั่วๆ',5)
