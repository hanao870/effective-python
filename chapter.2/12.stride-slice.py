"""項目12:1つの式では、ストライドとスライスを同時に使わない."""

if __name__ == "__main__":
    x = ["red", "orange", "yellow", "green", "blue", "purple"]
    # list[start:end:stride] start から end まで stride の増分毎の要素を取得する
    odds = x[::2]
    even = x[1::2]

    print(f"{x=}")
    print(f"{odds=}")
    print(f"{even=}")

    # バイト列の逆順にストライドを使う
    j = b"mongoose"
    k = j[::-1]

    print(f"{j=}")
    print(f"{k=}")

    # Unicode 文字列でもストライドの逆順は有効
    ll = "寿司"
    m = ll[::-1]

    print(f"{ll=}")
    print(f"{m=}")

    # Unicode 文字列を UTF-8 でエンコードした場合はエラーとなる
    # n = "寿司"
    # oo = n.encode("utf-8")
    # pp = oo[::-1]
    # qq = pp.decode("utf-8")
