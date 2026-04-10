"""
Задача 9: Прочитать заголовок CSV, список месяцев как список строк.
"""

import pandas as pd


class HeaderReader:
    """Читает CSV и возвращает список месяцев из заголовка."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.df = None

    def load(self):
        self.df = pd.read_csv(self.filepath)
        return self.df

    def get_months(self) -> list[str]:
        """Все столбцы кроме 'student' — это месяцы."""
        return [col for col in self.df.columns if col != "student"]

    def run(self):
        self.load()
        months = self.get_months()
        print("Все столбцы    :", list(self.df.columns))
        print("Список месяцев :", months)
        print("Кол-во месяцев :", len(months))


if __name__ == "__main__":
    reader = HeaderReader("wide_scores.csv")
    reader.run()
