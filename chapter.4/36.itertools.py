"""項目36:イテレータとジェネレータの作業では itertools を使う."""
import itertools


def _evens(x: int) -> bool:
    return x % 2 == 0


def _sum_modulo_20(first: int, second: int) -> int:
    output = first + second
    return output % 20


if __name__ == "__main__":
    it = itertools.chain([1, 2, 3], [4, 5, 6])
    print(list(it))

    it_1 = itertools.repeat("hello", 3)
    print(list(it_1))

    it_2 = itertools.cycle([1, 2, 3])
    result = [next(it_2) for _ in range(10)]
    print(result)

    # 1つのイテレータを第2引数で指定した数のイテレータに分割する
    it1, it2, it3 = itertools.tee(["first", "second", "third"], 3)
    print(list(it1))
    print(list(it2))
    print(list(it3))

    keys = ["one", "two", "three"]
    values = [1, 2]
    # 要素数の少ないイテレータをまとめた tuple イテレータを返す
    normal = list(zip(keys, values))
    print(f"zip: {normal}")

    # 要素数の多いイテレータをまとめた tuple イテレータを返す
    it_3 = itertools.zip_longest(keys, values, fillvalue="nope")
    longest = list(it_3)
    print(f"zip_longest: {longest}")

    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    first_five = itertools.islice(values, 5)
    print(f"First five: {list(first_five)}")

    middle_odds = itertools.islice(values, 2, 8, 2)
    print(f"Middle odds: {list(middle_odds)}")

    # 第1引数の条件式が False を返すまでイテレータの要素を返す
    it_4 = itertools.takewhile(lambda x: x < 7, values)
    print(f"itertools.takewhile: {list(it_4)}")

    # 第1引数の条件式が True を返すまでイテレータの要素をスキップする
    it_5 = itertools.dropwhile(lambda x: x < 7, values)
    print(f"itertools.dropwhile: {list(it_5)}")

    # 第1引数の条件式が True の要素を返す
    filter_result = filter(_evens, values)
    print(f"filter: {list(filter_result)}")

    # 第1引数の条件式が False の要素を返す
    filter_false_result = itertools.filterfalse(_evens, values)
    print(f"itertools.filterfalse] {list(filter_false_result)}")

    # イテレータに第2引数の値を適用する. 未指定の場合はイテレータの和を返す
    sum_reduce = itertools.accumulate(values)
    print(f"Sum: {list(sum_reduce)}")

    module_reduce = itertools.accumulate(values, _sum_modulo_20)
    print(f"Modulo: {list(module_reduce)}")

    # 1つ以上のイテレータの要素の直積を返す
    single = itertools.product([1, 2], repeat=2)
    print(f"Single: {list(single)}")

    multiple = itertools.product([1, 2], ["a", "b", "c"])
    print(f"Multiple: {list(multiple)}")

    # 第2引数の要素を取り出してできる順列を返す
    it_6 = itertools.permutations([1, 2, 3, 4], 2)
    print(f"itertools.permutations: {list(it_6)}")

    # 第2引数の要素数を取り出してできる全ての組み合わせを順不同で返す
    it_7 = itertools.combinations([1, 2, 3, 4], 2)
    print(f"itertools.combinations: {list(it_7)}")

    # itertools.combinations に自身の要素を追加する
    it_8 = itertools.combinations_with_replacement([1, 2, 3, 4], 2)
    print(f"itertools.combinations_with_replacement: {list(it_8)}")
