"""デコレータ."""
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")  # パラメータ仕様変数. パラメータを表す型ヒント
R = TypeVar("R")  # 戻り値の型を R と定義


def func_name(f: Callable[P, R]) -> Callable[P, R]:
    """関数実行時に関数名を表示するデコレータ.

    Args:
        f (Callable[P, R]): 呼び出し元関数オブジェクト
    Returns:
        Callable[P, R]: 呼び出し元関数オブジェクト
    """

    @wraps(f)
    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Call {f.__name__}")
        print("-" * 50)
        v = f(*args, **kwargs)
        return v

    return inner
