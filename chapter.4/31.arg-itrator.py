"""項目31:引数に対してイテレータを使うときには確実さを優先する."""


def _normalize(numbers: list[int]) -> list[float]:
    total = sum(numbers)
    result = []

    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result


if __name__ == "__main__":
    visits = [15, 35, 80]
    percentages = _normalize(visits)
    print(f"{percentages=}, {sum(percentages)=}")
