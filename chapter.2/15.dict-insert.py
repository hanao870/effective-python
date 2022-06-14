"""項目15:dict の挿入順序に依存する場合は注意する."""


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
