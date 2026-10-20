import streamlit as st

if "n1" not in st.session_state:
    st.session_state.n1 = 1
if"n2" not in st.session_state:
    st.session_state.n2 = 2
if "n3" not in st.session_state:
    st.session_state.n3 = 3
if "n4" not in st.session_state:
    st.session_state.n4 = 4

b1 = st.button("눌러 눌러, 1부터 시작")
b2 = st.button("눌러 눌러, 2부터 시작")
b3 = st.button("눌러 눌러, 3부터 시작")
b4 = st.button("눌러 눌러, 4부터 시작")
c = st.button("싹 지워!!")

if b1:
    st.session_state.n1 += 1
if b2:
    st.session_state.n2 += 1
if b3:
    st.session_state.n3 += 1
if b4:
    st.session_state.n4 += 1
if c:
    st.session_state.n1 = 1
    st.session_state.n2 = 2
    st.session_state.n3 = 3
    st.session_state.n4 = 4

st.write(f"버튼1: {st.session_state.n1}번 눌렀네!!!")
st.write(f"버튼2: {st.session_state.n2}번 눌렀네!!!")
st.write(f"버튼3: {st.session_state.n3}번 눌렀네!!!")
st.write(f"버튼4: {st.session_state.n4}번 눌렀네!!!")