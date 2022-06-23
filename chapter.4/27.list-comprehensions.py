"""項目27:map や filter の代わりにリスト内包表記を使う."""


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # リスト内包表記を用いずに2乗計算
    squares: list[int] = []

    for x in a:
        squares.append(x**2)
    print(f"{squares=}")

    squares_1 = [x**2 for x in a]
    print(f"{squares_1=}")

    # 上記のリスト内包表記を map で再現
    alt = map(lambda x: x**2, a)
    print(f"{list(alt)=}")

    even_squares = [x**2 for x in a if x % 2 == 0]
    print(f"{even_squares=}")

    # 上記リスト内包表記を map と filter で再現
    alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
    print(f"{list(alt)=}")

    # 辞書と集合のリスト内包表記
    even_squares_dict = {x: x**2 for x in a if x % 2 == 0}
    three_cubed_set = {x**3 for x in a if x % 3 == 0}
    print(f"{even_squares_dict=}")
    print(f"{three_cubed_set=}")

    alt_dict = dict(map(lambda x: (x, x**2), filter(lambda x: x % 2 == 0, a)))
    alt_set = set(map(lambda x: x**3, filter(lambda x: x % 3 == 0, a)))

    print(f"{alt_dict=}")
    print(f"{alt_set=}")
