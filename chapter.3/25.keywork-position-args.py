"""項目25:キーワード専用引数と位置専用引数で明確さを高める."""
from my_libs.decolator import func_name


@func_name
def _safe_division(
    number: float,
    divisor: int,
    ignore_overflow: bool = False,
    ignore_zero_division: bool = False,
) -> float:
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


@func_name
def _safe_division_c(
    number: float,
    divisor: int,
    *,  # キーワード専用引数の開始
    ignore_overflow: bool = False,
    ignore_zero_division: bool = False,
) -> float:
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


if __name__ == "__main__":
    result = _safe_division(1.0, 10**500, True, False)
    print(result)

    result = _safe_division(1.0, 0, False, True)
    print(result)

    # キーワード引数による例外フラグの切替
    result = _safe_division(1.0, 10**500, ignore_overflow=True)
    print(result)

    result = _safe_division(1.0, 0, ignore_zero_division=True)
    print(result)

    # 従来の位置指定引数の呼び出しはエラーとなる
    # result = _safe_division_c(1.0, 10**500, True, False)
    result = _safe_division_c(1.0, 0, ignore_zero_division=True)
    print(result)

    try:
        result = _safe_division_c(1.0, 0)
    except ZeroDivisionError as e:
        print(e)
