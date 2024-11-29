import streamlit as st
from PIL import Image
import common

common.check_login()

df_dset = st.session_state.dashbord_usersetting

if  str(df_dset.iloc[0,4]) == "True":

    with st.form(key='profile_form'):
        # テキストボックス
        name = st.text_input('お名前')
        adress = st.text_input('ご住所')
        
        if  str(df_dset.iloc[0,10]) == "True":
            # ラジオボタン
            age_category = st.radio(
                '年齢層',
                ('子ども（18歳未満）', '大人（18歳以上）')
            )
        else:
            # セレクトボックス
            age_category = st.selectbox(
                '年齢層',
                ('子ども（18歳未満）', '大人（18歳以上）')
            )
        
        # 複数選択
        hobby = st.multiselect(
            '趣味',
            ('スポーツ','読書','プログラミング','アニメ・映画','クルマ','バイク','釣り','料理','乗り鉄')
        )
        
        # ボタン
        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')

        if submit_btn:
            st.text(f'ようこそ！ {name} さん！ {adress} に書籍を送りました！。')
            st.text(f'年齢層: {age_category}')
            st.text(f'趣味: {",".join(hobby)}')
else:
    # 画像
    image = Image.open('./data/pose_yubisashi_kakunin_sagyouin_man.PNG')
    st.image(image, width=200)
    st.text('申し訳けありません、いまの権限ではグラフ表示ができません。\n'
            '設定値の確認をおねがいます。')
