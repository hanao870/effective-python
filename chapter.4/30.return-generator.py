"""項目30:リストを返さずにジェネレータを返すことだけを考える."""
from itertools import islice
from pathlib import Path
from typing import Iterator, TextIO


def _index_words(text: str) -> list[int]:
    result = []
    if text:
        result.append(0)

    for index, letter in enumerate(text):
        if letter == " ":
            result.append(index + 1)

    return result


def _index_word_iter(text: str) -> Iterator[int]:
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index + 1


def _index_file(handle: TextIO) -> Iterator[int]:
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == " ":
                yield offset


if __name__ == "__main__":
    address = "Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal."
    result = _index_words(address)
    print(result[:10])

    it = _index_word_iter(address)
    print(next(it))
    print(next(it))

    # ジェネレータのリスト変換
    result = list(_index_word_iter(address))
    print(result[:10])

    file_path = Path(__file__).parent / "address.txt"
    with open(file_path, "r") as f:
        it = _index_file(f)
        results = islice(it, 0, 10)
        print(list(results))
