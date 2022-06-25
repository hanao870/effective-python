"""項目29:代入式を使い内包表記の繰り返し作業をなくす."""
from my_libs.decolator import func_name

stock = {"nails": 125, "screws": 35, "wingnuts": 8, "washers": 24}
order = ["screws", "wingnuts", "clips"]


@func_name
def _get_bathes(count: int, size: int) -> int:
    return count // size


if __name__ == "__main__":
    result: dict[str, int] = {}

    for name in order:
        count = stock.get(name, 0)
        batches = _get_bathes(count, 8)
        if batches:
            result[name] = batches

    print(f"{result=}")

    # 上記ループと同じリスト内包表記
    found = {
        name: _get_bathes(stock.get(name, 0), 8)
        for name in order
        if _get_bathes(stock.get(name, 0), 8)
    }
    print(f"{found=}")

    # 同じ関数呼び出しが2か所あるため、1か所の引数だけを変更する可能性がある
    has_bug = {
        name: _get_bathes(stock.get(name, 0), 4)
        for name in order
        if _get_bathes(stock.get(name, 0), 8)
    }
    print(f"{has_bug=}")

    # 代入式で関数呼び出しを1回にする
    found = {
        name: batches
        for name in order
        if (batches := _get_bathes(stock.get(name, 0), 8))
    }
