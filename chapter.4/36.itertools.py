"""項目36:イテレータとジェネレータの作業では itertools を使う."""
import itertools

if __name__ == "__main__":
    it = itertools.chain([1, 2, 3], [4, 5, 6])
    print(list(it))

    it_1 = itertools.repeat("hello", 3)
    print(list(it_1))

    it_2 = itertools.cycle([1, 2, 3])
    result = [next(it_2) for _ in range(10)]
    print(result)
