"""項目35:ジェネレータで throw による状態遷移を起こすのは避ける."""
from typing import Generator


class MyError(Exception):
    """動作確認用例外クラス."""

    pass


class Reset(Exception):
    """タイマーリセット用例外."""

    pass


def _my_generator() -> Generator[int, None, None]:
    yield 1
    yield 2
    yield 3


def _my_generator_1() -> Generator[int, None, None]:
    yield 1

    try:
        yield 2
    except MyError:
        print("Got MyError!!!")
    else:
        yield 3

    yield 4


def _timer(period: int) -> Generator[int, None, None]:
    current = period
    while current:
        current -= 1
        try:
            yield current
        except Reset:
            current = period


RESETS = [
    False,
    False,
    False,
    True,
    False,
    True,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
]


def _check_for_reset() -> bool:
    # 外部イベントをポーリングして待つ
    return RESETS.pop(0)


def _announce(remaining: int) -> None:
    print(f"{remaining} ticks remaining")


def _run() -> None:
    it = _timer(4)

    while True:
        try:
            if _check_for_reset():
                current = it.throw(Reset())
            else:
                current = next(it)
        except StopIteration:
            break
        else:
            _announce(current)


if __name__ == "__main__":
    it = _my_generator()
    print(next(it))
    print(next(it))
    # print(it.throw(MyError("test error")))
    print("-" * 50)

    it = _my_generator_1()
    print(next(it))
    print(next(it))
    print(it.throw(MyError("test error")))
    print("-" * 50)

    _run()
    print("-" * 50)
