"""項目8:イテレータを並列に処理するには zip を使う."""
import itertools
from typing import Optional


def _usnig_enumerate(data: list[str]) -> None:
    longest_name: Optional[str] = None
    max_count = 0

    for i, name in enumerate(data):
        count = len(name)
        if count > max_count:
            longest_name = name
            max_count = count

    print(f"{longest_name=}, {max_count=}")
    print("-" * 50)


def _using_zip(data: list[str]) -> None:
    counts = [len(n) for n in data]

    print(f"{list(zip(data, counts))=}")
    print("-" * 50)

    longest_name: Optional[str] = None
    max_count = 0

    for name, count in zip(data, counts):
        if count > max_count:
            longest_name = name
            max_count = count

    print(f"{longest_name=}, {max_count=}")
    print("-" * 50)


def _zip_diff_len(data: list[str]) -> None:
    counts = [len(n) for n in data]
    data.append("Rosalind")

    print(f"{len(data)=}, {len(counts)=}")
    for name, count in zip(data, counts):
        print(f"{name=}, {count=}")
    print("-" * 50)

    # 要素数の多いリストに合わせた zip 処理
    for name, count in itertools.zip_longest(data, counts):
        print(f"{name}: {count}")
    print("-" * 50)


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

    print(f"{longest_name=}, {max_count=}")
    print("-" * 50)

    _usnig_enumerate(names)
    _using_zip(names)
    _zip_diff_len(names)
