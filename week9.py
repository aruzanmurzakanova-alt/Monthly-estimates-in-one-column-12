import pandas as pd

df = pd.read_csv('../data/wide_scores.csv')
months = list(df.columns[1:])  # без столбца 'student'
print("Заголовки:", df.columns.tolist())
print("Месяцы:", months)