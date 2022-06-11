"""項目8:イテレータを並列に処理するには zip を使う."""

from typing import Optional

if __name__ == "__main__":
    # リスト内包表記による文字数カウント
    names = ["Cecilia", "Lise", "Marie"]
    counts = [len(n) for n in names]
    print(counts)
    print("-" * 50)

    # 最大文字数の要素を取得する
    longest_name: Optional[str] = None
    max_count = 0

    for i in range(len(names)):
        count = len(names[i])
        if count > max_count:
            longest_name = names[i]
            max_count = count

    print(f"{max_count=}, {longest_name=}")
    print("-" * 50)
