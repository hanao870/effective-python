"""項目16:辞書の欠損キーの処理には in や KeyError ではなく get を使う."""
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
