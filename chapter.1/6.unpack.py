"""項目6:複数代入アンパック."""


def bubble_sort_old(a: list[str]) -> None:
    """従来のバブルソート.

    Args:
        a (list[str]): ソート対象リスト. ソート結果になる
    """
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                tmp = a[i]
                a[i] = a[i - 1]
                a[i - 1] = tmp


def bubble_sort_unpack(a: list[str]) -> None:
    """アンパックを用いたバブルソート.

    Args:
        a (list[str]): ソート対象リスト. ソート結果になる
    """
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                a[i - 1], a[i] = a[i], a[i - 1]


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

    names1 = ["pretzels", "carrots0", "arugula", "bacon"]
    bubble_sort_old(names1)
    print(names1)

    names2 = ["pretzels", "carrots0", "arugula", "bacon"]
    bubble_sort_unpack(names2)
    print(names2)
