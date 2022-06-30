"""項目37:組み込み型の深い入れ子にはせずクラスを作成する."""


class SimpleGradebook:
    """学生集団の成績を記録するクラス."""

    def __init__(self) -> None:
        """イニシャライザ."""
        self._grades: dict[str, list[int]] = {}

    def add_student(self, name: str) -> None:
        """生徒を追加する.

        Args:
            name (str): 追加する生徒名
        """
        self._grades[name] = []

    def report_grade(self, name: str, score: int) -> None:
        """生徒の成績を登録する.

        Args:
            name (str): 生徒名
            score (int): 成績
        """
        self._grades[name].append(score)

    def average_grade(self, name: str) -> float:
        """生徒の平均点を取得する.

        Args:
            name (str): 生徒名

        Returns:
            float: 平均点
        """
        grades = self._grades[name]
        return sum(grades) / len(grades)


if __name__ == "__main__":
    book = SimpleGradebook()
    book.add_student("Isaac Newton")
    book.report_grade("Isaac Newton", 90)
    book.report_grade("Isaac Newton", 95)
    book.report_grade("Isaac Newton", 85)

    print(book.average_grade("Isaac Newton"))
