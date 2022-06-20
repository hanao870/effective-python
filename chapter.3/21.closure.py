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


class Sorter:
    """ソートのヘルパークラス."""

    def __init__(self, group: set[int]) -> None:
        """イニシャライザ.

        Args:
            group (set[int]): ソートで優先する値のグループ
        """
        self.group = group
        self.found = False

    def __call__(self, x: int) -> tuple[int, int]:
        """...

        Args:
            x (int): ソート対象の値

        Returns:
            tuple[int, int]: ソート対象のインデックス
        """
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)


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

    sorter = Sorter(group)
    numbers.sort(key=sorter)
    print(f"Found: {found}")
    print(f"{numbers=}")
