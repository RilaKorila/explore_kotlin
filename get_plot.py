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
