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
