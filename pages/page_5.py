# さまざまなチャート要素
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import common

common.check_login()

df_dset = st.session_state.dashbord_usersetting

if  str(df_dset.iloc[0,7]) == "True":
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    line_chart_data = pd.DataFrame(
        {
            "col1": np.random.randn(20),
            "col2": np.random.randn(20),
            "col3": np.random.choice(["A", "B", "C"], 20),
        }
    )

    # エリアチャート
    if  str(df_dset.iloc[0,17]) == "True":
        st.text('【エリアチャート】')
        st.area_chart(chart_data)
    else:
        # 画像
        image = Image.open('./data/pose_yubisashi_kakunin_sagyouin_man.PNG')
        st.image(image, width=200)
        st.text('申し訳けありません、いまの権限ではグラフ表示ができません。\n'
                '')
    

    # 散布図
    if  str(df_dset.iloc[0,18]) == "True":
        st.text('【散布図】')
        st.scatter_chart(chart_data)
    else:
        # 画像
        image = Image.open('./data/pose_yubisashi_kakunin_sagyouin_man.PNG')
        st.image(image, width=200)
        st.text('申し訳けありません、いまの権限ではグラフ表示ができません。\n'
                '')

    # 折れ線
    if  str(df_dset.iloc[0,19]) == "True":
        st.text('【折れ線グラフ】')
        st.line_chart(line_chart_data, x="col1", y="col2", color="col3")
    else:
        # 画像
        image = Image.open('./data/pose_yubisashi_kakunin_sagyouin_man.PNG')
        st.image(image, width=200)
        st.text('申し訳けありません、いまの権限ではグラフ表示ができません。\n'
                '')
else:
    # 画像
    image = Image.open('./data/pose_yubisashi_kakunin_sagyouin_man.PNG')
    st.image(image, width=200)
    st.text('申し訳けありません、いまの権限ではグラフ表示ができません。\n'
            '設定値の確認をおねがいます。')
