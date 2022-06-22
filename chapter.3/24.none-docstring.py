"""項目24:動的なデフォルト引数を指定するときには None と docstring を使う."""
from datetime import datetime
from time import sleep

from my_libs.decolator import func_name


@func_name
def _log(message: str, when: datetime = datetime.now()) -> None:
    print(f"{when}: {message}")


if __name__ == "__main__":
    _log("Hi there!")
    sleep(0.5)
    _log("Hello again!")
