import csv

import pandas as pd

from commit_counts import CommitCounts
from commit_history import CommitHistory


def read_csv(fname):
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


def read_loc_diff_csv(fname):
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


def read_csv_as_df(fname):
    return pd.read_csv(fname)


def read_contributor_as_df(fname, filter_top10=False):
    data = []
    with open(fname, "r") as file:
        for line in file:
            try:
                # Name,Date Count の書式
                parts = line.split(",")
                name = parts[0]
                date = parts[1].split(" ")[0]
                count = int(parts[1].split(" ")[-1])

                # 日付が正しい形式か確認
                pd.to_datetime(date, format="%Y-%m")
                data.append([name, date, count])
            except (IndexError, ValueError) as e:
                print(line)

    # DataFrameを作成
    df = pd.DataFrame(data, columns=["Name", "Date", "Count"])
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce", format="%Y-%m")

    # contributorごとにデータをグループ化して処理
    if filter_top10:
        # 総コミット数で上位10名を選択
        top_contributors = df.groupby("Name")["Count"].sum().nlargest(10).index

        # 上位10名のデータをフィルタリング
        filtered_df = df[df["Name"].isin(top_contributors)]

        # 日付で並び替え
        filtered_df = filtered_df.sort_values(by="Date")
        return filtered_df
    else:
        grouped_df = df.groupby("Name")
        return grouped_df


def read_commit_coutns_csv():
    fname = "data/commit_counts_per_month.csv"

    with open(fname) as f:
        reader = csv.reader(f)
        csv_lines = [row for row in reader]

        commit_counts_list = []
        for line in csv_lines[1:]:
            counts = [int(count) for count in line[1:]]
            commit_counts_list.append(CommitCounts(line[0], counts))

    return commit_counts_list


def commit_counts_dates():
    fname = "data/commit_counts_per_month.csv"

    with open(fname) as f:
        reader = csv.reader(f)
        csv_lines = [row for row in reader]

        # csvのヘッダーを処理
        filename, *dates = csv_lines[0]
    return dates
