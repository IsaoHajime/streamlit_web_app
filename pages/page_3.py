import streamlit as st
import pandas as pd

# 画面分割
col1, col2, col3 = st.columns(3)

# データ分析関連
# 豊田市
with col1:
    df_toyota = pd.read_csv('./data/平均気温豊田.csv', index_col='年月')
    st.text('【豊田 平均気温】')
    st.line_chart(df_toyota)

    st.bar_chart(df_toyota['月平均'])

# 横浜市
with col2:
    df_yokohama = pd.read_csv('./data/平均気温横浜.csv', index_col='年月')
    st.text('【横浜 平均気温】')
    st.line_chart(df_yokohama)

    st.bar_chart(df_yokohama['月平均'])

# 札幌市
with col3:
    df_sapporo = pd.read_csv('./data/平均気温札幌.csv', index_col='年月')
    st.text('【札幌 平均気温】')
    st.line_chart(df_sapporo)

    st.bar_chart(df_sapporo['月平均'])
