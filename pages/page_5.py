# さまざまなチャート要素
import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

line_chart_data = pd.DataFrame(
    {
        "col1": np.random.randn(20),
        "col2": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20),
    }
)

# エリアチャート
st.text('【エリアチャート】')
st.area_chart(chart_data)

# 散布図
st.text('【散布図】')
st.scatter_chart(chart_data)

# 折れ線
st.text('【折れ線グラフ】')
st.line_chart(line_chart_data, x="col1", y="col2", color="col3")