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

    width = 10

    print(f"{'Unsorted':<{width}}: {repr(tools)}")
    # 名前順にソート
    tools.sort(key=lambda x: x.name)
    print(f"{'Sorted':<{width}}: {tools}")

    # 重さ順にソート
    tools.sort(key=lambda x: x.weight)
    print(f"{'By weight':<{width}}: {tools}")

    places = ["home", "work", "New York", "Paris"]
    places.sort()
    print(f"Case sensitive  : {places}")
    # 大文字小文字を無視
    places.sort(key=lambda x: x.lower())
    print(f"Case insensitive: {places}")

    power_tools = [
        Tool("drill", 4),
        Tool("circular saw", 5),
        Tool("jackhammer", 40),
        Tool("sander", 4),
    ]

    # タプルの比較
    saw = (5, "circular saw")
    jackhammer = (40, "jackhammer")
    print(f"{saw=}")
    print(f"{jackhammer=}")
    # タプルの第1要素を比較する
    print(f"{(jackhammer < saw)=}")

    drill = (4, "drill")
    sander = (4, "sander")
    print(f"{drill=}")
    print(f"{sander=}")
    # 第1要素が同じ場合は第2要素で比較する
    print(f"{(drill[0] == sander[0])=}")
    print(f"{(drill[1] < sander[1])=}")
    print(f"{(drill < sander)=}")

    # 重さ順に、名前でソートする
    print(f"Unsorted: {power_tools=}")
    power_tools.sort(key=lambda x: (x.weight, x.name))
    print(f"Sorted  : {power_tools=}")
