import pytesseract
from PIL import Image
import re
import streamlit as st
import numpy as np

rad = st.radio('입력방법을 선택하세요', options=['upload','use cam'])
if rad == 'use cam':
    picture = st.camera_input('사진촬영')
else:
    picture = st.file_uploader('파일을 선택하세요')

image = Image.open(picture)
st.image(image)
# 이미지 OCR
options = r"--psm 11 --oem 3 "
text = pytesseract.image_to_string(image, config=options,lang='eng+kor+equ')

# 수학 공식과 한글 추출
numbers = re.sub(r'[^0-9]',',',text)
numbers2 = numbers.split(',')
for i in numbers2:
    if (i=='') | (i=="") | (i==" ") | (i==' '):
        numbers2.remove(i)
    else:
        pass

for i in range(len(numbers2)):
    # try:
    numbers2[i] = float(numbers2[i])
    # except:
    #     pass
st.write('검색된 숫자')
st.write(numbers2)
numbers2 = np.array(numbers2)
st.header(f"이미지 내의 숫자 합계는 {format(numbers2.sum(),',')}입니다.")
st.header(f"이미지 내의 숫자 평균은 {format(numbers2.mean(),',')}입니다.")
st.header(f"이미지 내의 숫자 표준편차는 {format(np.std(numbers2),',')}입니다.")
st.header(f"이미지 내의 숫자 분산은 {format(np.var(numbers2),',')}입니다.")
