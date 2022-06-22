"""項目24:動的なデフォルト引数を指定するときには None と docstring を使う."""
from datetime import datetime
from time import sleep

from my_libs.decolator import func_name


@func_name
def _log(message: str, when: datetime = datetime.now()) -> None:
    print(f"{when}: {message}")


@func_name
def log(message: str, when: datetime | None = None) -> None:
    """`when` のタイムスタンプを含んだ `message` を出力する.

    Args:
        message (str): 出力するメッセージ
        when (datetime | None, optional): `message` 出力時のタイムスタンプ.
            デフォルトは現在時刻.
    """
    if when is None:
        when = datetime.now()
    print(f"{when}: {message}")


if __name__ == "__main__":
    _log("Hi there!")
    sleep(0.5)
    _log("Hello again!")

    log("Hi there!")
    sleep(0.5)
    log("Hello again!")
