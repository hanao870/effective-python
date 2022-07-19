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


class TimesSeven(MyBaseClass):
    """ひし形継承動作確認クラス."""

    def __init__(self, value: int) -> None:
        """イニシャライザ."""
        MyBaseClass.__init__(self, value)
        self.value *= 7


class PlusNine(MyBaseClass):
    """ひし形継承動作確認クラス."""

    def __init__(self, value: int) -> None:
        """イニシャライザ."""
        MyBaseClass.__init__(self, value)
        self.value += 9


class ThisWay(TimesSeven, PlusNine):
    """ひし形継承派生クラス."""

    def __init__(self, value: int) -> None:
        """イニシャライザ."""
        TimesSeven.__init__(self, value)
        PlusNine.__init__(self, value)


class TimesSevenCorrect(MyBaseClass):
    """ひし形継承動作確認クラス.

    基底クラスの初期化は super を使用.
    """

    def __init__(self, value: int) -> None:
        """イニシャライザ."""
        print("Call TimesSevenCorrect __init__")
        super().__init__(value)
        self.value *= 7


class PlusNineCorrect(MyBaseClass):
    """ひし形継承動作確認クラス.

    基底クラスの初期化は super を使用.
    """

    def __init__(self, value: int) -> None:
        """イニシャライザ."""
        print("Call PlusNineCorrect __init__")
        super().__init__(value)
        self.value += 9


class GoodWay(TimesSevenCorrect, PlusNineCorrect):
    """ひし形継承派生クラス.

    問題なく動作する.
    """

    def __init__(self, value: int) -> None:
        """イニシャライザ."""
        print("Call GoodWay __init__")
        super().__init__(value)


class MyBaseClassOther:
    """動作確認基底クラス."""

    def __init__(self, value: float) -> None:
        """イニシャライザ."""
        print("Call MyBaseClassOther __init__")
        self.value = value


class ExplicitTrisect(MyBaseClassOther):
    """関数 super の引数動作確認クラス."""

    def __init__(self, value: float) -> None:
        """イニシャライザ."""
        # 第1引数はスーパークラスから見たクラスの型
        # 第2引数は第1引数のクラスインスタンス
        # super は基本的に引数無しで使用する
        super(ExplicitTrisect, self).__init__(value)
        self.value /= 3


class AutomaticTrisect(MyBaseClassOther):
    """関数 super の引数動作確認クラス."""

    def __init__(self, value: float) -> None:
        """イニシャライザ."""
        super(self.__class__, self).__init__(value)
        self.value /= 3


class ImplicitTrisect(MyBaseClassOther):
    """関数 super の引数動作確認クラス."""

    def __init__(self, value: float) -> None:
        """イニシャライザ."""
        super().__init__(value)
        self.value /= 3


if __name__ == "__main__":
    foo = OneWay(5)
    print(f"First ordering is (5 * 2) + 5 = {foo.value}")

    # 期待する結果は (5 + 5) * 2 = 20 だが 15 が表示される.
    bar = AnotherWay(5)
    print(f"Second ordering still is {bar.value}")

    hoge = ThisWay(5)
    # hoge.value は 14 となる.
    # MyBaseClass.__init__ の2回呼び出しの為、値がリセットされる.
    print(f"Should be (5 * 7) + 9 = 44 but is {hoge.value}")

    fuga = GoodWay(5)
    print(f"Should be 7 * (5 + 9) = 98 and is {fuga.value}")

    # クラス呼び出し順 MRO(Method Resolution Order) の確認.
    mro_str = "\n".join(repr(cls) for cls in GoodWay.mro())
    print(mro_str)

    print(f"ExplicitTrisect(9) is {ExplicitTrisect(9).value}")
    print(f"AutomaticTrisect(9) is {AutomaticTrisect(9).value}")
    print(f"ImplicitTrisect(9) is {ImplicitTrisect(9).value}")
