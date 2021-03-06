"""項目39:@classmethodポリモルフィズムを使ってオブジェクトをジェネリックに構築する."""
import os
import random
import shutil
from pathlib import Path
from threading import Thread
from typing import Iterator, Type, TypeVar


class InputData:
    """入力データを表す基底クラス."""

    def read(self) -> str:
        """データの読み込み.

        Raises:
            NotImplementedError: 関数未実装
        """
        raise NotImplementedError


T = TypeVar("T", bound="GenericInputData")


class GenericInputData:
    """入力データを表す基底クラス.

    ジェネリック対応
    """

    def read(self) -> str:
        """データの読み込み.

        Raises:
            NotImplementedError: 関数未実装
        """
        raise NotImplementedError

    @classmethod
    def generate_inputs(
        cls: Type[T], config: dict[str, str]
    ) -> Iterator["PathInputData"]:
        """`GenericInputData` を生成する.

        Args:
            cls (Type[T]): GenericInputData クラスインスタンス
            config (dict[str, str]): 引数名と引数の値のペア

        Raises:
            NotImplementedError: 関数未定義

        Yields:
            Iterator[PathInputData]: ファイル読込クラスインスタンス
        """
        raise NotImplementedError


class PathInputData(GenericInputData):
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

    @classmethod
    def generate_inputs(
        cls: Type[T], config: dict[str, str]
    ) -> Iterator["PathInputData"]:
        """`PathInputData` クラスを生成する.

        Yields:
            Iterator[PathInputData]: ファイル読込クラスインスタンス
        """
        data_dir = config["data_dir"]
        for name in os.listdir(data_dir):
            yield PathInputData(os.path.join(data_dir, name))


class Worker:
    """ファイルデータの改行をカウントする基底クラス."""

    def __init__(self, input_data: PathInputData) -> None:
        """イニシャライザ.

        Args:
            input_data (PathInputData): ファイルデータ
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


U = TypeVar("U", bound="GenericWorker")


class GenericWorker:
    """ファイルデータの改行をカウントする基底クラス.

    ジェネリック対応
    """

    def __init__(self, input_data: PathInputData) -> None:
        """イニシャライザ.

        Args:
            input_data (PathInputData): ファイルデータ
        """
        self.input_data = input_data
        self.result: int = 0

    def map(self) -> None:
        """ファイルデータを初期化する?.

        Raises:
            NotImplementedError: 関数未実装
        """
        raise NotImplementedError

    def reduce(self, other: "GenericWorker") -> None:
        """ファイルデータを追加する.

        Args:
            other (int): ファイルデータ

        Raises:
            NotImplementedError: 関数未実装
        """
        raise NotImplementedError

    @classmethod
    def create_worker(
        cls: Type[U], input_class: "GenericInputData", config: dict[str, str]
    ) -> list[U]:
        """`GenericWorker` クラス生成.

        Args:
            cls (Type[U]): 呼び出し元オブジェクト
            input_class (GenericInputData): ファイル読込クラス
            config (dict[str, str]): 引数名と引数の値のペア

        Returns:
            list[U]: ...
        """
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):
    """ファイルデータの改行数をカウントするクラス."""

    def map(self) -> None:
        """ファイル内の改行数をカウントする."""
        data = self.input_data.read()
        self.result = data.count("\n")

    def reduce(self, other: "GenericWorker") -> None:
        """`other` の改行数を追加する.

        Args:
            other (Worker): 追加するテキストデータ
        """
        self.result += other.result


def _generate_inputs(data_dir: str) -> Iterator[PathInputData]:
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def _create_workers(input_list: Iterator[PathInputData]) -> list[LineCountWorker]:
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers


def _execute(workers: list[LineCountWorker]) -> int:
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result


def mapreduce(data_dir: str) -> int:
    """`data_dir` 内のファイルの改行数をカウントする.

    Args:
        data_dir (str): ファイルが保存されているディレクトリ
    """
    inputs = _generate_inputs(data_dir)
    workers = _create_workers(inputs)
    return _execute(workers)


def _mapreduce_generic(
    worker_class: GenericWorker, input_class: GenericInputData, config: dict[str, str]
) -> int:
    # workers = worker_class.create_worker(input_class, config)
    # return _execute(workers)
    pass


if __name__ == "__main__":

    def _write_test_files(tmpdir: str) -> None:
        """動作確認用のテストファイルを作成する.

        Args:
            tmpdir (str): テストファイルを作成するディレクトリ. 絶対パス指定
        """
        if not os.path.isdir(tmpdir):
            os.makedirs(tmpdir)

        for i in range(100):
            with open(os.path.join(tmpdir, str(i)), "w") as f:
                f.write("\n" * random.randint(0, 100))

    tmpdir = Path(__file__).parent / "tmp_dir"
    _write_test_files(str(tmpdir))

    result = mapreduce(str(tmpdir))
    print(f"There are {result} lines")

    shutil.rmtree(tmpdir)
