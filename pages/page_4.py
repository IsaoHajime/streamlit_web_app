import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.subheader('【横浜 平均気温】')

df = pd.read_csv('./data/平均気温.csv', index_col='年月')
st.line_chart(df)

st.bar_chart(df['月平均'])
    


# matplotlib
fig, ax = plt.subplots()
ax.plot(df.index, df['月平均'])
ax.set_title('matplotlib Graph')
st.pyplot(fig)
