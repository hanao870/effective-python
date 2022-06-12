"""項目10:代入式で繰り返しを防ぐ."""


def _make_lemonade(count: int) -> None:
    print("Call _make_lemonade")
    print("-" * 50)


def _out_of_stock() -> None:
    print("Call _out_of_stock")
    print("-" * 50)


if __name__ == "__main__":
    fresh_fruit = {"apple": 10, "banana": 8, "lemon": 5}

    count = fresh_fruit.get("lemon", 0)
    if count:
        _make_lemonade(count)
    else:
        _out_of_stock()

    # 上記の if を代入式で行う
    if count := fresh_fruit.get("lemon", 0):
        _make_lemonade(count)
    else:
        _out_of_stock()
