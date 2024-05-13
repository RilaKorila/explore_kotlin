import plotly.graph_objects as go

from file_io import read_csv


def heatmap(source_type, sort_option):
    hisotry = read_csv(source_type)
    committed_filenames = hisotry.filenames
    print(committed_filenames)
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
