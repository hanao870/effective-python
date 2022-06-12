"""項目10:代入式で繰り返しを防ぐ."""


def _make_lemonade(count: int) -> None:
    pass


def _out_of_stock() -> None:
    pass


if __name__ == "__main__":
    fresh_fruit = {"apple": 10, "banana": 8, "lemon": 5}

    count = fresh_fruit.get("lemon", 0)
    if count:
        _make_lemonade(count)
    else:
        _out_of_stock()
