"""項目18:__missing__ でキー依存デフォルト値を作成する方法を把握しておく."""
# from collections import defaultdict
from io import BufferedRandom

from my_libs.decolator import func_name


@func_name
def _picture_handle_dict_1() -> None:
    pictures: dict[str, BufferedRandom] = {}
    path = "profile_1234.png"

    if (handle := pictures.get(path)) is None:
        try:
            handle = open(path, "a+b")
        except OSError:
            print(f"Failed to open path {path}")
            raise
        else:
            pictures[path] = handle

    handle.seek(0)
    image_data = handle.read()
    print(image_data)


@func_name
def _picture_handle_dict_2() -> None:
    # _picture_handle_dict_1 の setdefault 版
    pictures: dict[str, BufferedRandom] = {}
    path = "profile_1234.png"

    try:
        handle = pictures.setdefault(path, open(path, "a+b"))
    except OSError:
        print(f"Failed to open path {path}")
        raise
    else:
        handle.seek(0)
        image_data = handle.read()
        print(image_data)


@func_name
def _open_picture(profile_path: str) -> BufferedRandom:
    try:
        return open(profile_path, "a+b")
    except OSError:
        print(f"Failed to open path {profile_path}")
        raise


@func_name
def _picture_handle_dict_3() -> None:
    # _picture_handle_dict_2 の defaultdict 版
    # path = "profile_1234.png"

    # defaultdict のコンストラクタで渡せる関数は引数なしのみ
    # pcitures: dict[str, BufferedRandom] = defaultdict(_open_picture)
    # handle = pcitures[path]
    # handle.seek(0)
    # image_data = handle.read()
    # print(image_data)
    pass


# _open_picture ヘルパー関数を使うためのクラス
class Pictures(dict[str, BufferedRandom]):
    """..."""

    @func_name
    def __missing__(self, key: str) -> BufferedRandom:
        """欠損キーの処理.

        Args:
            key (str): 画像のパス.

        Returns:
            BufferedRandom: `key` のファイルハンドラ
        """
        value = _open_picture(key)
        self[key] = value
        return value


if __name__ == "__main__":
    _picture_handle_dict_1()
    _picture_handle_dict_2()
    _picture_handle_dict_3()

    pictures: dict[str, BufferedRandom] = {}
    path = "profile_1234.png"

    pictures = Pictures()
    # path が存在しないと __missing__ が呼ばれる.
    handle = pictures[path]
    handle.seek(0)
    image_data = handle.read()
    print(image_data)
