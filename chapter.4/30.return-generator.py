"""項目30:リストを返さずにジェネレータを返すことだけを考える."""


from typing import Iterator


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


if __name__ == "__main__":
    address = "Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal."
    result = _index_words(address)
    print(result[:10])

    it = _index_word_iter(address)
    print(next(it))
    print(next(it))
