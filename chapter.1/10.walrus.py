"""項目10:代入式で繰り返しを防ぐ."""
from my_libs.decolator import func_name


@func_name
def _make_lemonade(count: int) -> None:
    pass


@func_name
def _out_of_stock() -> None:
    pass


@func_name
def _make_cider(count: int) -> None:
    pass


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

    # リンゴの個数判定
    count = fresh_fruit.get("apple", 0)
    if count >= 4:
        _make_cider(count)
    else:
        _out_of_stock()

    # 上記 if を代入式で行う
    if (count := fresh_fruit.get("apple", 0)) >= 4:
        _make_cider(count)
    else:
        _out_of_stock()
