"""
Задача 9: Загрузить столбец price как массив строк,
найти строки где нет цифр (маска плохих).
"""

import pandas as pd
import numpy as np


class PriceMaskFinder:
    """Загружает CSV и находит плохие строки в колонке price."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.df = None

    def load(self):
        self.df = pd.read_csv(self.filepath, dtype={"price": str})
        return self.df

    def get_price_array(self) -> np.ndarray:
        """Возвращает колонку price как массив строк."""
        return self.df["price"].to_numpy(dtype=str)

    def get_bad_mask(self) -> np.ndarray:
        """
        Маска плохих строк — True там где нет ни одной цифры
        (пустые строки, 'nan', 'abc' и т.д.)
        """
        prices = self.get_price_array()
        mask = np.array([not any(ch.isdigit() for ch in str(p)) for p in prices])
        return mask

    def run(self):
        self.load()
        prices = self.get_price_array()
        bad_mask = self.get_bad_mask()

        print("Массив строк колонки price:")
        print(prices)
        print()
        print("Маска плохих строк (True = плохая):")
        print(bad_mask)
        print()
        print("Плохие строки:")
        bad_df = self.df[bad_mask][["product", "price"]]
        print(bad_df.to_string(index=False))
        print(f"\nВсего плохих: {bad_mask.sum()} из {len(prices)}")


if __name__ == "__main__":
    finder = PriceMaskFinder("prices_raw.csv")
    finder.run()