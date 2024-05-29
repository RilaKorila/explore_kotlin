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


def diff_heatmap(source_type, sort_option):
    hisotry = file_io.read_loc_diff_csv(source_type)
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
