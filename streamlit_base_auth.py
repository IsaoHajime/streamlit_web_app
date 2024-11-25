import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth

# ユーザ設定の.yamlファイルを読込んで認証情報を取得する


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
        else:
            st.text(f'ログインに失敗しました！ もう一度やり直してください。')
            
