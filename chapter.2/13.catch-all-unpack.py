"""項目13:スライスではなく catch-all アンパックを使う."""

if __name__ == "__main__":
    car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
    car_ages_descending = sorted(car_ages, reverse=True)

    # リスト先頭の2つをアンパック(エラー)
    # oldest, second_oldest = car_ages_descending

    oldest = car_ages_descending[0]
    second_oldest = car_ages_descending[1]
    others = car_ages_descending[2:]
    print("Using slice:")
    print(f"{oldest=}, {second_oldest=}, {others=}")
    print("-" * 80)

    # catch-all によるリスト先頭2つのアンパック
    oldest, second_oldest, *others = car_ages_descending
    print("Using catch-all unpack:")
    print(f"{oldest=}, {second_oldest=}, {others=}")
    print("-" * 80)

    oldest, *others, youngest = car_ages_descending
    print(f"{oldest=}, {others=}, {youngest=}")
    print("-" * 80)

    *others, second_youngest, youngest = car_ages_descending
    print(f"{others=}, {second_youngest=}, {youngest=}")
    print("-" * 80)

    # catch-all で全取得はできない
    # *others = car_ages_descending
    # 複数の catch-all もできない
    # first, *middle, *second_middle = [1, 2, 3, 4, 5]

    # 複数レベルの構造では複数の catch-all アンパックが可能
    car_inventory = {
        "Downtown": ("Silver Shadow", "Pinto", "DMC"),
        "Airport": ("Skyline", "Viper", "Gremlin", "Nova"),
    }

    ((loc1, (best1, *rest1)), (loc2, (best2, *rest2))) = car_inventory.items()
    print(f"Best at {loc1} is {best1}, {len(rest1)} others")
    print(f"Best at {loc2} is {best2}, {len(rest2)} others")
    print("-" * 80)

    # 要素が不足する場合は catch-all アンパックは空リストになる
    rest: list[int]  # mypy の型アノテーション必須
    first, second, *rest = [1, 2]
    print(f"{first=}, {second=}, {rest=}")
