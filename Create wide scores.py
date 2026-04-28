"""
Создаёт файл wide_scores.csv с баллами студентов по месяцам.
"""

import csv


class WideScoresCreator:
    """Создаёт wide_scores.csv: строки — студенты, столбцы — месяцы."""

    MONTHS = ["jan", "feb", "mar", "apr", "may", "jun",
              "jul", "aug", "sep", "oct", "nov", "dec"]

    DATA = [
        {"student": "Alice",  "jan": 85, "feb": 90, "mar": 78, "apr": 92, "may": 88, "jun": 76,
                               "jul": 95, "aug": 83, "sep": 89, "oct": 91, "nov": 87, "dec": 94},
        {"student": "Bob",    "jan": 72, "feb": 68, "mar": 75, "apr": 80, "may": 65, "jun": 70,
                               "jul": 78, "aug": 82, "sep": 74, "oct": 79, "nov": 71, "dec": 77},
        {"student": "Carol",  "jan": 91, "feb": 88, "mar": 93, "apr": 87, "may": 95, "jun": 90,
                               "jul": 85, "aug": 92, "sep": 96, "oct": 89, "nov": 94, "dec": 91},
        {"student": "David",  "jan": 60, "feb": 65, "mar": 58, "apr": 70, "may": 63, "jun": 67,
                               "jul": 72, "aug": 55, "sep": 68, "oct": 74, "nov": 61, "dec": 69},
        {"student": "Eve",    "jan": 78, "feb": 82, "mar": 85, "apr": 79, "may": 88, "jun": 83,
                               "jul": 90, "aug": 76, "sep": 84, "oct": 87, "nov": 80, "dec": 86},
    ]

    def __init__(self, output_path: str = "wide_scores.csv"):
        self.output_path = output_path

    def create(self) -> "WideScoresCreator":
        """Записывает wide_scores.csv на диск."""
        fieldnames = ["student"] + self.MONTHS
        with open(self.output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.DATA)
        print(f"Файл создан: {self.output_path}")
        print(f"Студентов: {len(self.DATA)}, Месяцев: {len(self.MONTHS)}")
        return self


if __name__ == "__main__":
    WideScoresCreator("wide_scores.csv").create()