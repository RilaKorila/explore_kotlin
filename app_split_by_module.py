import streamlit as st

import get_plot

## 初期設定
st.set_page_config(layout="wide")

## ページ描画
st.title("Hello, Kotlin")

# kotlin compiler
st.write("## kotlin: compiler")

fig = get_plot.heatmap_ordered_by_first_commit(
    "data/kotlin/split_by_module/kotlin_compiler.csv"
)
fig.update_layout(
    title="kotlin: compiler",
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


# kotlin native
st.write("## kotlin: native")

fig = get_plot.heatmap_ordered_by_first_commit(
    "data/kotlin/split_by_module/kotlin_native.csv"
)
fig.update_layout(
    title="kotlin: native",
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

# kotlin analysis
st.write("## kotlin: analysis")

fig = get_plot.heatmap_ordered_by_first_commit(
    "data/kotlin/split_by_module/kotlin_analysis.csv"
)
fig.update_layout(
    title="kotlin: analysis",
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


# kotlin plugins
st.write("## kotlin: plugins")

fig = get_plot.heatmap_ordered_by_first_commit(
    "data/kotlin/split_by_module/kotlin_plugins.csv"
)
fig.update_layout(
    title="kotlin: plugins",
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


### Kotlin contributor
st.write("## contributor linechart: compiler/fir")
fig = get_plot.line_chart_from_df("data/kotlin/contributor_commit_counts.csv")
st.plotly_chart(fig, theme="streamlit", use_container_width=True)


st.write("## contributor top n: compiler/fir")
fig = get_plot.bar_chart_from_df_top_n("data/kotlin/contributor_commit_counts_top.csv")
st.plotly_chart(fig, theme="streamlit", use_container_width=True)
