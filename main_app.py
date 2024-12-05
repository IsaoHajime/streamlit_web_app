import streamlit as st
import streamlit_authenticator as stauth    # releas 0.2.3 :2023.09.08
from PIL import Image
import extra_streamlit_components as stx
import pandas as pd

import yaml
from yaml.loader import SafeLoader

## ユーザー設定読み込み
yaml_path = "config.yaml"

with open(yaml_path) as file:
        config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
)

st.title('やま アプリ')
st.caption('これは やま のPythonコード検証用テストアプリです。')

# 画像
image = Image.open('./data/Streamlitキャプチャ.PNG')
st.image(image, width=300)

# ダッシュボート設定情報を取得する
df = pd.read_csv('./data/dashbord_user.csv')


## Login UI
name, authentication_status, username = authenticator.login('ログイン', 'main')

if st.session_state["authentication_status"]:
        with st.sidebar:
                ## ログイン成功
                st.write(f'## Welcome *{st.session_state["name"]}*')
                st.write('# ログインしました!')

                ## Logout UI
                authenticator.logout('Logout','sidebar')


        # userID = st.text_input('ユーザーID')
        # userID = st.session_state["usernames"]
        userID = str.upper(username)

        # ボタン
        # submit_btn = st.form_submit_button('送信')
        # cancel_btn = st.form_submit_button('キャンセル')
        print(userID)


        # loginユーザのダッシュボート設定情報を取得する
        df_exist = df[df['id'] == userID]
        if df_exist.empty is False:
                st.dataframe(df_exist)
                st.session_state.dashbord_usersetting = df_exist
                #print('↓↓↓ ユーザセッションの設定値は以下のとおり ↓↓↓')
                #print(st.session_state.dashbord_usersetting)
                st.text(f'ようこそ！ {df_exist.iloc[0,1]} さん！ ログインに成功しました！。')
                # st.text(f'ようこそ、 {df_exist.loc[[userID],['name']]} さん！ ログインに成功しました！。')
                if df_exist.iloc[0,2] == 'admin' or df_exist.iloc[0,2] == 'owner':
                        st.dataframe(df)



                st.subheader('自己紹介')
                st.text('Pythonに関する情報をインターネット上から収集しているシステムエンジニア やま です\n'
                        'よろしければチャンネル登録・高評価、宜しくお願いいたします！')
                

                # 動画
                st.subheader('インド・ニューデリー  ラッシーづくり（４）')
                st.text('インド・ニューデリーのラッシー屋のラッシーができるまでの映像。店先で水牛ミルクを沸騰させてかき回し、\n'
                        'ろ過する様子や砂糖を入れて混ぜ合わせる様子が見られる。２００８年撮影。')
                #filepath = "https://www.nhk.or.jp/das/movie/D0002161/D0002161053_00000_V_000.mp4"
                #video_file = open("https://www.nhk.or.jp/das/movie/D0002161/D0002161053_00000_V_000.mp4",'rb')
                #video_file = open(filepath,'rb')
                video_file = open('./data/D0002161053_00000_V_000.mp4','rb')
                video_bytes = video_file.read()
                st.video(video_bytes)
                st.caption('【NHKクリエイティブ・ライブラリー】')

elif st.session_state["authentication_status"] is False:
        # ログイン失敗
        st.error(f'ログインに失敗しました！ もう一度やり直してください。')
elif st.session_state["authentication_status"] is None:
        # デフォルト
        st.warning(f'ユーザー名またはパスワードを入力してください。')
