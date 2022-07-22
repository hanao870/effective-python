"""項目42:プライベート属性よりパブリックな属性が好ましい."""


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


if __name__ == "__main__":
    foo = MyObject()
    print(f"{foo.public_field=}")
