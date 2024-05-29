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

fig = get_plot.heatmap("data/coroutines/git_hisitory_logs_each_month.csv", sort_option)
fig.update_layout(title="kotlinx.coroutines: GitHub commits per month", xaxis_nticks=36)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

# kotlinx.serialization
st.write("## kotlinx.serialization")
sort_option = st.radio(
    "Sort by:", ("Default", "Name"), index=0, key="radio_for_serialization"
)
st.text("並び順: " + sort_option)

fig = get_plot.heatmap(
    "data/serialization/git_hisitory_logs_each_month.csv", sort_option
)
fig.update_layout(
    title="kotlinx.serialization: GitHub commits per month", xaxis_nticks=36
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

# kotlin
st.write("## kotlin: commit数")
sort_option = st.radio(
    "Sort by:", ("Default", "Name"), index=0, key="radio_for_kotlin_aggregated"
)
st.text("並び順: " + sort_option)

fig = get_plot.heatmap(
    "data/kotlin/aggregated_git_hisitory_logs_each_month.csv", sort_option
)
fig.update_layout(title="kotlin: GitHub commits per month", xaxis_nticks=36)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)


# kotlin
st.write("## kotlin: testを含む")
sort_option = st.radio(
    "Sort by:",
    ("Default", "Name"),
    index=0,
    key="aggregated_git_hisitory_logs_each_month_included_test",
)
st.text("並び順: " + sort_option)

fig = get_plot.heatmap(
    "data/kotlin/aggregated_git_hisitory_logs_each_month_included_test.csv", sort_option
)
fig.update_layout(title="kotlin: GitHub commits per month", xaxis_nticks=36)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

# kotlin
st.write("## kotlin: testを含まない")
sort_option = st.radio(
    "Sort by:",
    ("Default", "Name"),
    index=0,
    key="aggregated_git_hisitory_logs_each_month_excluded_test",
)
st.text("並び順: " + sort_option)

fig = get_plot.heatmap(
    "data/kotlin/aggregated_git_hisitory_logs_each_month_excluded_test.csv", sort_option
)
fig.update_layout(title="kotlin: GitHub commits per month", xaxis_nticks=36)

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

## line chart
fig = get_plot.line_chart()
st.plotly_chart(fig, use_container_width=True)
