import streamlit as st
from PIL import Image
import pandas as pd
import common

common.check_login()

df_dset = st.session_state.dashbord_usersetting

if  str(df_dset.iloc[0,5]) == "True":
    # 画面分割
    col1, col2, col3 = st.columns(3)

    # データ分析関連
    # 豊田市
    if  str(df_dset.iloc[0,11]) == "True":
        with col1:
            df_toyota = pd.read_csv('./data/平均気温豊田.csv', index_col='年月')
            st.text('【豊田 平均気温】')
            st.line_chart(df_toyota)
            st.bar_chart(df_toyota['月平均'])
    else:
        with col1:
            st.text('')

    # 横浜市
    if  str(df_dset.iloc[0,12]) == "True":
        with col2:
            df_yokohama = pd.read_csv('./data/平均気温横浜.csv', index_col='年月')
            st.text('【横浜 平均気温】')
            st.line_chart(df_yokohama)
            st.bar_chart(df_yokohama['月平均'])
    else:
        with col1:
            st.text('')

    # 札幌市
    if  str(df_dset.iloc[0,13]) == "True":
        with col3:
            df_sapporo = pd.read_csv('./data/平均気温札幌.csv', index_col='年月')
            st.text('【札幌 平均気温】')
            st.line_chart(df_sapporo)
            st.bar_chart(df_sapporo['月平均'])
    else:
        with col1:
            st.text('')
else:
    # 画像
    image = Image.open('./data/pose_yubisashi_kakunin_sagyouin_man.png')
    st.image(image, width=200)
    st.text('申し訳けありません、いまの権限ではグラフ表示ができません。\n'
            '設定値の確認をおねがいます。')
