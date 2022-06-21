"""項目22:可変長位置引数を使って、見た目をすっきりさせる."""
from my_libs.decolator import func_name


@func_name
def _log(message: str, values: list[int]) -> None:
    if not values:
        print(message)
    else:
        value_str = ", ".join(str(x) for x in values)
        print(f"{message}: {value_str}")


@func_name
def _log_1(message: str, *values: int) -> None:
    if not values:
        print(message)
    else:
        value_str = ", ".join(str(x) for x in values)
        print(f"{message}: {value_str}")


if __name__ == "__main__":
    _log("My numbers are", [1, 2])
    _log("Hi there", [])

    _log_1("My numbers are", 1, 2)
    _log_1("Hi there")
