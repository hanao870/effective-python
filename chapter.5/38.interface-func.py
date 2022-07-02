"""項目38:単純なインターフェイスにはクラスの代わりに関数を使う."""
from collections import defaultdict


def _log_missing() -> int:
    print("Key added")
    return 0


def _increment_with_report(
    current: dict[str, int], increments: list[tuple[str, int]]
) -> tuple[dict[str, int], int]:
    added_count = 0

    def _missing() -> int:
        nonlocal added_count  # ステートフルクロージャー
        added_count += 1
        return 0

    result = defaultdict(_missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count


if __name__ == "__main__":
    names = ["Socrates", "Archimedes", "Plato", "Aristotle"]
    names.sort(key=len)
    print(names)

    current = {"green": 12, "blue": 3}
    increments = [
        ("red", 5),
        ("blue", 17),
        ("orange", 9),
    ]
    # キーが見つからなかったら呼ばれる関数を第1引数に指定
    result = defaultdict(_log_missing, current)
    print(f"Brfore: {dict(result)}")
    for key, amount in increments:
        result[key] += amount
    print("After: ", dict(result))

    result_1, count = _increment_with_report(current, increments)
    print(f"{count=}, {dict(result_1)=}")
