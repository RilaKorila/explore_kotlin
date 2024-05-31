import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import file_io


def heatmap(fname, sort_option):
    hisotry = file_io.read_csv(fname)
    committed_filenames = hisotry.filenames
    committed_counts = hisotry.counts

    if sort_option == "Name":
        sorted_indices = sorted(
            range(len(committed_filenames)), key=lambda k: committed_filenames[k]
        )
        sorted_filenames = [committed_filenames[i] for i in sorted_indices]
        sorted_counts = [committed_counts[i] for i in sorted_indices]
    else:
        sorted_filenames = committed_filenames
        sorted_counts = committed_counts

    colorscale = [
        [0, "white"],  # 最小値の色
        [1, "red"],  # 最大値の色
    ]
    fig = go.Figure(
        data=go.Heatmap(
            z=sorted_counts, x=hisotry.dates, y=sorted_filenames, colorscale=colorscale
        )
    )

    return fig


def heatmap_ordered_by_first_commit(fname):
    hisotry_df = file_io.read_csv_as_df(fname)
    sorted_history_df = sort_by_first_non_zero(hisotry_df)

    # ヒートマップ用のデータを準備
    sorted_filenames = sorted_history_df["filename"]
    sorted_counts = sorted_history_df.drop(columns=["filename"]).values
    history_dates = pd.to_datetime(sorted_history_df.columns[1:], format="%Y%m")

    colorscale = [
        [0, "white"],  # 最小値の色
        [1, "red"],  # 最大値の色
    ]
    fig = go.Figure(
        data=go.Heatmap(
            z=sorted_counts, x=history_dates, y=sorted_filenames, colorscale=colorscale
        )
    )
    return fig


def diff_heatmap(fname, sort_option):
    hisotry = file_io.read_loc_diff_csv(fname)
    committed_filenames = hisotry.filenames
    committed_counts = hisotry.counts
    min_value = min(min(sublist) for sublist in committed_counts)

    if sort_option == "Name":
        sorted_indices = sorted(
            range(len(committed_filenames)), key=lambda k: committed_filenames[k]
        )
        sorted_filenames = [committed_filenames[i] for i in sorted_indices]
        sorted_counts = [committed_counts[i] for i in sorted_indices]
    else:
        sorted_filenames = committed_filenames
        sorted_counts = committed_counts

    min_value = min(min(sublist) for sublist in sorted_counts)
    max_value = max(max(sublist) for sublist in sorted_counts)
    scale_range = max(abs(min_value), abs(max_value))

    original_color_scale = create_color_scale()
    fig = go.Figure(
        data=go.Heatmap(
            z=sorted_counts,
            x=hisotry.dates,
            y=sorted_filenames,
            colorscale=original_color_scale,
            zmin=-scale_range,
            zmax=scale_range,
        )
    )

    return fig


def line_chart():
    # 除外するデータを選択
    excluded_files = set(["llvm-project", "kandy", "dukat", "kotlin-spec"])

    # データの準備
    commit_counts = file_io.read_commit_coutns_csv()
    all_counts = []
    files = []
    for commit_count in commit_counts:
        if (
            commit_count.filename in excluded_files
            or "example" in commit_count.filename
            or "workshop" in commit_count.filename
        ):
            continue
        files.append(commit_count.filename)
        all_counts.append(commit_count.counts)

    dates = file_io.commit_counts_dates()

    # データフレームの作成
    chart_data = pd.DataFrame(all_counts).T
    chart_data.columns = files
    chart_data.index = dates

    # インデックスをリセットして、'Date'列を作成
    chart_data.reset_index(inplace=True)
    chart_data.rename(columns={"index": "Date"}, inplace=True)

    # Melt the dataframe to long format for plotly
    chart_data_long = pd.melt(
        chart_data,
        id_vars=["Date"],
        value_vars=files,
        var_name="File",
        value_name="Counts",
    )

    # Plotly Expressでラインチャートを描画
    fig = px.line(
        chart_data_long,
        x="Date",
        y="Counts",
        color="File",
        title="Commit Counts Over Time",
    )
    return fig


def line_chart_from_df(fname):
    df = file_io.read_contributor_as_df(fname)
    fig = go.Figure()

    for name, group in df:
        fig.add_trace(
            go.Scatter(x=group["Date"], y=group["Count"], mode="lines", name=name)
        )

    # グラフのレイアウトを設定
    fig.update_layout(
        title="Contributor Commit Counts Over Time",
        xaxis_title="Date",
        yaxis_title="Commit Count",
        legend_title="Contributor",
    )

    return fig


def bar_chart_from_df_top_n(fname):
    df = file_io.read_contributor_as_df(fname, filter_top10=False)
    fig = go.Figure()

    for name, group in df:
        fig.add_trace(go.Bar(x=group["Date"], y=group["Count"], name=name))
    # グラフのレイアウトを設定
    # fig.update_xaxes(range=[group["Date"].min(), group["Date"].max()])
    fig.update_yaxes(range=[0, 120])
    fig.update_layout(
        title="Contributor Commit Counts Over Time",
        xaxis_title="Date",
        yaxis_title="Commit Count",
        legend_title="Contributor",
    )

    return fig


def heatmap_contributor(fname):
    df = file_io.read_contributor_as_df(fname)
    # df["Date"] = pd.to_datetime(df["Date"]).dt.to_period("M")
    # pivot_table = df.pivot_table(values="Count", index="Name", columns="Date", fill_value=0, aggfunc='sum')
    # pivot_table = df.pivot_table(values="Count", index="Name", columns=df["Date"].dt.to_period("M"), fill_value=0, aggfunc='sum')
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m").dt.to_period("M")

    # ピボットテーブルを作成
    pivot_table = df.pivot_table(
        values="Count", index="Name", columns="Date", fill_value=0, aggfunc="sum"
    )

    # 列を文字列に変換
    pivot_table.columns = pivot_table.columns.astype(str)

    sorted_filenames = pivot_table.index
    sorted_counts = pivot_table.values
    history_dates = pd.to_datetime(pivot_table.columns, format="%Y-%m")

    colorscale = [
        [0, "white"],
        [1, "green"],
    ]
    pivot_table.columns = pivot_table.columns.astype(str)

    fig = go.Figure(
        data=go.Heatmap(
            z=sorted_counts, x=history_dates, y=sorted_filenames, colorscale=colorscale
        )
    )
    return fig


def create_color_scale():
    """
    既存のRdBuカラースケールだと、countが0の時に白にならなかったので自作する
    """
    colorscale = [
        [0, "blue"],  # 最小値の色
        [0.5, "white"],  # 0の色
        [1, "red"],  # 最大値の色
    ]

    return colorscale


def sort_by_first_non_zero(df):
    """
    DataFrameを0以外の数字が最初に登場するタイミング順に並び替える関数。

    Args:
        df (pd.DataFrame): 並び替え対象のDataFrame。

    Returns:
        pd.DataFrame: 並び替えたDataFrame。
    """

    def find_first_non_zero(row):
        for col in df.columns[1:]:
            if row[col] != 0:
                return col
        return df.columns[-1]  # 全て0の場合は最後の列を返す

    # 新しい列 'first_non_zero' に最初に0以外の数字が登場する列を記録
    df["first_non_zero"] = df.apply(find_first_non_zero, axis=1)

    # 'first_non_zero' 列を基にデータを並び替える
    sorted_df = df.sort_values(by="first_non_zero", ascending=False).drop(
        columns=["first_non_zero"]
    )

    return sorted_df
