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
