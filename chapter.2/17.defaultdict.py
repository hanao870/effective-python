"""項目17:内部状態の欠損要素を扱うには setdefault ではなく defaultdict を使う."""
from collections import defaultdict

from my_libs.decolator import func_name


class Visits:
    """訪問した国と都市を管理するクラス."""

    def __init__(self) -> None:
        """イニシャライザ.

        辞書を初期化
        """
        self.data: dict[str, set[str]] = defaultdict(set)

    def add(self, country: str, city: str) -> None:
        """`country` に `city` を追加する.

        Args:
            country (str): 訪問国
            city (str): 都市名
        """
        # city_set = self.data.setdefault(country, set())
        # city_set.add(city)
        self.data[country].add(city)


@func_name
def _setdefault_demo() -> None:
    visits = {"Mexico": {"Tulum", "Puerto Vallarta"}, "Japan": {"Hakone"}}

    visits.setdefault("France", set()).add("Arles")

    if (japan := visits.get("Japan")) is None:
        visits["Japan"] = japan = set()
    japan.add("Kyoto")

    print(visits)


@func_name
def _visits_demo_1() -> None:
    visits = Visits()
    visits.add("Russia", "Yekaterinburg")
    visits.add("Tanzania", "Zanzibar")
    print(visits.data)


@func_name
def _visits_demo_2() -> None:
    visits = Visits()
    visits.add("England", "Bath")
    visits.add("England", "London")
    print(visits.data)


if __name__ == "__main__":
    _setdefault_demo()
    _visits_demo_1()
    _visits_demo_2()
