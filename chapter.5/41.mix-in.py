"""項目41:Mix-in クラスで機能合成を考える."""
from typing import Any, TypeVar


class ToDictMixin:
    """シリアライズ辞書の基底クラス."""

    def to_dict(self) -> dict[str, Any]:
        """シリアライズした辞書を返す.

        Returns:
            dict[str, Any]: シリアライズされた辞書
        """
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict: dict[str, Any]) -> dict[str, Any]:
        output = {}

        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)

        return output

    def _traverse(self, key: str, value: Any) -> Any:
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, "__dict__"):
            return self._traverse_dict(value.__dict__)
        else:
            return value


U = TypeVar("U", bound="BinaryTree")


class BinaryTree(ToDictMixin):
    """二分木クラス."""

    def __init__(
        self,
        value: int,
        left: U | None = None,
        right: U | None = None,
    ) -> None:
        """イニシャライザ.

        Args:
            value (int): 値
            left (BinaryTree | None, optional): 辞書値その1
            right (BinaryTree | None, optional): 辞書値その2
        """
        self.value = value
        self.left = left
        self.right = right


V = TypeVar("V", bound="BinaryTreeWithParent")


class BinaryTreeWithParent(BinaryTree):
    """親への参照を保持する二分木クラス."""

    def __init__(
        self,
        value: int,
        left: U | None = None,
        right: U | None = None,
        parent: U | None = None,
    ) -> None:
        """イニシャライザ.

        Args:
            value (int): 値
            left (U | None, optional): 辞書値その1
            right (U | None, optional): 辞書値その2
            parent (U | None, optional): 辞書値その3
        """
        super().__init__(value=value, left=left, right=right)
        self.parent = parent

    def _traverse(self, key: str, value: Any) -> Any:
        if isinstance(value, BinaryTreeWithParent) and key == "parent":
            return value.value  # サイクルを防ぐ
        else:
            return super()._traverse(key, value)


class NamedSubTree(ToDictMixin):
    """Mix-in テストクラス."""

    def __init__(self, name: str, tree_with_parent: "BinaryTreeWithParent") -> None:
        """イニシャライザ.

        Args:
            name (str): 名前
            tree_with_parent (BinaryTreeWithParent): オブジェクト
        """
        self.name = name
        self.tree_with_parent = tree_with_parent


if __name__ == "__main__":
    tree = BinaryTree(
        10,
        left=BinaryTree(7, right=BinaryTree(9)),
        right=BinaryTree(13, left=BinaryTree(11)),
    )
    print(tree.to_dict())

    # root = BinaryTreeWithParent(10)
    # root.left = BinaryTreeWithParent(7, parent=root)
    # root.left.right = BinaryTreeWithParent(9, parent=root.left)
    # print(root.to_dict())

    # my_tree = NamedSubTree("foobar", root.left.right)
    # print(my_tree.to_dict())  # 無限ループにならない
