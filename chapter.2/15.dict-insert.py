"""項目15:dict の挿入順序に依存する場合は注意する."""


def _my_func(**kwargs: str) -> None:
    for key, value in kwargs.items():
        print(f"{key} = {value}")
    print("-" * 50)


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
