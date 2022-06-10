"""項目5ヘルパー関数."""
from urllib.parse import parse_qs


def get_first_int(values: dict[str, list[str]], key: str, default: int = 0) -> int:
    """`values` から `key` の値を検索するヘルパー関数.

    Args:
        values (dict[str, list[str]]): クエリデータ
        key (str): 検索するキー
        default (int, optional): `key` が存在しない場合のデフォルト値. Defaults to 0.

    Returns:
        int: `key` が存在する場合は `key` の値. ない場合は `default` 値
    """
    found = values.get(key, [""])

    if found[0]:
        return int(found[0])
    else:
        return default


if __name__ == "__main__":
    my_value = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
    print(repr(my_value))

    print("Red:      ", my_value.get("red"))
    print("Green:    ", my_value.get("green"))
    print("Opacity:  ", my_value.get("opacity"))
    print("-" * 50)

    # or の前が False の場合は or の後ろの値が採用される
    # 正直わかりにくい
    red = my_value.get("red", [""])[0] or 0
    green = my_value.get("green", [""])[0] or 0
    opacity = my_value.get("opacity", [""])[0] or 0

    print(f"Red:     {red!r}")
    print(f"Green:   {green!r}")
    print(f"Opacity: {opacity!r}")
    print("-" * 50)

    # 上記の3項演算子バージョン
    # 他2つも同じことを記述する必要がある
    red_str = my_value.get("red", [""])
    red = int(red_str[0]) if red_str[0] else 0

    # ヘルパー関数による値の取得
    green = get_first_int(my_value, "green")
    opacity = get_first_int(my_value, "opacity")

    print(f"Red:     {red!r}")
    print(f"Green:   {green!r}")
    print(f"Opacity: {opacity!r}")
