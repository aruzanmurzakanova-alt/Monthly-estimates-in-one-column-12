import pandas as pd
import numpy as np

df = pd.read_csv('../data/wide_scores.csv')
matrix = df.iloc[:, 1:].to_numpy()  # без столбца student
print("Матрица:\n", matrix)
print("Форма:", matrix.shape)
