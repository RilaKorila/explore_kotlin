import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

import file_io
import get_plot


def save_heatmap():
    fig = get_plot.heatmap(
        "data/kotlin/aggregated_git_hisitory_logs_each_month.csv",
        "",
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
        width=2000,
    )

    pio.write_image(fig, "heatmap_kotlin.png", format="png", scale=2)


def save_individual_bar_charts(fname, output_dir):
    # データを読み込む
    df = file_io.read_contributor_as_df(fname, filter_top10=False)

    # 各貢献者ごとにグラフを作成して保存
    for name, group in df.groupby("Name"):
        fig = go.Figure()

        fig.add_trace(go.Bar(x=group["Date"], y=group["Count"], name=name))

        # グラフのレイアウトを設定
        fig.update_layout(
            title=f"Commit Counts Over Time for {name}",
            xaxis_title="Date",
            yaxis_title="Commit Count",
            legend_title="Contributor",
        )

        # ファイル名を作成して保存
        file_path = f"{output_dir}/{name}_commit_counts.png"
        fig.write_image(file_path)


if __name__ == "__main__":
    save_individual_bar_charts(
        "./data/kotlin/contributor_commit_counts_top.csv", "./result"
    )
