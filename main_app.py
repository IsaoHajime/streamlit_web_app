import streamlit as st
from PIL import Image

st.title('やま アプリ')
st.caption('これは やま のPythonコード検証用テストアプリです。')

# 画像
image = Image.open('./data/Streamlitキャプチャ.PNG')
st.image(image, width=300)

st.subheader('自己紹介')
st.text('Pythonに関する情報をインターネット上から収集しているシステムエンジニア やま です\n'
        'よろしければチャンネル登録・高評価、宜しくお願いいたします！')


# 動画
st.subheader('インド・ニューデリー　ラッシーづくり（４）')
st.text('インド・ニューデリーのラッシー屋のラッシーができるまでの映像。店先で水牛ミルクを沸騰させてかき回し、\n'
        'ろ過する様子や砂糖を入れて混ぜ合わせる様子が見られる。２００８年撮影。')
#filepath = "https://www.nhk.or.jp/das/movie/D0002161/D0002161053_00000_V_000.mp4"
#video_file = open("https://www.nhk.or.jp/das/movie/D0002161/D0002161053_00000_V_000.mp4",'rb')
#video_file = open(filepath,'rb')
video_file = open('./data/D0002161053_00000_V_000.mp4','rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.caption('【NHKクリエイティブ・ライブラリー】')
