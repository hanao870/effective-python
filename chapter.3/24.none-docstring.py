"""項目24:動的なデフォルト引数を指定するときには None と docstring を使う."""
import json
from datetime import datetime
from time import sleep
from typing import Any

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


@func_name
def _decode(data: str, default: dict[str, int] = {}) -> Any:
    try:
        return json.loads(data)
    except ValueError:
        return default


@func_name
def decode(data: str, default: dict[str, int] | None = None) -> Any:
    """JSON 形式の文字列を読み込む.

    Args:
        data (str): JSON 形式文字列
        default (dict[str, int] | None): 読込失敗時のデフォルト値.
            デフォルトは空の辞書

    Returns:
        Any: 読み込んだ JSON データ.
    """
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default


if __name__ == "__main__":
    _log("Hi there!")
    sleep(0.5)
    _log("Hello again!")

    log("Hi there!")
    sleep(0.5)
    log("Hello again!")

    # デフォルト引数は1回しか評価されないため、同じオブジェクトを共用する
    foo: dict[str, int] = _decode("bad data")
    foo["stuff"] = 5
    bar: dict[str, int] = _decode("also bad")
    bar["meep"] = 1
    print(f"Foo: {foo}")
    print(f"Bar: {bar}")

    # 戻り値が異なるオブジェクトの辞書のため、
    # _decode 関数で問題であったオブジェクトの共用を解消
    foo_1: dict[str, int] = decode("bad data")
    foo_1["stuff"] = 5
    bar_1: dict[str, int] = decode("also bad")
    bar_1["meep"] = 1
    print(f"Foo: {foo_1}")
    print(f"Bar: {bar_1}")
