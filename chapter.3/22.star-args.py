"""項目22:可変長位置引数を使って、見た目をすっきりさせる."""
from typing import Iterator

from my_libs.decolator import func_name


@func_name
def _log(message: str, values: list[int]) -> None:
    if not values:
        print(message)
    else:
        value_str = ", ".join(str(x) for x in values)
        print(f"{message}: {value_str}")


@func_name
def _log_1(message: str, *values: int) -> None:
    if not values:
        print(message)
    else:
        value_str = ", ".join(str(x) for x in values)
        print(f"{message}: {value_str}")


def _my_generator() -> Iterator[int]:
    for i in range(10):
        yield i


def _my_func(*args: int) -> None:
    print(args)


if __name__ == "__main__":
    _log("My numbers are", [1, 2])
    _log("Hi there", [])

    _log_1("My numbers are", 1, 2)
    _log_1("Hi there")

    # 可変長位置引数に配列を渡す
    favorites = [7, 33, 99]
    _log_1("Favorite colors", *favorites)

    # 可変長位置引数は tuple に変換される.
    # ジェネレータの全要素が展開されるため、メモリが大量消費される.
    it = _my_generator()
    _my_func(*it)
