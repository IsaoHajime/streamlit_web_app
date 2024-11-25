import streamlit as st
from PIL import Image

df_dset = st.session_state.dashbord_usersetting
#変数型が微妙に違うのだか。。
test = df_dset.iloc[0,3]
print(type(test))
print("col3:" + str(test))
test = df_dset.iloc[0,9]
print(type(test))
print("col9:" + str(test))

if  str(df_dset.iloc[0,3]) == "True" and str(df_dset.iloc[0,9]) == "True":
    code = '''
    import streamlit as st

    st.title('やま アプリ')
    '''
    st.code(code, language='python')
else:
    # 画像
    image = Image.open('./data/pose_yubisashi_kakunin_sagyouin_man.PNG')
    st.image(image, width=200)
    st.text('申し訳けありません、いまの権限ではグラフ表示ができません。\n'
            '設定値の確認をおねがいます。')
