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
