import streamlit as st
from PIL import Image
import pandas as pd

st.title('やま アプリ')
st.caption('これは やま のPythonコード検証用テストアプリです。')

# 画像
image = Image.open('./data/Streamlitキャプチャ.PNG')
st.image(image, width=300)


# ログイン・ユーザーフォーム
# テキストボックス
with st.form(key='login_form'):
    st.subheader('ログイン')
    userID = st.text_input('ユーザーID')
    
    # ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    print(userID)


if submit_btn:
        df = pd.read_csv('./data/dashbord_user.csv')
        # ダッシュボート設定情報を取得する
        df_exist = df[df['id'] == userID]
        if df_exist.empty is False:
                print(df_exist)
                st.dataframe(df_exist)
                st.session_state.dashbord_usersetting = df_exist
                print('↓↓↓ ユーザセッションの設定値は以下のとおり ↓↓↓')
                print(st.session_state.dashbord_usersetting)
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

        else:
                st.text(f'ログインに失敗しました！ もう一度やり直してください。')
