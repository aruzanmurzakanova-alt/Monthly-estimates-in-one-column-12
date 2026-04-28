"""
Задача 13: Линейный график баллов по месяцам для одного выбранного студента из long-таблицы; PNG.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


class StudentScorePlotter:
    """Строит линейный график баллов по месяцам для одного студента из long-таблицы."""

    MONTH_ORDER = ["jan", "feb", "mar", "apr", "may", "jun",
                   "jul", "aug", "sep", "oct", "nov", "dec"]

    def __init__(self, filepath: str, student_name: str = "Alice"):
        self.filepath = filepath
        self.student_name = student_name
        self.long_df: pd.DataFrame | None = None
        self.student_df: pd.DataFrame | None = None

    def load(self) -> "StudentScorePlotter":
        """Загружает CSV и создаёт long-формат."""
        wide_df = pd.read_csv(self.filepath)
        self.long_df = wide_df.melt(
            id_vars=["student"],
            var_name="month",
            value_name="score"
        )
        return self

    def filter_student(self) -> "StudentScorePlotter":
        """Фильтрует данные для выбранного студента и сортирует по месяцам."""
        if self.long_df is None:
            raise ValueError("Сначала вызовите load()")
        df = self.long_df[self.long_df["student"] == self.student_name].copy()
        df["month"] = pd.Categorical(df["month"], categories=self.MONTH_ORDER, ordered=True)
        self.student_df = df.sort_values("month").reset_index(drop=True)
        return self

    def plot(self, output_path: str = "student_scores.png") -> "StudentScorePlotter":
        """Строит и сохраняет линейный график."""
        if self.student_df is None:
            raise ValueError("Сначала вызовите filter_student()")

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(
            self.student_df["month"],
            self.student_df["score"],
            marker="o", linewidth=2.5, markersize=7,
            color="#2E86AB", markerfacecolor="#E84855"
        )

        # Подписи значений над точками
        for _, row in self.student_df.iterrows():
            ax.annotate(
                str(int(row["score"])),
                (row["month"], row["score"]),
                textcoords="offset points", xytext=(0, 10),
                ha="center", fontsize=9, color="#333333"
            )

        ax.set_title(f"Баллы по месяцам: {self.student_name}", fontsize=14, fontweight="bold", pad=15)
        ax.set_xlabel("Месяц", fontsize=11)
        ax.set_ylabel("Балл", fontsize=11)
        ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
        ax.grid(axis="y", linestyle="--", alpha=0.5)
        ax.set_ylim(
            max(0, self.student_df["score"].min() - 10),
            min(100, self.student_df["score"].max() + 15)
        )
        plt.tight_layout()
        plt.savefig(output_path, dpi=150)
        plt.close()
        print(f"График сохранён: {output_path}")
        return self

    def display(self, output_path: str = "student_scores.png") -> None:
        print(f"=== Задача 13: График баллов для '{self.student_name}' ===")
        print(self.student_df[["month", "score"]].to_string(index=False))
        self.plot(output_path)


if __name__ == "__main__":
    plotter = StudentScorePlotter("wide_scores.csv", student_name="Alice")
    plotter.load().filter_student().display("student_scores.png")