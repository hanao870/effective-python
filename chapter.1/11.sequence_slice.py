"""項目11:シーケンスをどのようにスライスするか知っておく."""


def _print_slice(a: list[str]) -> None:
    print(f"{a[:]=}")
    print(f"{a[:5]=}")
    print(f"{a[:-1]=}")
    print(f"{a[4:]=}")
    print(f"{a[-3:]=}")
    print(f"{a[2:5]=}")
    print(f"{a[2:-1]=}")
    print(f"{a[-3:-1]=}")


if __name__ == "__main__":
    a = ["a", "b", "c", "d", "e", "f", "g", "h"]

    print(f"{a=}")

    # list[start:end] でスライス.
    # start は含まれ、end は含まれない
    print(f"Middle two:     {a[3:5]}")
    print(f"All but ends:   {a[1:7]}")

    # 先頭からのスライス a[0:5] と同じ
    print(f"{a[:5]=}")
    # 末尾までのスライス a[5:len(a)] と同じ
    print(f"{a[5:]=}")

    _print_slice(a)

    # リストの境界を超えたスライス. 欠損要素は無視される
    first_twenty_items = a[:20]
    last_twenty_items = a[-20:]
    print(f"{first_twenty_items=}")
    print(f"{last_twenty_items=}")
    # インデックスアクセスではエラーとなる
    # print(f"{a[20]=}")

    # スライスして得られたリストは新しいリスト
    b = a[3:]
    print(f"Before    : {b=}")
    b[1] = "99"
    print(f"After     : {b=}")
    print(f"No change : {a=}")
    print("-" * 50)

    # スライスより短いリストを代入すると短くなる
    print(f"Before: {a=}")
    a[2:7] = ["99", "22", "14"]
    print(f"After : {a=}")
    print("-" * 50)

    # スライスより長いリストを代入すると長くなる
    print(f"Before: {a=}")
    a[2:3] = ["47", "11"]
    print(f"After : {a=}")
    print("-" * 50)
