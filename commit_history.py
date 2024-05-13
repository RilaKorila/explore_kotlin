class CommitHistory:
    def __init__(self, dates, filenames, counts):
        self.dates = dates
        self.filenames = filenames
        self.counts = counts

        if len(counts) != len(filenames):
            print("countsは2次元配列です。外側の個数が、ファイル数と一致していません")
        if len(counts[0]) != len(dates):
            print("countsは2次元配列です。内側の個数が、日付の記録数と一致していません")
