"""項目19:複数の戻り値では、4個以上の変数なら決してアンパックしない."""
from my_libs.decolator import func_name


@func_name
def _get_stats(numbers: list[int]) -> tuple[int, int]:
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum


@func_name
def _my_function() -> tuple[int, int]:
    return 3, 4


@func_name
def _get_avg_ration(numbers: list[int]) -> list[float]:
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled


@func_name
def _get_stats_new(numbers: list[int]) -> tuple[int, int, float, float, int]:
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count

    sorted_numbers = sorted(numbers)
    middle = count // 2
    if count % 2 == 0:
        lower = sorted_numbers[middle - 1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]

    return minimum, maximum, average, median, count


if __name__ == "__main__":
    lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
    minimum, maximum = _get_stats(lengths)
    print(f"Min: {minimum}, Max: {maximum}")

    # アンパックと関数戻り値の動作確認
    first, second = 1, 2
    print(f"{first=}, {second=}")

    first, second = _my_function()
    print(f"{first=}, {second=}")

    # catch-all アンパック
    longest, *middle, shortest = _get_avg_ration(lengths)
    print(f"Longest:  {longest:>4.0%}")
    print(f"Shortest: {shortest:>4.0%}")
    print(f"Middle:   {middle}")

    # 複数戻り値のアンパック(多すぎ!!!)
    minimum, maximum, average, median, count = _get_stats_new(lengths)
    print(f"Min: {minimum}, Max: {maximum}")
    print(f"Average: {average}, Median: {median}, Count: {count}")
