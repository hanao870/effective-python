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
    value = baz.get_private_field()
