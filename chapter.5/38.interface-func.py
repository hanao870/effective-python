"""項目38:単純なインターフェイスにはクラスの代わりに関数を使う."""


if __name__ == "__main__":
    names = ["Socrates", "Archimedes", "Plato", "Aristotle"]
    names.sort(key=len)
    print(names)
