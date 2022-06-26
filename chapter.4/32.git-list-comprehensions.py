"""項目32:大きなリスト内包表記にはジェネレータ式を考える."""
import os
import random
from pathlib import Path

if __name__ == "__main__":
    # テストデータ作成
    file_path = Path(__file__).parent / "my_file.txt"
    if not os.path.isfile(file_path):
        with open(file_path, "w") as f:
            for _ in range(10):
                f.write("a" * random.randint(0, 100))
                f.write("\n")

    # ファイルの1行の長さを保持するリスト内包表記.
    # ファイルサイズが小さい場合のみ有効.
    # ファイルサイズが大きいと、メモリを大量に消費する
    value = [len(x) for x in open(file_path)]
    print(value)

    # リスト内包表記とジェネレータを組み合わせたジェネレータ式
    it = (len(x) for x in open(file_path))
    print(it)

    # for i in range(10):
    #     print(f"{i}: {next(it)}")

    # ジェネレータ式は組み合わせることが可能
    roots = ((x, x**0.5) for x in it)
    for i in range(10):
        print(f"{i}: {next(roots)}")
