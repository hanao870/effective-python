"""項目12:1つの式では、ストライドとスライスを同時に使わない."""
from my_libs.decolator import func_name


@func_name
def _complex_stride() -> None:
    x = ["a", "b", "c", "d", "e", "f", "g", "h"]
    print(f"{x=}")
    print(f"{x[::2]=}")
    print(f"{x[::-2]=}")
    print("-" * 50)

    print(f"{x[2::2]=}")
    print(f"{x[-2::-2]=}")
    print(f"{x[-2:2:-2]=}")
    print(f"{x[2:2:-2]=}")
    print("-" * 50)

    # ストライドでスライス後、さらにスライスする.
    # ややこしい!!!!!
    y = x[::2]
    z = y[1:-1]

    print(f"{y=}")
    print(f"{z=}")


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

    _complex_stride()
