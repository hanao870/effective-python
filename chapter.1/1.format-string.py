"""Format string の動作確認."""


if __name__ == "__main__":
    key = "my_var"
    value = 1.234

    formatted = f"{key} = {value}"
    print(formatted)

    # !r repr 呼び出し
    # :<10 文字幅を 10 に設定
    # .2f 小数点第3位を四捨五入
    formatted = f"{key!r:<10} = {value:.2f}"
    print(formatted)

    # 以下のフォーマット結果は全て同じ
    f_string = f"{key:<10} = {value:.2f}"
    c_tuple = "%-10s = %.2f" % (key, value)
    str_args = "{:<10} = {:.2f}".format(key, value)
    str_kw = "{key:<10} = {value:.2f}".format(key=key, value=value)
    c_dict = "%(key)-10s = %(value).2f" % {"key": key, "value": value}

    assert c_tuple == c_dict == f_string
    assert str_args == str_kw == f_string

    pantry: list[tuple[str, float]] = [
        ("avocados", 1.25),
        ("bananas", 2.5),
        ("cherries", 15),
    ]

    print("-" * 50)

    for i, (item, count) in enumerate(pantry):
        old_style = "#%d: %-10s = %d" % (i + 1, item.title(), round(count))
        new_style = "#{}: {:<10s} = {}".format(i + 1, item.title(), round(count))
        f_string = f"#{i+1}: {item.title():<10s} = {round(count)}"

        print(f"{old_style=}")
        print(f"{new_style=}")
        print(f"{f_string =}")
        print("-" * 50)

        assert old_style == new_style == f_string
