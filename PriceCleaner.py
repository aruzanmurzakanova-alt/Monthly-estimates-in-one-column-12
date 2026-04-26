"""
Задача 10: Функция — убрать пробелы, заменить запятую на точку,
astype(float) для валидных строк.
"""

import pandas as pd
import numpy as np


class PriceCleaner:
    """Очищает строки с ценами и конвертирует в float."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.df = None

    def load(self):
        self.df = pd.read_csv(self.filepath, dtype={"price": str})
        return self.df

    def clean_price(self, value: str) -> float | None:
        """
        Очищает одну строку цены:
        1. Убирает пробелы
        2. Заменяет запятую на точку
        3. Конвертирует в float
        Возвращает None если строка невалидна.
        """
        try:
            cleaned = str(value).replace(" ", "").replace(",", ".")
            return float(cleaned)
        except (ValueError, AttributeError):
            return None

    def clean_all(self) -> np.ndarray:
        """Применяет clean_price ко всей колонке price."""
        return np.array([self.clean_price(p) for p in self.df["price"]])

    def run(self):
        self.load()

        print("Примеры очистки:")
        test_values = ["12,5", "1 234,56", "0,99", "abc", "", "15 999,99"]
        for v in test_values:
            result = self.clean_price(v)
            print(f"  '{v}' → {result}")

        print()
        cleaned = self.clean_all()
        print("Вся колонка после очистки:")
        for product, raw, clean in zip(self.df["product"], self.df["price"], cleaned):
            print(f"  {product:10s} | '{raw}' → {clean}")


if __name__ == "__main__":
    cleaner = PriceCleaner("prices_raw.csv")
    cleaner.run()