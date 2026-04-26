"""
Задача 11: DataFrame с колонками price_raw, price_clean, флаг ошибки парсинга.
"""

import pandas as pd
import numpy as np


class PriceDataFrame:
    """Создаёт DataFrame с сырой ценой, очищенной и флагом ошибки."""

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

    def build_result_df(self) -> pd.DataFrame:
        """
        Строит DataFrame с колонками:
        - price_raw   : исходная строка
        - price_clean : float или None
        - parse_error : True если не удалось распарсить
        """
        price_raw   = self.df["price"].astype(str).values
        price_clean = np.array([self.clean_price(p) for p in price_raw])
        parse_error = np.array([v is None for v in price_clean])

        result = self.df.copy()
        result["price_raw"]   = price_raw
        result["price_clean"] = price_clean
        result["parse_error"] = parse_error
        # Убираем старую колонку price
        result = result.drop(columns=["price"])

        return result

    def run(self):
        self.load()
        result = self.build_result_df()

        print("DataFrame с price_raw, price_clean, parse_error:")
        print(result[["product", "price_raw", "price_clean", "parse_error"]].to_string(index=False))
        print()
        print(f"Всего строк   : {len(result)}")
        print(f"Успешно       : {(~result['parse_error']).sum()}")
        print(f"Ошибок парсинга: {result['parse_error'].sum()}")


if __name__ == "__main__":
    pdf = PriceDataFrame("prices_raw.csv")
    pdf.run()
