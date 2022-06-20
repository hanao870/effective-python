"""項目21:クロージャが変数スコープとどう関わるかを把握しておく."""
from my_libs.decolator import func_name


@func_name
def _sort_priority(values: list[int], group: set[int]) -> None:
    def _helper(x: int) -> tuple[int, int]:
        if x in group:
            return (0, x)
        return (1, x)

    values.sort(key=_helper)


if __name__ == "__main__":
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}
    _sort_priority(numbers, group)
    print(f"{numbers=}")
