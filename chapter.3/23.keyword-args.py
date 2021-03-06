"""項目23:キーワード引数にオプションの振る舞いを与える."""
from my_libs.decolator import func_name


@func_name
def _remainder(number: int, divisor: int) -> int:
    return number % divisor


@func_name
def _print_parameter(**kwargs: float) -> None:
    for key, value in kwargs.items():
        print(f"{key} = {value}")


@func_name
def _flow_rate(
    weight_diff: float, time_diff: int, period: int = 1, unit_per_kg: float = 1
) -> float:
    return ((weight_diff * unit_per_kg) / time_diff) * period


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

    # キーワード引数
    _print_parameter(alpha=1.5, beta=9, gamma=4)

    weight_diff = 0.5
    time_diff = 3
    flow_per_second = _flow_rate(weight_diff, time_diff, 1)
    print(f"{flow_per_second:.3} kg per second")

    flow_per_second = _flow_rate(weight_diff, time_diff)
    print(f"{flow_per_second:.3} kg per second")
    flow_per_hour = _flow_rate(weight_diff, time_diff, period=3600)
    print(f"{flow_per_hour} kg per hour")

    pound_per_hour = _flow_rate(weight_diff, time_diff, period=3600, unit_per_kg=2.2)
    print(f"{pound_per_hour} pound per hour")
