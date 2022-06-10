"""項目6:複数代入アンパック."""

if __name__ == "__main__":
    snack_calories = {"chips": 140, "popcorn": 80, "nuts": 190}
    items = tuple(snack_calories.items())
    print(items)
    print("-" * 50)

    # タプルの値をインデックスでアクセス
    item = ("Peanut butter", "Jelly")
    first = item[0]
    second = item[1]
    print(f"{first} and {second}")
    print("-" * 50)

    # タプルに代入(エラーとなる)
    pair = ("Chocolate", "Peanut butter")
    # pair[0] = "Honey"

    # アンパックによる値の取得
    first, second = pair
    print(f"{first} and {second}")
    print("-" * 50)
