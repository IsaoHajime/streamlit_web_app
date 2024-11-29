import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import common

common.check_login()

df_dset = st.session_state.dashbord_usersetting

if  str(df_dset.iloc[0,6]) == "True":

    
    st.subheader('【横浜 平均気温】')

    df = pd.read_csv('./data/平均気温.csv', index_col='年月')
    if  str(df_dset.iloc[0,14]) == "True":
        st.line_chart(df)
        
    if  str(df_dset.iloc[0,15]) == "True":
        st.bar_chart(df['月平均'])
        


    # matplotlib
    if  str(df_dset.iloc[0,16]) == "True":
        fig, ax = plt.subplots()
        ax.plot(df.index, df['月平均'])
        ax.set_title('matplotlib Graph')
        st.pyplot(fig)
else:
    # 画像
    image = Image.open('./data/pose_yubisashi_kakunin_sagyouin_man.PNG')
    st.image(image, width=200)
    st.text('申し訳けありません、いまの権限ではグラフ表示ができません。\n'
            '設定値の確認をおねがいます。')
