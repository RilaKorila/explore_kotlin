import streamlit as st

import get_plot

## 初期設定
st.set_page_config(layout="wide")

## ページ描画
st.title("Hello, Kotlin")

# kotlin
st.write("## kotlin: commit数")
sort_option_kotlin_aggregated = st.radio(
    "Sort by:", ("Default", "Name"), index=0, key="radio_for_kotlin_aggregated"
)
st.text("並び順: " + sort_option_kotlin_aggregated)

fig = get_plot.heatmap(
    "data/kotlin/aggregated_git_hisitory_logs_each_month.csv",
    sort_option_kotlin_aggregated,
)
fig.update_layout(
    title="kotlin: GitHub commits per month",
    xaxis=dict(
        tickangle=45,  # x軸のラベルを45度回転
        tickmode="array",
        dtick=1,  # すべてのラベルを表示
    ),
    margin=dict(t=50, l=50, r=50, b=200),
    height=1000,
    width=800,
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)


# kotlin
st.write("## kotlin: testを含む")
sort_option_kotlin_included_test = st.radio(
    "Sort by:",
    ("Default", "Name"),
    index=0,
    key="aggregated_git_hisitory_logs_each_month_included_test",
)
st.text("並び順: " + sort_option_kotlin_included_test)

fig = get_plot.heatmap(
    "data/kotlin/aggregated_git_hisitory_logs_each_month_included_test.csv",
    sort_option_kotlin_included_test,
)
fig.update_layout(
    title="kotlin: GitHub commits per month",
    xaxis=dict(
        tickangle=45,  # x軸のラベルを45度回転
        tickmode="array",
        dtick=1,  # すべてのラベルを表示
    ),
    margin=dict(t=50, l=50, r=50, b=200),
    height=1000,
    width=800,
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

# kotlin
st.write("## kotlin: testを含まない")
sort_option_kotlin_excluded_test = st.radio(
    "Sort by:",
    ("Default", "Name"),
    index=0,
    key="aggregated_git_hisitory_logs_each_month_excluded_test",
)
st.text("並び順: " + sort_option_kotlin_excluded_test)

fig = get_plot.heatmap(
    "data/kotlin/aggregated_git_hisitory_logs_each_month_excluded_test.csv",
    sort_option_kotlin_excluded_test,
)
fig.update_layout(
    title="kotlin: GitHub commits per month",
    xaxis=dict(
        tickangle=45,  # x軸のラベルを45度回転
        tickmode="array",
        dtick=1,  # すべてのラベルを表示
    ),
    margin=dict(t=50, l=50, r=50, b=200),
    height=1000,
    width=800,
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

# KEEP
st.write("## KEEP")
sort_option_keep = st.radio(
    "Sort by:", ("Default", "Name"), index=0, key="radio_for_keep"
)
st.text("並び順: " + sort_option_keep)

fig = get_plot.diff_heatmap(
    "data/KEEP/aggregated_git_log_changes_loc_only_proposal.csv", sort_option_keep
)
fig.update_layout(
    title="KEEP: GitHub commits per month",
    xaxis=dict(
        tickangle=45,  # x軸のラベルを45度回転
        tickmode="array",
        dtick=1,  # すべてのラベルを表示
    ),
    margin=dict(t=50, l=50, r=50, b=200),
    height=1000,
    width=800,
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)


# KEEP
st.write("## KEEP : 現状残っていないもの")
fig = get_plot.diff_heatmap(
    "data/KEEP/disappered/aggregated_git_log_changes_loc_only_proposal.csv",
    sort_option_keep,
)
fig.update_layout(
    title="KEEP: GitHub commits per month",
    xaxis=dict(
        tickangle=45,  # x軸のラベルを45度回転
        tickmode="array",
        dtick=1,  # すべてのラベルを表示
    ),
    margin=dict(t=50, l=50, r=50, b=200),
    height=1000,
    width=800,
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

## line chart
fig = get_plot.line_chart()
st.plotly_chart(fig, use_container_width=True)
