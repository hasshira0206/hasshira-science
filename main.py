import pandas as pd
import numpy as np
import requests, json
import streamlit as st
st.write('エラーが出ていますが、気にしない。気にしない。')
def keisan(K,num):
    if K=='春分！' or '秋分！':
        x=90-num
    if K=='夏至！':
        x=90-num+23.4
    if K=='冬至！':
        x=90-num-23.4
    return x

st.title("南中高度計算君")
K = st.selectbox('何を計算しますか？',
                                    ['春分！',
                                     '秋分！',
                                     '夏至！',
                                     '冬至！',
                                     ])
postal = st.text_input(label='郵便番号を入力')
if st.checkbox("確定！"):
    url = 'http://geoapi.heartrails.com/api/json?method=searchByPostal&postal='
    res_dict = requests.get(url+postal).json()['response']['location'][0]
    st.write("{}ー{}ー{}ですねぇ？".format(res_dict['prefecture'],res_dict['city'],res_dict['town']))
    num=res_dict['y'].split('.')
    num=int(num[0])
    st.write(keisan(K,num),"度になります")
  
