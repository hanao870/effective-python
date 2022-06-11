"""項目8:イテレータを並列に処理するには zip を使う."""

if __name__ == "__main__":
    # リスト内包表記による文字数カウント
    names = ["Cecilia", "Lise", "Marie"]
    counts = [len(n) for n in names]
    print(counts)
    print("-" * 50)
