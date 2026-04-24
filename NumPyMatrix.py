"""
Задача 10: Числовой блок (без столбца student) → матрица NumPy, проверить форму.
"""
 
import pandas as pd
import numpy as np
 
 
class NumPyMatrix:
    """Загружает CSV и превращает числовой блок в матрицу NumPy."""
 
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.df = None
 
    def load(self):
        self.df = pd.read_csv(self.filepath)
        return self.df
 
    def get_months(self) -> list[str]:
        return [col for col in self.df.columns if col != "student"]
 
    def get_matrix(self) -> np.ndarray:
        """Возвращает числовой блок как матрицу NumPy."""
        months = self.get_months()
        return self.df[months].to_numpy()
 
    def run(self):
        self.load()
        matrix = self.get_matrix()
        months = self.get_months()
        students = list(self.df["student"])
 
        print(f"Форма матрицы : {matrix.shape}  ({len(students)} студентов × {len(months)} месяцев)")
        print(f"Тип данных    : {matrix.dtype}")
        print("Матрица баллов:")
        print(matrix)
 
 
if __name__ == "__main__":
    nm = NumPyMatrix("wide_scores.csv")
    nm.run()
