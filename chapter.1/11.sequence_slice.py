"""項目11:シーケンスをどのようにスライスするか知っておく."""


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
