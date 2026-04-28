"""
Задача 11: melt с id_vars=['student'], var_name='month', value_name='score'.
"""

import pandas as pd


class WideToLongConverter:
    """Конвертирует широкий формат CSV в длинный с помощью melt."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.wide_df: pd.DataFrame | None = None
        self.long_df: pd.DataFrame | None = None

    def convert(self) -> "WideToLongConverter":
        """Читает wide-CSV и применяет melt для получения long-формата."""
        self.wide_df = pd.read_csv(self.filepath)
        self.long_df = self.wide_df.melt(
            id_vars=["student"],
            var_name="month",
            value_name="score"
        )
        # Сортируем для удобного просмотра
        self.long_df = self.long_df.sort_values(["student", "month"]).reset_index(drop=True)
        return self

    def get_long_df(self) -> pd.DataFrame:
        if self.long_df is None:
            raise ValueError("Сначала вызовите метод convert()")
        return self.long_df

    def display(self) -> None:
        print("=== Задача 11: Wide → Long (melt) ===")
        print(f"Wide форма: {self.wide_df.shape}")
        print(f"Long форма: {self.long_df.shape}")
        print(f"\nПервые 10 строк long-таблицы:")
        print(self.long_df.head(10).to_string(index=False))


if __name__ == "__main__":
    converter = WideToLongConverter("wide_scores.csv")
    converter.convert().display()