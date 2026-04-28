"""
Задача 10: Числовой блок (без имени студента) в матрицу NumPy, проверить форму.
"""

import numpy as np
import pandas as pd


class ScoreMatrixLoader:
    """Загружает числовой блок CSV в матрицу NumPy."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.matrix: np.ndarray | None = None
        self.students: list[str] = []
        self.months: list[str] = []

    def load(self) -> "ScoreMatrixLoader":
        """Читает CSV и преобразует числовые столбцы в матрицу NumPy."""
        df = pd.read_csv(self.filepath)
        self.students = df["student"].tolist()
        self.months = [col for col in df.columns if col != "student"]
        self.matrix = df[self.months].to_numpy(dtype=float)
        return self

    def get_matrix(self) -> np.ndarray:
        if self.matrix is None:
            raise ValueError("Сначала вызовите метод load()")
        return self.matrix

    def display(self) -> None:
        print("=== Задача 10: NumPy-матрица баллов ===")
        print(f"Форма матрицы: {self.matrix.shape}  "
              f"({self.matrix.shape[0]} студентов × {self.matrix.shape[1]} месяцев)")
        print(f"Тип данных: {self.matrix.dtype}")
        print("Матрица:")
        print(self.matrix)


if __name__ == "__main__":
    loader = ScoreMatrixLoader("wide_scores.csv")
    loader.load().display()