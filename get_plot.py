import plotly.express as px
import plotly.graph_objects as go

from file_io import read_csv, read_loc_diff_csv


def heatmap(source_type, sort_option):
    hisotry = read_csv(source_type)
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

    fig = go.Figure(
        data=go.Heatmap(
            z=sorted_counts, x=hisotry.dates, y=sorted_filenames, colorscale="Reds"
        )
    )

    return fig


def diff_heatmap(source_type, sort_option):
    hisotry = read_loc_diff_csv(source_type)
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

    # FIXME 0の時に白になるcolorscaleを作成する
    # min_value = min(min(sublist) for sublist in sorted_counts)
    # max_value = max(max(sublist) for sublist in sorted_counts)
    # original_color_scale = create_color_scale(min_value, max_value)
    # RdBuカラースケールを取得し、逆転する
    original_colorscale = px.colors.diverging.RdBu
    reversed_colorscale = original_colorscale[::-1]

    # カラースケールの例を作成
    colorscale = []
    for i, color in enumerate(reversed_colorscale):
        colorscale.append((i / (len(reversed_colorscale) - 1), color))
    fig = go.Figure(
        data=go.Heatmap(
            z=sorted_counts, x=hisotry.dates, y=sorted_filenames, colorscale=colorscale
        )
    )

    return fig


def create_color_scale(min_value, max_value):
    """
    既存のRdBuカラースケールだと、countが0の時に白にならなかったので自作する
    """
    # null_valueを計算
    null_value = (0 - min_value) / (max_value - min_value)
    colorlength = 100
    border = int(null_value * colorlength)

    # カラースケールを作成
    colorscale = []

    # colorscale below zero
    reds = px.colors.sequential.Reds[::-1]  # Reds カラーのリストを逆順にする
    reds = reds[:border]  # 必要な範囲に切り取る
    for i in range(len(reds)):
        colorscale.append((i / colorlength, reds[i]))

    # colorscale above zero
    greens = px.colors.sequential.Greens
    greens = greens[: colorlength - border]
    for i in range(len(greens)):
        colorscale.append(((i + border) / colorlength, greens[i]))

    return colorscale
