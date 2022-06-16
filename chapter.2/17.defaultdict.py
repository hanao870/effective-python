"""項目17:内部状態の欠損要素を扱うには setdefault ではなく defaultdict を使う."""
if __name__ == "__main__":
    visits = {"Mexico": {"Tulum", "Puerto Vallarta"}, "Japan": {"Hakone"}}

    visits.setdefault("France", set()).add("Arles")

    if (japan := visits.get("Japan")) is None:
        visits["Japan"] = japan = set()
    japan.add("Kyoto")

    print(visits)
