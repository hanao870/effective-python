"""項目33:yield from で複数のジェネレータを作る."""
from typing import Callable, Iterator


def _move(period: int, speed: float) -> Iterator[float]:
    for _ in range(period):
        yield speed


def _pause(delay: int) -> Iterator[int]:
    for _ in range(delay):
        yield 0


def _animate() -> Iterator[int | float]:
    for delta in _move(4, 5.0):
        yield delta
    for delta_p in _pause(3):
        yield delta_p
    for delta in _move(2, 3.0):
        yield delta


def _render(delta: float) -> None:
    print(f"Delta: {delta:.1f}")
    # イメージをスクリーン上で動かす


def _run(func: Callable[[], Iterator[int | float]]) -> None:
    for delta in func():
        _render(delta)


def _animate_composed() -> Iterator[int | float]:
    yield from _move(4, 5.0)
    yield from _pause(3)
    yield from _move(2, 3.0)


if __name__ == "__main__":
    _run(_animate)
    print("-" * 50)

    _run(_animate_composed)
