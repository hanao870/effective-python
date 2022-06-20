"""項目21:クロージャが変数スコープとどう関わるかを把握しておく."""
from my_libs.decolator import func_name


@func_name
def _sort_priority(values: list[int], group: set[int]) -> None:
    def _helper(x: int) -> tuple[int, int]:
        if x in group:
            return (0, x)
        return (1, x)

    values.sort(key=_helper)


@func_name
def _sort_priority2(numbers: list[int], group: set[int]) -> bool:
    found = False

    def _helper(x: int) -> tuple[int, int]:
        if x in group:
            # クロージャ関数での代入は新たな変数定義となる
            # found = True  # 簡単そうに見える
            return (0, x)
        return (1, x)

    numbers.sort(key=_helper)
    return found


@func_name
def _sort_priority3(numbers: list[int], group: set[int]) -> bool:
    found = False

    def _helper(x: int) -> tuple[int, int]:
        nonlocal found  # スコープの横断
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=_helper)
    return found


if __name__ == "__main__":
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}
    _sort_priority(numbers, group)
    print(f"{numbers=}")

    found = _sort_priority2(numbers, group)
    print(f"Found: {found}")
    print(f"{numbers=}")

    found = _sort_priority3(numbers, group)
    print(f"Found: {found}")
    print(f"{numbers=}")
