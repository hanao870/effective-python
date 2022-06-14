"""項目15:dict の挿入順序に依存する場合は注意する."""
from collections.abc import MutableMapping
from typing import Iterator


class SortedDict(MutableMapping[str, int]):
    """..."""

    def __init__(self) -> None:
        """イニシャライザ."""
        self.data: dict[str, int] = {}

    def __getitem__(self, key: str) -> int:
        """`key` の値を取得する.

        Args:
            key (str): 値を取得するキー

        Returns:
            int: `key` の値
        """
        return self.data[key]

    def __setitem__(self, key: str, value: int) -> None:
        """`key` に対応する `value` を設定する.

        Args:
            key (str):  キー
            value (int): `key` の値
        """
        self.data[key] = value

    def __delitem__(self, key: str) -> None:
        """`key` を削除する.

        Args:
            key (str): 削除するキー
        """
        del self.data[key]

    def __iter__(self) -> Iterator[str]:
        """クラス内辞書のイテレータを返す.

        Yields:
            Iterator[str]: 辞書のイテレータ
        """
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self) -> int:
        """辞書の長さを返す.

        Returns:
            int: クラス内辞書の長さ
        """
        return len(self.data)


class MyClass:
    """クラスのインスタンス辞書の動作確認用."""

    def __init__(self) -> None:
        """イニシャライザ."""
        self.alligator = "hatchling"
        self.elephant = "calf"


def _my_func(**kwargs: str) -> None:
    for key, value in kwargs.items():
        print(f"{key} = {value}")
    print("-" * 50)


def _popular_ranks(votes: dict[str, int], ranks: dict[str, int]) -> None:
    names = list(votes.keys())
    names.sort(key=lambda x: votes[x], reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


def _get_winner(ranks: dict[str, int]) -> str:
    return next(iter(ranks))


if __name__ == "__main__":
    baby_name = {"cat": "kitten", "dog": "puppy"}
    # Python 3.5 以前は、辞書への挿入順ではなく Key でソートされる
    print(baby_name)
    print("-" * 50)

    print(list(baby_name.keys()))
    print(list(baby_name.values()))
    print(list(baby_name.items()))
    # 最終挿入要素
    print(baby_name.popitem())
    print("-" * 50)

    _my_func(goose="gosling", kangaroo="joey")

    # クラスのインスタンス辞書は代入順で表示される
    a = MyClass()
    for key, value in a.__dict__.items():
        print(f"{key} = {value}")

    # 動物の赤ちゃんの投票数
    votes = {"otter": 1281, "polar bear": 587, "fox": 863}

    ranks: dict[str, int] = {}
    _popular_ranks(votes, ranks)
    print(ranks)
    winner = _get_winner(ranks)
    print(winner)
    print("-" * 50)

    # 標準辞書ではなく SortedDict に結果を格納する
    # mypy で型エラーが発生. 実行はできるが、結果は間違っている('fox' と表示される)
    # sorted_ranks = SortedDict()
    # _popular_ranks(votes, sorted_ranks)
    # print(sorted_ranks.data)
    # winner = _get_winner(sorted_ranks)
    # print(winner)
