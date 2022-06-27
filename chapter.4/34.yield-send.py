"""項目34:send でジェネレータにデータを注入するのはやめる."""
import math
from typing import Generator, Iterator, Optional


def _wave(amplitude: float, steps: int) -> Iterator[float]:
    step_size = 2 * math.pi / steps

    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        yield output


def _transmit(output: Optional[float]) -> None:
    if output is None:
        print("Output is None")
    else:
        print(f"Output: {output:>5.1f}")


def _run(it: Iterator[float]) -> None:
    for output in it:
        _transmit(output)


def _my_generator() -> Generator[int, Optional[str], None]:
    received = yield 1
    print(f"{received=}")


def _wave_modulating(steps: int) -> Generator[float, Optional[float], None]:
    step_size = 2 * math.pi / steps
    amplitude = yield 0.0  # 最初の振幅を受け取る

    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)

        if amplitude is None:
            amplitude = 0.0

        output = amplitude * fraction
        amplitude = yield output  # 次の振幅を受け取る


def _run_modulating(it: Generator[float, Optional[float], None]) -> None:
    amplitudes = [None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    for amplitude in amplitudes:
        output = it.send(amplitude)
        _transmit(output)


def _complex_wave() -> Iterator[float]:
    yield from _wave(7.0, 3)
    yield from _wave(2.0, 4)
    yield from _wave(10.0, 5)


if __name__ == "__main__":
    _run(_wave(3.0, 8))

    it = iter(_my_generator())
    output = next(it)  # 最初のジェネレータ出力を取得
    print(f"{output=}")

    try:
        next(it)  # 終わるまでジェネレータ実行
    except StopIteration:
        pass
    else:
        assert False

    it = iter(_my_generator())
    # 最初のジェネレータ出力取得
    # yield 式がないため None 以外では例外が送出される
    output = it.send(None)
    print(f"{output=}")

    try:
        it.send("hello!")  # ジェネレータに値を送信
    except StopIteration:
        pass

    _run_modulating(_wave_modulating(12))
    print("-" * 50)

    _run(_complex_wave())
    print("-" * 50)
