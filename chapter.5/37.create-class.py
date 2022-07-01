"""項目37:組み込み型の深い入れ子にはせずクラスを作成する."""
from collections import defaultdict, namedtuple


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


class BySubjectGradebook:
    """科目毎に成績のリストを管理するクラス."""

    def __init__(self) -> None:
        """イニシャライザ."""
        # 型アノテーションを記述すると既に複雑...
        # Any で代替可能だが、型が不明...
        # self._grades: dict[str, Any] = {}
        self._grades: dict[str, dict[str, list[int]]] = {}

    def add_student(self, name: str) -> None:
        """生徒を追加する.

        Args:
            name (str): 生徒名
        """
        self._grades[name] = defaultdict(list)

    def report_grade(self, name: str, subject: str, grade: int) -> None:
        """生徒の科目毎の成績を追加する.

        Args:
            name (str): 生徒名
            subject (str): 科目名
            grade (int): 科目の成績
        """
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(grade)

    def average_grade(self, name: str) -> float:
        """生徒の全成績の平均点を計算する.

        Args:
            name (str): 生徒名

        Returns:
            float: 全教科の平均点
        """
        by_subject = self._grades[name]
        total, count = 0, 0
        for grade in by_subject.values():
            total += sum(grade)
            count += len(grade)

        return total / count


class WeightedGradebook:
    """科目毎に成績と重みのリストを管理するクラス."""

    def __init__(self) -> None:
        """イニシャライザ."""
        # 型アノテーションを記述すると複雑さが顕著...
        # Any で代替可能だが、型が不明...
        # self._grades: dict[str, Any] = {}
        self._grades: dict[str, dict[str, list[tuple[int, float]]]] = {}

    def add_student(self, name: str) -> None:
        """生徒を追加する.

        Args:
            name (str): 追加する生徒名
        """
        self._grades[name] = defaultdict(list)

    def repot_grade(self, name: str, subject: str, score: int, weight: float) -> None:
        """生徒の科目毎の成績と重みを追加する.

        Args:
            name (str): 生徒名
            subject (str): 科目名
            score (int): 成績
            weight (float): 重み
        """
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((score, weight))

    def average_grade(self, name: str) -> float:
        """生徒の全成績の平均点を計算する.

        Args:
            name (str): 生徒名

        Returns:
            float: 全成績の平均点
        """
        by_subject = self._grades[name]
        score_sum, score_count = 0.0, 0

        for _, scores in by_subject.items():
            subject_avg, total_weight = 0.0, 0.0
            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight

            score_sum += subject_avg / total_weight
            score_count += 1

        return score_sum / score_count


Grade = namedtuple("Grade", ("score", "weight"))


class Subject:
    """一つの科目を表すクラス."""

    def __init__(self) -> None:
        """イニシャライザ."""
        self._grades: list[Grade] = []

    def report_grade(self, score: int, weight: float) -> None:
        """科目の成績と重みを追加する.

        Args:
            score (int): 成績
            weight (float): 成績の重み
        """
        self._grades.append(Grade(score, weight))

    def average_grade(self) -> float:
        """全成績の平均点を計算する.

        Returns:
            float: 全成績の平均点
        """
        total, total_weight = 0.0, 0.0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


if __name__ == "__main__":
    book = SimpleGradebook()
    book.add_student("Isaac Newton")
    book.report_grade("Isaac Newton", 90)
    book.report_grade("Isaac Newton", 95)
    book.report_grade("Isaac Newton", 85)

    print(book.average_grade("Isaac Newton"))

    book1 = BySubjectGradebook()
    book1.add_student("Albert Einstein")
    book1.report_grade("Albert Einstein", "Math", 75)
    book1.report_grade("Albert Einstein", "Math", 65)
    book1.report_grade("Albert Einstein", "Gym", 90)
    book1.report_grade("Albert Einstein", "Gym", 95)
    print(book1.average_grade("Albert Einstein"))

    book2 = WeightedGradebook()
    book2.add_student("Albert Einstein")
    book2.repot_grade("Albert Einstein", "Math", 75, 0.05)
    book2.repot_grade("Albert Einstein", "Math", 65, 0.15)
    book2.repot_grade("Albert Einstein", "Math", 70, 0.80)
    book2.repot_grade("Albert Einstein", "Gym", 100, 0.40)
    book2.repot_grade("Albert Einstein", "Gym", 85, 0.60)
    print(book2.average_grade("Albert Einstein"))
