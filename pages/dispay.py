#import os

#リストファイルを削除
#os.remove('list.txt')

import streamlit as st
import pickle
import datetime
import time

DIFF_JST_FROM_UTC = 9
now = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)

ut_now = time.time()

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

consumption_list = pickle.load(f)
hour_later_list =pickle.load(f)

v1a = pickle.load(f)
v1b = pickle.load(f)
v1c = pickle.load(f)
v2a = pickle.load(f)
v2b = pickle.load(f)
v2c = pickle.load(f)
v3a = pickle.load(f)
v3b = pickle.load(f)
v3c = pickle.load(f)
v4a = pickle.load(f)
v4b = pickle.load(f)
v4c = pickle.load(f)
v5a = pickle.load(f)
v5b = pickle.load(f)
v5c = pickle.load(f)
v6a = pickle.load(f)
v6b = pickle.load(f)
v6c = pickle.load(f)
v7a = pickle.load(f)
v7b = pickle.load(f)
v7c = pickle.load(f)
v8a = pickle.load(f)
v8b = pickle.load(f)
v8c = pickle.load(f)

list_start = pickle.load(f)

    

#登録時間
start = list_start[0]
#消費率
consumption_rate = consumption_list[0]
#x時間後
hour_later = hour_later_list[0]
#x時間後の日時
later_ = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC + hour_later_list[0])
#経過時間
progress = ((ut_now - start)/3600 )
#消費量
consumption = consumption_rate * (progress+hour_later)


entY = list0[0]
entm = list0[1]
entd = list0[2]
entH = list0[3]
entM = list0[4]







if hour_later >=20 :
    list1[0,0,0]
    list2[0,0,0]
    list3[0,0,0]
    list4[0,0,0]
    list5[0,0,0]
    list6[0,0,0]
    list7[0,0,0]
    list8[0,0,0]

#######
if any(v1a):
    lv1a = (list1[0] - consumption)
else:
    lv1a = list1[0]
lv1a = round(lv1a,2)   
if any(v1b):
    lv1b = (list1[1] - consumption)
else:
    lv1b = list1[1]
lv1b = round(lv1b,2) 
if any(v1c):
    lv1c = (list1[2] - consumption)
else:
    lv1c = list1[2]
lv1c = round(lv1c,2)


if any(v2a):
    lv2a = (list2[0] - consumption)
else:
    lv2a = list2[0]
lv2a = round(lv2a,2)   
if any(v2b):
    lv2b = (list2[1] - consumption)
else:
    lv2b = list2[1]
lv2b = round(lv2b,2) 
if any(v2c):
    lv2c = (list2[2] - consumption)
else:
    lv2c = list2[2]
lv2c = round(lv2c,2)

if any(v3a):
    lv3a = (list3[0] - consumption)
else:
    lv3a = list3[0]
lv3a = round(lv3a,2)   
if any(v3b):
    lv3b = (list3[1] - consumption)
else:
    lv3b = list3[1]
lv3b = round(lv3b,2) 
if any(v3c):
    lv3c = (list3[2] - consumption)
else:
    lv3c = list3[2]
lv3c = round(lv3c,2)  

if any(v4a):
    lv4a = (list4[0] - consumption)
else:
    lv4a = list4[0]
lv4a = round(lv4a,2)   
if any(v4b):
    lv4b = (list4[1] - consumption)
else:
    lv4b = list4[1]
lv4b = round(lv4b,2) 
if any(v4c):
    lv4c = (list4[2] - consumption)
else:
    lv4c = list4[2]
lv4c = round(lv4c,2)

if any(v5a):
    lv5a = (list5[0] - consumption)
else:
    lv5a = list5[0]
lv5a = round(lv5a,2)   
if any(v1b):
    lv5b = (list5[1] - consumption)
else:
    lv5b = list5[1]
lv5b = round(lv5b,2) 
if any(v5c):
    lv5c = (list5[2] - consumption)
else:
    lv5c = list5[2]
lv5c = round(lv5c,2)

if any(v6a):
    lv6a = (list6[0] - consumption)
else:
    lv6a = list6[0]
lv6a = round(lv6a,2)   
if any(v6b):
    lv6b = (list6[1] - consumption)
else:
    lv6b = list6[1]
lv6b = round(lv6b,2) 
if any(v6c):
    lv6c = (list6[2] - consumption)
else:
    lv6c = list6[2]
lv6c = round(lv6c,2)

if any(v7a):
    lv7a = (list7[0] - consumption)
else:
    lv7a = list7[0]
lv7a = round(lv7a,2)   
if any(v7b):
    lv7b = (list7[1] - consumption)
else:
    lv7b = list7[1]
lv7b = round(lv7b,2) 
if any(v7c):
    lv7c = (list7[2] - consumption)
else:
    lv7c = list7[2]
lv7c = round(lv7c,2)

if any(v8a):
    lv8a = (list8[0] - consumption)
else:
    lv8a = list8[0]
lv8a = round(lv8a,2)   
if any(v8b):
    lv8b = (list8[1] - consumption)
else:
    lv8b = list8[1]
lv8b = round(lv8b,2) 
if any(v8c):
    lv8c = (list8[2] - consumption)
else:
    lv8c = list8[2]
lv8c = round(lv8c,2)
######

#表示
col1, col2 = st.columns([2,5])
with col1:
    st.subheader(f"{list0[0]}/{list0[1]}/{list0[2]}")
    st.subheader(f"{list0[3]}:{list0[4]} 登録")

    st.subheader('---1号---')
    st.subheader(f"A : {list1[0]}{v1a[0]}")
    st.subheader(f"B : {list1[1]}{v1b[0]}")
    st.subheader(f"C : {list1[2]}{v1c[0]}")

    st.subheader('---2号---')
    st.subheader(f"A : {list2[0]}{v2a[0]}")
    st.subheader(f"B : {list2[1]}{v2b[0]}")
    st.subheader(f"C : {list2[2]}{v2c[0]}")

    st.subheader('---3号---')
    st.subheader(f"A : {list3[0]}{v3a[0]}")
    st.subheader(f"B : {list3[1]}{v3b[0]}")
    st.subheader(f"C : {list3[2]}{v3c[0]}")

    st.subheader('---4号---')
    st.subheader(f"A : {list4[0]}{v4a[0]}")
    st.subheader(f"B : {list4[1]}{v4b[0]}")
    st.subheader(f"C : {list4[2]}{v4c[0]}")

    st.subheader('---5号---')
    st.subheader(f"A : {list5[0]}{v5a[0]}")
    st.subheader(f"B : {list5[1]}{v5b[0]}")
    st.subheader(f"C : {list5[2]}{v5c[0]}")

    st.subheader('---6号---')
    st.subheader(f"A : {list6[0]}{v6a[0]}")
    st.subheader(f"B : {list6[1]}{v6b[0]}")
    st.subheader(f"C : {list6[2]}{v6c[0]}")

    st.subheader('---7号---')
    st.subheader(f"A : {list7[0]}{v7a[0]}")
    st.subheader(f"B : {list7[1]}{v7b[0]}")
    st.subheader(f"C : {list7[2]}{v7c[0]}")

    st.subheader('---8号---')
    st.subheader(f"A : {list8[0]}{v8a[0]}")
    st.subheader(f"B : {list8[1]}{v8b[0]}")
    st.subheader(f"C : {list8[2]}{v8c[0]}")
    st.subheader("======")
    
with col2:
    st.text(f"消費量{consumption_rate}/hで")
    if hour_later == 0:
        st.text(f"現在時刻 {later_.strftime('%H:%M')} の")
        st.text(f"予測値")
    else:
        st.text(f"今から{hour_later}時間後")
        st.text(f"{later_.strftime('%H:%M')}の予測値")

    st.subheader('-1号予測-')
    st.subheader(f"A : {lv1a}")
    st.subheader(f"B : {lv1b}")
    st.subheader(f"C : {lv1c}")
    st.subheader('-2号予測-')
    st.subheader(f"A : {lv2a}")
    st.subheader(f"B : {lv2b}")
    st.subheader(f"C : {lv2c}")
    st.subheader('-3号予測-')
    st.subheader(f"A : {lv3a}")
    st.subheader(f"B : {lv3b}")
    st.subheader(f"C : {lv3c}")
    st.subheader('-4号予測-')
    st.subheader(f"A : {lv4a}")
    st.subheader(f"B : {lv4b}")
    st.subheader(f"C : {lv4c}")
    st.subheader('-5号予測-')
    st.subheader(f"A : {lv5a}")
    st.subheader(f"B : {lv5b}")
    st.subheader(f"C : {lv5c}")
    st.subheader('---6号予測-')
    st.subheader(f"A : {lv6a}")
    st.subheader(f"B : {lv6b}")
    st.subheader(f"C : {lv6c}")
    st.subheader('-7号予測-')
    st.subheader(f"A : {lv7a}")
    st.subheader(f"B : {lv7b}")
    st.subheader(f"C : {lv7c}")
    st.subheader('-8号予測-')
    st.subheader(f"A : {lv8a}")
    st.subheader(f"B : {lv8b}")
    st.subheader(f"C : {lv8c}")



