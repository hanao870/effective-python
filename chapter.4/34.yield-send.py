"""項目34:send でジェネレータにデータを注入するのはやめる."""
import math
from typing import Iterator, Optional


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


if __name__ == "__main__":
    _run(_wave(3.0, 8))
