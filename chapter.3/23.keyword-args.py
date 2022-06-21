"""項目23:キーワード引数にオプションの振る舞いを与える."""
from my_libs.decolator import func_name


@func_name
def _remainder(number: int, divisor: int) -> int:
    return number % divisor


if __name__ == "__main__":
    print(_remainder(20, 7))

    # 以下の呼び出しは全て同じ.
    print(_remainder(20, divisor=7))
    print(_remainder(number=20, divisor=7))
    print(_remainder(divisor=7, number=20))

    # 位置引数はキーワード引数より前の位置で指定する
    # print(_remainder(number=20, 7))
    # 各引数は1回だけ指定できる
    # print(_remainder(20, number=7))

    # キーワード引数に対応した辞書を渡す
    my_kwargs = {"number": 20, "divisor": 7}
    print(f"{_remainder(**my_kwargs)=}")

    # キーワードに重複がない限り ** を渡せる
    my_kwargs = {"divisor": 7}
    print(f"{_remainder(number=20, **my_kwargs)=}")

    # 重複がない限り複数の ** を渡せる
    my_kwargs = {"number": 20}
    other_kwargs = {"divisor": 7}
    print(f"{_remainder(**my_kwargs, **other_kwargs)=}")
