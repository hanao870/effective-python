"""項目14:key 引数を使い複雑な基準でソートする."""


class Tool:
    """工具の情報を扱うクラス."""

    def __init__(self, name: str, weight: float) -> None:
        """イニシャライザ.

        Args:
            name (str): 工具名
            weight (float): 工具の重さ(kg)
        """
        self.name = name
        self.weight = weight

    def __repr__(self) -> str:
        """工具情報表示.

        Returns:
            str: 工具情報
        """
        return f"Tool({self.name!r}, {self.weight!r})"


if __name__ == "__main__":
    numbers = [93, 86, 11, 68, 70]
    print(f"Sort Before: {numbers}")

    numbers.sort()
    print(f"Sort After : {numbers}")

    tools = [
        Tool("Level", 3.5),
        Tool("Hammer", 1.25),
        Tool("Screwdriver", 0.5),
        Tool("Chisel", 0.25),
    ]

    # ソートメソッドが定義されていないためエラーとなる
    # tools.sort()

    print(f"Unsorted: {repr(tools)}")
    # 名前順にソート
    tools.sort(key=lambda x: x.name)
    print(f"Sorted  : {tools}")
