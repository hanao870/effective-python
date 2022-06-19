"""項目19:複数の戻り値では、4個以上の変数なら決してアンパックしない."""
from my_libs.decolator import func_name


@func_name
def _get_stats(numbers: list[int]) -> tuple[int, int]:
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum


@func_name
def _my_function() -> tuple[int, int]:
    return 3, 4


if __name__ == "__main__":
    lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
    minimum, maximum = _get_stats(lengths)
    print(f"Min: {minimum}, Max: {maximum}")

    # アンパックと関数戻り値の動作確認
    first, second = 1, 2
    print(f"{first=}, {second=}")

    first, second = _my_function()
    print(f"{first=}, {second=}")
