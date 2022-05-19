# 스트림릿 라이브러리를 사용하기 위한 임포트
from turtle import st


import streamlit as st
st

# 웹 대시보드 개발 라이브러리인 스트림릿은
# main 함수가 있어야 한다

def main() :
    st.title('안녕하세요, 웹 대시보드 프로젝트')
    st.title('hello')

if __name__=='__main__' :
    main()



import streamlit as st

def main() :
    st.title('웹 대시보드')
    st.text('웹 대시보드 개발하기')
    name = '홍길동'
     # 제 이름은 홍길동 입니다.
     '제 이름은 {}입니다.'.format(name)
if __name__=='__main__' :
    main()


import steamlit as st
import pandas as pd
def main() :
    df = pd.read_csv('data2/iris.csv')
    print(df)

if

