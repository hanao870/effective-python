"""項目42:プライベート属性よりパブリックな属性が好ましい."""
from typing import Type, TypeVar


class MyObject:
    """プライベート/パブリックの動作確認クラス."""

    def __init__(self) -> None:
        """イニシャライザ."""
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self) -> int:
        """プライベート変数値を取得する.

        Returns:
            int: プライベート変数値
        """
        return self.__private_field


U = TypeVar("U", bound="MyOtherObject")


class MyOtherObject:
    """クラスメソッドのプライベートフィールドアクセス."""

    def __init__(self) -> None:
        """イニシャライザ."""
        self.__private_field = 71

    @classmethod
    def get_private_field_to_instance(cls: Type[U], instance: "MyOtherObject") -> int:
        """プライベートフィールド値を取得する.

        Args:
            cls (Type[U]): 呼び出し元オブジェクト
            instance (MyOtherObject): 値を取得するクラスインスタンス

        Returns:
            int: フィールド値
        """
        return instance.__private_field


class MyParentObject:
    """プライベートフィールド動作確認用基底クラス."""

    def __init__(self) -> None:
        """イニシャライザ."""
        self.__private_field = 70


class MyChildObject(MyParentObject):
    """プライベートフィールド動作確認用派生クラス."""

    def get_private_field(self) -> int:
        """基底クラスのプライベートフィールド値を取得する.

        Returns:
            int: 基底クラスのプライベートフィールド値
        """
        # 基底クラスのプライベートフィールドの直接アクセスはエラー
        return self.__private_field
        # 以下の方法でプライベートフィールドにアクセスはできるが...
        # return self._MyParentObject__private_field


class MyStringClass:
    """プライベートフィールドの動作確認クラス."""

    def __init__(self, value: int) -> None:
        """イニシャライザ.

        Args:
            value (int): 設定値
        """
        self.__value = value

    def get_value(self) -> str:
        """プライベートフィールド値を `str` に変換する.

        Returns:
            str: `str` 変換した値
        """
        return str(self.__value)


class MyIntegerSubclass(MyStringClass):
    """基底クラスのプライベートフィールドアクセスの動作確認クラス."""

    def get_value_int(self) -> int:
        """基底クラスのプライベートフィールド値を取得する.

        Returns:
            int: 基底クラスのプライベートフィールド値
        """
        # 派生クラスから基底クラスのプライベートフィールドへアクセス可能
        # 以下の方法で取得できるが mypy でエラーとなる...
        # return int(self._MyStringClass__value)
        return 0


if __name__ == "__main__":
    foo = MyObject()
    print(f"{foo.public_field=}")

    print(f"{foo.get_private_field()=}")
    # プライベートフィールドの直接アクセスはエラー
    # print(f"{foo.__private_field=}")

    # クラスメソッドからプライベートフィールド値取得
    bar = MyOtherObject()
    value = MyOtherObject.get_private_field_to_instance(bar)
    print(f"{value=}")

    baz = MyChildObject()
    # value = baz.get_private_field()
    # オブジェクトの属性辞書を確認してプライベートフィールドの名前が確認できる
    print(baz.__dict__)
    # プライベートフィールドは以下の名前で登録されている
    # baz._MyParentObject__private_field

    hoge = MyStringClass(5)
    print(f"{hoge.get_value()=}")
    fuga = MyIntegerSubclass(50)
    print(f"{fuga.get_value_int()=}")
