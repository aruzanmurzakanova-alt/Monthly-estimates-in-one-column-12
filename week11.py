"""
Задача 11: melt с id_vars=['student'], var_name='month', value_name='score'.
Превращает wide-формат в long-формат.
"""

import pandas as pd


class WideToLong:
    """Применяет pd.melt() для преобразования wide → long."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.df = None

    def load(self):
        self.df = pd.read_csv(self.filepath)
        return self.df

    def melt(self) -> pd.DataFrame:
        """Возвращает таблицу в long-формате: student, month, score."""
        long_df = self.df.melt(
            id_vars=["student"],
            var_name="month",
            value_name="score"
        )
        return long_df

    def run(self):
        self.load()
        long_df = self.melt()
        print("Форма long-таблицы:", long_df.shape)
        print()
        print(long_df.to_string(index=False))


if __name__ == "__main__":
    wtl = WideToLong("wide_scores.csv")
    wtl.run()
