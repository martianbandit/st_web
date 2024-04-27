import streamlit as st
import pickle
import datetime

DIFF_JST_FROM_UTC = 9
date = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)

with st.form(key="1_form"):
    
    st.title('入力')
    
    st.subheader('1号')
    #テキストボックス
    tank1A= st.text_input('1-A')
    a1= st.checkbox("1-A")
    tank1B= st.text_input('1-B')
    b1= st.checkbox("1")
    tank1C= st.text_input('1-C')
    c1= st.checkbox("2")
     
    st.subheader('2号')
    #テキストボックス
    tank2A= st.text_input('2-A')
    tank2B= st.text_input('2-B')
    tank2C= st.text_input('2-C')
    
    st.subheader('3号')
    #テキストボックス
    tank3A= st.text_input('3-A')
    tank3B= st.text_input('3-B')
    tank3C= st.text_input('3-C')

    st.subheader('4号')
    #テキストボックス
    tank4A= st.text_input('4-A')
    tank4B= st.text_input('4-B')
    tank4C= st.text_input('4-C')
    
    st.subheader('5号')
    #テキストボックス
    tank5A= st.text_input('5-A')
    tank5B= st.text_input('5-B')
    tank5C= st.text_input('5-C')
    
    st.subheader('6号')
    #テキストボックス
    tank6A= st.text_input('6-A')
    tank6B= st.text_input('6-B')
    tank6C= st.text_input('6-C')
    
    st.subheader('7号')
    #テキストボックス
    tank7A= st.text_input('7-A')
    tank7B= st.text_input('7-B')
    tank7C= st.text_input('7-C')
    
    st.subheader('8号')
    #テキストボックス
    tank8A= st.text_input('8-A')
    tank8B= st.text_input('8-B')
    tank8C= st.text_input('8-C')

    submit_btn = st.form_submit_button("送信")
    cancel_btn = st.form_submit_button("キャンセル")
 
if submit_btn:
    
    #リストファイルをつくる
    f = open('list.txt','wb')
    
    list0 = []
    list0.append(date.month)
    list0.append(date.day)
    list0.append(date.hour)
    list0.append(date.minute)
    
    
    list1 = []
    list1.append(tank1A)
    list1.append(tank1B)
    list1.append(tank1C)
    
    list2 = []
    list2.append(tank2A)
    list2.append(tank2B)
    list2.append(tank2C)
    
    list3 = []
    list3.append(tank3A)
    list3.append(tank3B)
    list3.append(tank3C)
    
    list4 = []
    list4.append(tank4A)
    list4.append(tank4B)
    list4.append(tank4C)

    list5 = []
    list5.append(tank5A)
    list5.append(tank5B)
    list5.append(tank5C)
    
    list6 = []
    list6.append(tank6A)
    list6.append(tank6B)
    list6.append(tank6C)
    
    list7 = []
    list7.append(tank7A)
    list7.append(tank7B)
    list7.append(tank7C)
        
    list8 = []
    list8.append(tank8A)
    list8.append(tank8B)
    list8.append(tank8C)
    
    #リストファイルを保存 
    pickle.dump(list0,f)   
    pickle.dump(list1,f)
    pickle.dump(list2,f)
    pickle.dump(list3,f)
    pickle.dump(list4,f)
    pickle.dump(list5,f)
    pickle.dump(list6,f)
    pickle.dump(list7,f)
    pickle.dump(list8,f)