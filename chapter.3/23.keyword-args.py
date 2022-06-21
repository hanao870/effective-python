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
