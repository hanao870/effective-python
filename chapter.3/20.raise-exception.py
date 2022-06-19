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


@func_name
def _careful_divide_raise(a: int, b: int) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Invalid inputs")


@func_name
def careful_divide(a: float, b: float) -> float:
    """Divides a by b.

    Args:
        a (float): 分母
        b (float): 分子

    Returns:
        float: a / b の値

    Raises:
        ValueError: a / b が失敗
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Invalid inputs")


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

    x, y = 5, 2
    try:
        result = _careful_divide_raise(x, y)
    except ValueError as err:
        print(err)
    else:
        print(f"Result is {result:.1f}")

    try:
        result = careful_divide(3, 0)
    except ValueError as err:
        print(err)
    else:
        print(f"Result is {result:.1f}")
