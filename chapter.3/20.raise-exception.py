"""項目20:None を返すのではなく例外を送出する."""
from typing import Optional

from my_libs.decolator import func_name


@func_name
def _careful_divide(a: int, b: int) -> Optional[float]:
    try:
        return a / b
    except ZeroDivisionError:
        return None


@func_name
def _careful_divide_tuple(a: int, b: int) -> tuple[bool, Optional[float]]:
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


if __name__ == "__main__":
    x, y = 1, 0
    result = _careful_divide(x, y)
    if result is None:
        print("Invalid inputs")

    x, y = 0, 5
    result = _careful_divide(x, y)
    # None と 0 の判定となる
    if not result:
        print("Invalid inputs")

    # 第1戻り値に成否を受け取る
    success, result = _careful_divide_tuple(1, 0)
    if not success:
        print("Invalid inputs")

    # 但し、戻り値は簡単に無視できる. result が 0 の場合に問題あり
    _, result = _careful_divide_tuple(0, 5)
    if not result:
        print("Invalid inputs")
