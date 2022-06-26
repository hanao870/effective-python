"""項目31:引数に対してイテレータを使うときには確実さを優先する."""
from pathlib import Path
from typing import Callable, Iterator


class ReadVisits:
    """イテレータプロトコルを実装したコンテナクラス."""

    def __init__(self, data_path: str) -> None:
        """イニシャライザ.

        Args:
            data_path (str): 旅行者データを記録したファイル名
        """
        self.data_path = data_path

    def __iter__(self) -> Iterator[int]:
        """旅行者データを返すジェネレータ.

        Yields:
            Iterator[int]: `data_path` に記録された旅行者データ
        """
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


def _normalize(numbers: list[int]) -> list[float]:
    total = sum(numbers)
    result = []

    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result


def _read_visits(data_path: str) -> Iterator[int]:
    with open(data_path) as f:
        for line in f:
            yield int(line)


def _normalize_copy(numbers_itr: Iterator[int]) -> list[float]:
    numbers = list(numbers_itr)  # イテレータを複製
    total = sum(numbers)
    result = []

    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result


def _normalize_func(get_iter: Callable[[], Iterator[int]]) -> list[float]:
    total = sum(get_iter())  # 新たなイテレータ
    result = []

    for value in get_iter():  # 新たなイテレータ
        percent = 100 * value / total
        result.append(percent)

    return result


def _normalize_class(numbers: ReadVisits) -> list[float]:
    total = sum(numbers)
    result = []

    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result


if __name__ == "__main__":
    N = 100

    visits = [15, 35, 80]
    percentages = _normalize(visits)
    print(f"{percentages=}, {sum(percentages)=}")
    print("-" * N)

    file_path = Path(__file__).parent / "my_numbers.txt"
    it = _read_visits(str(file_path))
    # total = sum(numbers) でイテレータが最後まで生成される.
    # そのため、percentages は空のリストとなる.
    # percentages = _normalize(it)
    # print(percentages)

    it = _read_visits(str(file_path))
    percentages = _normalize_copy(it)
    print(f"{percentages=}, {sum(percentages)=}")
    print("-" * N)

    # イテレータを生成する関数を渡す
    percentages = _normalize_func(lambda: _read_visits(str(file_path)))
    print(f"{percentages=}, {sum(percentages)=}")
    print("-" * N)

    # コンテナクラスを使用
    visits_cls = ReadVisits(str(file_path))
    percentages = _normalize_class(visits_cls)
    print(f"{percentages=}, {sum(percentages)=}")
    print("-" * N)
