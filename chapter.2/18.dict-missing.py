"""項目18:__missing__ でキー依存デフォルト値を作成する方法を把握しておく."""
from io import BufferedRandom

if __name__ == "__main__":
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
