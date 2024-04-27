#import os

#リストファイルを削除
#os.remove('list.txt')

import streamlit as st
import pickle


f = open('./list.txt','rb')
list0 = pickle.load(f)
list1 = pickle.load(f)
list2 = pickle.load(f)
list3 = pickle.load(f)
list4 = pickle.load(f)
list5 = pickle.load(f)
list6 = pickle.load(f)
list7 = pickle.load(f)
list8 = pickle.load(f)


st.title(f"{list0[0]}/{list0[1]}")
st.title(f"{list0[2]}:{list0[3]} 登録")

st.header('1号')
st.subheader(f"  A: {list1[0]}")
st.subheader(f"  B: {list1[1]}")
st.subheader(f"  C: {list1[2]}")

st.header('2号')
st.subheader(f"  A: {list2[0]}")
st.subheader(f"  B: {list2[1]}")
st.subheader(f"  C: {list2[2]}")

st.header('3号')
st.subheader(f"  A: {list3[0]}")
st.subheader(f"  B: {list3[1]}")
st.subheader(f"  C: {list3[2]}")

st.header('4号')
st.subheader(f"  A: {list4[0]}")
st.subheader(f"  B: {list4[1]}")
st.subheader(f"  C: {list4[2]}")

st.header('5号')
st.subheader(f"  A: {list5[0]}")
st.subheader(f"  B: {list5[1]}")
st.subheader(f"  C: {list5[2]}")

st.header('6号')
st.subheader(f"  A: {list6[0]}")
st.subheader(f"  B: {list6[1]}")
st.subheader(f"  C: {list6[2]}")

st.header('7号')
st.subheader(f"  A: {list7[0]}")
st.subheader(f"  B: {list7[1]}")
st.subheader(f"  C: {list7[2]}")

st.header('8号')
st.subheader(f"  A: {list8[0]}")
st.subheader(f"  B: {list8[1]}")
st.subheader(f"  C: {list8[2]}")