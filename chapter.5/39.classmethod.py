"""項目39:@classmethodポリモルフィズムを使ってオブジェクトをジェネリックに構築する."""
from typing import TextIO


class InputData:
    """入力データを表す基底クラス."""

    def read(self) -> str:
        """データの読み込み.

        Raises:
            NotImplementedError: 関数未実装
        """
        raise NotImplementedError


class PathInputData(InputData):
    """データファイルパスの読込クラス."""

    def __init__(self, path: str) -> None:
        """イニシャライザ.

        Args:
            path (str): ファイルパス
        """
        super().__init__()
        self.path = path

    def read(self) -> str:
        """ファイルデータの読込.

        Returns:
            str: ファイルデータ
        """
        with open(self.path) as f:
            return f.read()


class Worker:
    """ファイルデータを追加する基底クラス."""

    def __init__(self, input_data: TextIO) -> None:
        """イニシャライザ.

        Args:
            input_data (TextIO): ファイルデータ
        """
        self.input_data = input_data
        self.result: int = 0

    def map(self) -> None:
        """ファイルデータを初期化する?.

        Raises:
            NotImplementedError: 関数未実装
        """
        raise NotImplementedError

    def reduce(self, other: "Worker") -> None:
        """ファイルデータを追加する.

        Args:
            other (int): ファイルデータ

        Raises:
            NotImplementedError: 関数未実装
        """
        raise NotImplementedError


class LineCountWorker(Worker):
    """ファイルデータの改行数をカウントするクラス."""

    def map(self) -> None:
        """ファイル内の改行数をカウントする."""
        data = self.input_data.read()
        self.result = data.count("\n")

    def reduce(self, other: "Worker") -> None:
        """`other` の改行数を追加する.

        Args:
            other (Worker): 追加するテキストデータ
        """
        self.result += other.result
