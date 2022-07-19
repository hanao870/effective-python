"""項目40:super を使ってスーパークラスを初期化する."""


class MyBaseClass:
    """動作確認用基底クラス."""

    def __init__(self, value: int) -> None:
        """イニシャライザ."""
        print("Call MyBaseClass __init__")
        self.value = value


class MyChildClass(MyBaseClass):
    """動作確認用派生クラス."""

    def __init__(self) -> None:
        """イニシャライザ."""
        # 多重継承の場合はうまく動作しない(?)
        MyBaseClass.__init__(self, 5)


class TimesTwo:
    """フィールド value を2倍にする基底クラス."""

    def __init__(self) -> None:
        """イニシャライザ."""
        print("Call TimesTwo __init__")
        self.value: int
        self.value *= 2


class PlusFive:
    """フィールド value に5を加算する基底クラス."""

    def __init__(self) -> None:
        """イニシャライザ."""
        print("Call PlusFive __init__")
        self.value: int
        self.value += 5


class OneWay(MyBaseClass, TimesTwo, PlusFive):
    """フィールド value を操作する派生クラス."""

    def __init__(self, value: int) -> None:
        """イニシャライザ."""
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    """フィールド value を操作する派生クラス."""

    def __init__(self, value: int) -> None:
        """イニシャライザ."""
        # 基底クラスの並びと __init__ 呼び出しが異なる
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


if __name__ == "__main__":
    foo = OneWay(5)
    print(f"First ordering is (5 * 2) + 5 = {foo.value}")

    # 期待する結果は (5 + 5) * 2 = 20 だが 15 が表示される.
    bar = AnotherWay(5)
    print(f"Second ordering still is {bar.value}")
