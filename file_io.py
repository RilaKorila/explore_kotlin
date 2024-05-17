import csv

from commit_history import CommitHistory


def read_csv(source_type):
    if source_type == "coroutines":
        fname = "data/coroutines/git_hisitory_logs_each_month.csv"
    elif source_type == "serialization":
        fname = "data/serialization/git_hisitory_logs_each_month.csv"

    with open(fname) as f:
        reader = csv.reader(f)
        csv_lines = [row for row in reader]

        # csvのヘッダーを処理
        filename, *dates = csv_lines[0]

        # csvの中身を処理
        committed_filenames = []
        committed_counts = []

        for line in csv_lines[1:]:
            filename, *counts = line
            committed_filenames.append(filename)
            committed_counts.append(counts)

    return CommitHistory(dates, committed_filenames, committed_counts)


def read_loc_diff_csv(source_type):
    if source_type == "coroutines":
        fname = "data/coroutines/git_hisitory_logs-loc_each_month.csv"
    elif source_type == "serialization":
        fname = "data/serialization/git_hisitory_logs-loc_each_month.csv"
    elif source_type == "kotlin":
        fname = "data/kotlin/git_hisitory_logs-loc_each_month_only_kt_before201207.csv"

    with open(fname) as f:
        reader = csv.reader(f)
        csv_lines = [row for row in reader]

        # csvのヘッダーを処理
        filename, *dates = csv_lines[0]

        # csvの中身を処理
        committed_filenames = []
        committed_counts = []

        for line in csv_lines[1:]:
            filename, *counts = line
            committed_filenames.append(filename)
            committed_counts.append([int(count) for count in counts])

    return CommitHistory(dates, committed_filenames, committed_counts)
