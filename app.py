import streamlit as st

import get_plot

## 初期設定
st.set_page_config(layout="wide")

## ページ描画
st.title("Hello, Kotlin")

# kotlinx.coroutines
st.write("## kotlinx.coroutines")
sort_option = st.radio(
    "Sort by:", ("Default", "Name"), index=0, key="radio_for_coroutines"
)
st.text("並び順: " + sort_option)

fig = get_plot.heatmap("serialization", sort_option)
fig.update_layout(title="kotlinx.coroutines: GitHub commits per month", xaxis_nticks=36)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

# kotlinx.serialization
st.write("## kotlinx.serialization")
sort_option = st.radio(
    "Sort by:", ("Default", "Name"), index=0, key="radio_for_serialization"
)
st.text("並び順: " + sort_option)

fig = get_plot.heatmap("serialization", sort_option)
fig.update_layout(
    title="kotlinx.serialization: GitHub commits per month", xaxis_nticks=36
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

# kotlin
st.write("## kotlin")
sort_option = st.radio("Sort by:", ("Default", "Name"), index=0, key="radio_for_kotlin")
st.text("並び順: " + sort_option)

fig = get_plot.diff_heatmap("kotlin", sort_option)
fig.update_layout(title="kotlin: GitHub commits per month", xaxis_nticks=36)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)


# KEEP
st.write("## kotlin")
sort_option = st.radio("Sort by:", ("Default", "Name"), index=0, key="radio_for_keep")
st.text("並び順: " + sort_option)

fig = get_plot.diff_heatmap("KEEP", sort_option)
fig.update_layout(title="kotlin: GitHub commits per month", xaxis_nticks=36)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)
