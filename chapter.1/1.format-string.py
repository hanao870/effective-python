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
