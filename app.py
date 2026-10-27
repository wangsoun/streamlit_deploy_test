import streamlit as st

if "n1" not in st.session_state:
    st.session_state.n1 = 1

st.write("# 처음으로 작성한 핸드폰용 st code")
b1 = st.button("카운터 1부터 증가")
b999 = st.button(" 카운터 리셋")

if b1:
    st.session_state.n1 += 1
if b999:
    st.session_state.n1 = 1

st.write(f'카운터1= {st.session_state.n1}')
