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

    # 複雑なアンパック
    favorite_snacks = {
        "salty": ("pretzels", 100),
        "sweet": ("cookie", 180),
        "veggie": ("carrots", 20),
    }

    (
        (type1, (name1, cals1)),
        (type2, (name2, cals2)),
        (type3, (name3, cals3)),
    ) = favorite_snacks.items()

    print(f"Favorite {type1} is {name1} with {cals1} calories")
    print(f"Favorite {type2} is {name2} with {cals2} calories")
    print(f"Favorite {type3} is {name3} with {cals3} calories")
    print("-" * 50)
