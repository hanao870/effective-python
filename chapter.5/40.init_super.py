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


if __name__ == "__main__":
    foo = OneWay(5)
    print(f"First ordering is (5 * 2) + 5 = {foo.value}")
