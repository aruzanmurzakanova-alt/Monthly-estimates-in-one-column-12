"""
Задача 12: pivot обратно и сравнить одну ячейку с исходным wide_scores.csv (должно совпасть).
"""

import pandas as pd


class LongToWideVerifier:
    """Выполняет pivot long-таблицы обратно в wide и проверяет корректность."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.original_df: pd.DataFrame | None = None
        self.long_df: pd.DataFrame | None = None
        self.restored_df: pd.DataFrame | None = None

    def load_and_melt(self) -> "LongToWideVerifier":
        """Загружает оригинал и создаёт long-формат."""
        self.original_df = pd.read_csv(self.filepath)
        self.long_df = self.original_df.melt(
            id_vars=["student"],
            var_name="month",
            value_name="score"
        )
        return self

    def pivot_back(self) -> "LongToWideVerifier":
        """Возвращает long-таблицу в wide с помощью pivot."""
        if self.long_df is None:
            raise ValueError("Сначала вызовите load_and_melt()")
        pivoted = self.long_df.pivot(index="student", columns="month", values="score")
        # Восстанавливаем порядок столбцов как в оригинале
        month_order = [c for c in self.original_df.columns if c != "student"]
        self.restored_df = pivoted[month_order].reset_index()
        self.restored_df.columns.name = None
        return self

    def verify_cell(self, student: str, month: str) -> bool:
        """Сравнивает одну ячейку между оригинальным и восстановленным DataFrame."""
        orig_val = self.original_df.loc[
            self.original_df["student"] == student, month
        ].values[0]
        rest_val = self.restored_df.loc[
            self.restored_df["student"] == student, month
        ].values[0]
        return orig_val == rest_val

    def display(self) -> None:
        print("=== Задача 12: Pivot обратно + проверка ячейки ===")
        print(f"Оригинальная форма: {self.original_df.shape}")
        print(f"Восстановленная форма: {self.restored_df.shape}")

        # Проверяем конкретную ячейку
        student, month = "Alice", "mar"
        match = self.verify_cell(student, month)
        orig_val = self.original_df.loc[
            self.original_df["student"] == student, month
        ].values[0]
        print(f"\nПроверка ячейки [{student}][{month}]:")
        print(f"  Оригинал:      {orig_val}")
        print(f"  Восстановлено: {orig_val}")
        print(f"  Совпадает: {'✅ ДА' if match else '❌ НЕТ'}")

        # Проверяем все ячейки
        cols = [c for c in self.original_df.columns if c != "student"]
        orig_sorted = self.original_df.set_index("student")[cols].sort_index()
        rest_sorted = self.restored_df.set_index("student")[cols].sort_index()
        all_match = orig_sorted.equals(rest_sorted)
        print(f"\nВсе ячейки совпадают: {'✅ ДА' if all_match else '❌ НЕТ'}")


if __name__ == "__main__":
    verifier = LongToWideVerifier("wide_scores.csv")
    verifier.load_and_melt().pivot_back().display()