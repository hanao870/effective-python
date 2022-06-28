"""項目35:ジェネレータで throw による状態遷移を起こすのは避ける."""
from typing import Generator


class MyError(Exception):
    """動作確認用例外クラス."""

    pass


def _my_generator() -> Generator[int, None, None]:
    yield 1
    yield 2
    yield 3


if __name__ == "__main__":
    it = _my_generator()
    print(next(it))
    print(next(it))
    print(it.throw(MyError("test error")))
