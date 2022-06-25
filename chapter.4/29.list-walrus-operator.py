"""項目29:代入式を使い内包表記の繰り返し作業をなくす."""
stock = {"nails": 125, "screws": 35, "wingnuts": 8, "washers": 24}
order = ["screws", "wingnuts", "clips"]


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

    # 内包表記の評価順によるエラー
    # tenth は if の評価より後に定義される
    # bug = {name: (tenth := count // 10) for name, count in stock.items() if tenth > 0}
    # 代入式を if に移動させると解決
    result = {
        name: tenth for name, count in stock.items() if (tenth := count // 10) > 0
    }
    print(f"{result=}")

    # 変数のスコープはリスト内包表記外にも及ぶ
    half = [
        (squared := last**2) for count in stock.values() if (last := count // 2) > 10
    ]
    # flake8 では last と squared は未定義と判定される
    # print(f"Last item of {half} is {last} ** 2 = {squared}")

    # for ループ構造でも for の外にスコープが及ぶ
    for count_for in stock.values():
        last_for = count_for // 2
        squared_for = last_for**2
    print(f"{count_for} // 2 = {last_for}; {last_for} ** 2 = {squared_for}")

    # 代入式を使わないリスト内包表記ではスコープは外部に及ばない
    half = [count_list // 2 for count_list in stock.values()]
    print(f"{half=}")
    # 未定義エラー
    # print(f"{count_list=}")

    # イテレータの作成
    found_itr = (
        (name, batches)
        for name in order
        if (batches := _get_bathes(stock.get(name, 0), 8))
    )
    print(next(found_itr))
    print(next(found_itr))
