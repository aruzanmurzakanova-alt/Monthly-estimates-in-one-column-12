"""
Задача 12: Сохранить prices_clean.csv с числовой колонкой price_clean
и исходными остальными колонками.
"""

import pandas as pd
import numpy as np


class PriceFileSaver:
    """Сохраняет очищенный CSV файл."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.df = None

    def load(self):
        self.df = pd.read_csv(self.filepath, dtype={"price": str})
        return self.df

    def clean_price(self, value: str) -> float | None:
        try:
            cleaned = str(value).replace(" ", "").replace(",", ".")
            return float(cleaned)
        except (ValueError, AttributeError):
            return None

    def build_clean_df(self) -> pd.DataFrame:
        """Строит финальный DataFrame для сохранения."""
        result = self.df.copy()
        result["price_clean"] = [self.clean_price(p) for p in self.df["price"]]
        # Убираем старую сырую колонку price
        result = result.drop(columns=["price"])
        return result

    def save(self, output_path: str = "prices_clean.csv"):
        """Сохраняет очищенный DataFrame в CSV."""
        clean_df = self.build_clean_df()
        clean_df.to_csv(output_path, index=False, encoding="utf-8")
        print(f"✅ Файл сохранён → {output_path}")
        return clean_df

    def run(self):
        self.load()
        clean_df = self.save("prices_clean.csv")
        print()
        print("Содержимое prices_clean.csv:")
        print(clean_df.to_string(index=False))


if __name__ == "__main__":
    saver = PriceFileSaver("prices_raw.csv")
    saver.run()