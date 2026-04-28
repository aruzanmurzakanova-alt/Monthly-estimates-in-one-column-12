"""
Задача 9: Прочитать заголовок, список месяцев как список строк.
"""

import csv


class HeaderReader:
    """Читает заголовок CSV-файла и извлекает список месяцев."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.header: list[str] = []
        self.months: list[str] = []

    def read(self) -> "HeaderReader":
        """Читает файл и извлекает заголовок и месяцы."""
        with open(self.filepath, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            self.header = next(reader)
        # Все столбцы кроме первого ('student') — месяцы
        self.months = self.header[1:]
        return self

    def get_header(self) -> list[str]:
        return self.header

    def get_months(self) -> list[str]:
        return self.months

    def display(self) -> None:
        print("=== Задача 9: Заголовок и месяцы ===")
        print(f"Заголовок: {self.header}")
        print(f"Месяцы ({len(self.months)} шт.): {self.months}")


if __name__ == "__main__":
    reader = HeaderReader("wide_scores.csv")
    reader.read().display()