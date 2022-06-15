"""項目16:辞書の欠損キーの処理には in や KeyError ではなく get を使う."""
from my_libs.decolator import func_name


@func_name
def _complex_dict_in() -> None:
    votes = {"baguette": ["Bob", "Alice"], "ciabatta": ["Coco", "Deb"]}

    key = "brioche"
    who = "Elmer"

    if key in votes:
        names = votes[key]
    else:
        votes[key] = names = []

    names.append(who)
    print(f"{votes=}")


@func_name
def _complex_dict_key_error() -> None:
    votes = {"baguette": ["Bob", "Alice"], "ciabatta": ["Coco", "Deb"]}

    key = "brioche"
    who = "Elmer"

    try:
        names = votes[key]
    except KeyError:
        votes[key] = names = []

    names.append(who)
    print(f"{votes=}")


@func_name
def _complex_dict_get() -> None:
    votes = {"baguette": ["Bob", "Alice"], "ciabatta": ["Coco", "Deb"]}

    key = "brioche"
    who = "Elmer"

    # names = votes.get(key)
    # if names is None:
    #     votes[key] = names = []

    # 上記 if を代入式で簡略化
    if (names := votes.get(key)) is None:
        votes[key] = names = []

    names.append(who)
    print(f"{votes=}")


@func_name
def _complex_dict_setdefault() -> None:
    votes = {"baguette": ["Bob", "Alice"], "ciabatta": ["Coco", "Deb"]}

    key = "brioche"
    who = "Elmer"

    # _complex_dict_get と同じ処理を setdefault で記述
    # setdefault は key が存在しなければ第2引数の値を設定し、取得する
    names = votes.setdefault(key, [])
    names.append(who)
    print(f"{votes=}")


if __name__ == "__main__":
    counters = {"pumpernickel": 2, "sourdough": 1}

    # key の有無確認 using in
    key = "wheat"

    if key in counters:
        count = counters[key]
    else:
        count = 0
    counters[key] = count + 1

    # key の有無確認 using KeyError
    try:
        count = counters[key]
    except KeyError:
        count = 0

    counters[key] = count + 1

    # key の有無確認 using get
    count = counters.get(key, 0)
    counters[key] = count + 1

    # in / KeyError で count を省いた処理
    # 同じ key で2回アクセスする処理を記述する必要がある
    if key not in counters:
        counters[key] = 0
    counters[key] += 1

    if key in counters:
        counters[key] += 1
    else:
        counters[key] = 1

    try:
        counters[key] += 1
    except KeyError:
        counters[key] = 1

    _complex_dict_in()
    _complex_dict_key_error()
    _complex_dict_get()
    _complex_dict_setdefault()
