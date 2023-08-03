import pytesseract
from PIL import Image
import re
import streamlit as st
import numpy as np

picture = st.camera_input('사진촬영')

image = Image.open(picture)

# 이미지 OCR
options = r"--psm 11 --oem 3 "
text = pytesseract.image_to_string(image, config=options,lang='eng+kor+equ')

# 수학 공식과 한글 추출
numbers = re.sub(r'[^0-9]',' ',text)
numbers2 = numbers.split(' ')
numbers2 = sorted(set(numbers2))
numbers2.remove('')
# print(text)
# # 결과 출력
# print('수학 공식:', formulas)
# print('한글:', hangul)
for i in range(len(numbers2)):
    numbers2[i] = float(numbers2[i])

st.write(numbers2)
numbers2 = np.array(numbers2)
st.header(f"이미지 내의 숫자 합계는 {format(numbers2.sum(),',')}입니다.")
st.header(f"이미지 내의 숫자 평균은 {format(numbers2.mean(),',')}입니다.")
st.header(f"이미지 내의 숫자 표준편차는 {format(np.std(numbers2),',')}입니다.")
st.header(f"이미지 내의 숫자 분산은 {format(np.var(numbers2),',')}입니다.")
