"""項目20:None を返すのではなく例外を送出する."""
from typing import Optional

from my_libs.decolator import func_name


@func_name
def _careful_divide(a: int, b: int) -> Optional[float]:
    try:
        return a / b
    except ZeroDivisionError:
        return None


if __name__ == "__main__":
    x, y = 1, 0
    result = _careful_divide(x, y)
    if result is None:
        print("Invalid inputs")
