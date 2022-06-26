"""項目30:リストを返さずにジェネレータを返すことだけを考える."""


def _index_words(text: str) -> list[int]:
    result = []
    if text:
        result.append(0)

    for index, letter in enumerate(text):
        if letter == " ":
            result.append(index + 1)

    return result


if __name__ == "__main__":
    address = "Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal."
    result = _index_words(address)
    print(result[:10])
