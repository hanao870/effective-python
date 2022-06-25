"""項目28:内包表記では、3 つ以上の式を避ける."""


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"{matrix=}")

    flat = [x for row in matrix for x in row]
    print(f"{flat=}")

    squared = [[x**2 for x in row] for row in matrix]
    print(f"{squared=}")

    my_lists = [[[1, 2], [3, 4]], [[5, 6], [7, 8], [9, 10]]]
    print(f"{my_lists=}")

    # リスト内包表記の3重ループ. 非常に読みにくい
    my_flat = [x for sublist1 in my_lists for sublist2 in sublist1 for x in sublist2]
    print(f"{my_flat=}")

    # 上記をループ構造で表記. こちらのほうが読みやすい!
    my_flat = []
    for sublist1 in my_lists:
        for sublist2 in sublist1:
            my_flat.extend(sublist2)
    print(f"{my_flat=}")
