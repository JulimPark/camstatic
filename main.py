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
    try:
        numbers2[i] = float(numbers2[i])
    except:
        numbers2.remove(numbers2[i])
        
st.header('검색된 숫자 목록')
st.write(numbers2)
numbers2 = np.array(numbers2)
st.header(f'검색된 숫자의 개수는 :red[{len(numbers2)}개] 입니다.')
st.subheader(f":green[합계]: :blue[{format(numbers2.sum(),',')}]")
st.subheader(f":green[평균]: :blue[{format(numbers2.mean(),',')}]")
st.subheader(f":green[표준편차]: :blue[{format(np.std(numbers2),',')}]")
st.subheader(f":green[분산]: :blue[{format(np.var(numbers2),',')}]")
st.warning(':red[컴퓨터 비전 기술로 읽은 데이터에 대한 통계입니다. 인식환경에 따라 오차가 발생할 수 있으니 주의하시기 바랍니다.]')
