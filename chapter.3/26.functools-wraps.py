"""項目26:functools.wraps を使って関数デコレータを定義する."""
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")  # パラメータ仕様変数. パラメータを表す型ヒント
R = TypeVar("R")  # 戻り値の型を R と定義


def trace(f: Callable[P, R]) -> Callable[P, R]:
    """関数の詳細情報を表示するデコレータ.

    Args:
        f (Callable[P, R]): 呼び出し元関数オブジェクト

    Returns:
        Callable[P, R]: 呼び出し元関数オブジェクト
    """

    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        result = f(*args, **kwargs)
        print(f"{f.__name__}({args!r}, {kwargs!r}) -> {result!r}")
        return result

    return wrapper


@trace
def fibonacci(n: int) -> int:
    """`n` 番目のフィボナッチ数列を返す.

    Args:
        n (int): フィボナッチ数列の番号

    Returns:
        int: `n` 番目のフィボナッチ数列
    """
    if n in (1, 0):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == "__main__":
    fibonacci(4)

    print(fibonacci)
    help(fibonacci)

    # デコレートされた元の関数の位置を特定できないためエラーとなる
    # import pickle

    # pickle.dumps(fibonacci)
