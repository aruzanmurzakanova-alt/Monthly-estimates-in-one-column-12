"""
Задача 14: POST wide CSV → JSON long (список записей) как в н.11.
FastAPI сервер доступен только локально на http://localhost:8888
"""

from __future__ import annotations

import io

import pandas as pd
import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse


app = FastAPI(title="Задача 14: Wide CSV → Long JSON")


class WideToLongConverter:
    """Конвертирует wide CSV в long-формат."""

    @staticmethod
    def convert(csv_content: str) -> list[dict]:
        df = pd.read_csv(io.StringIO(csv_content))
        if "student" not in df.columns:
            raise ValueError("CSV должен содержать столбец 'student'")
        long_df = df.melt(id_vars=["student"], var_name="month", value_name="score")
        long_df = long_df.sort_values(["student", "month"]).reset_index(drop=True)
        return long_df.to_dict(orient="records")


class WideToLongAPI:
    """Регистрирует маршруты FastAPI."""

    def __init__(self, app: FastAPI):
        self.app = app
        self.converter = WideToLongConverter()
        self._register_routes()

    def _register_routes(self) -> None:
        self.app.get("/")(self._index)
        self.app.post("/convert")(self._convert)

    def _index(self) -> dict:
        return {
            "description": "Wide CSV → Long JSON конвертер",
            "endpoints": {
                "GET  /": "эта страница",
                "POST /convert": "отправь CSV файл, получи JSON long-формат",
            },
            "docs": "http://localhost:8888/docs"
        }

    async def _convert(self, file: UploadFile = File(...)) -> JSONResponse:
        content = await file.read()
        try:
            records = self.converter.convert(content.decode("utf-8"))
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        return JSONResponse(content=records)


# Регистрируем маршруты
WideToLongAPI(app)


if __name__ == "__main__":
    print("=== Задача 14: Wide CSV → Long JSON API ===")
    print("Сервер: http://localhost:8888")
    print("Документация: http://localhost:8888/docs  ← открой в браузере!")
    print("Остановить: Ctrl + C")
    print("-" * 50)
    uvicorn.run(app, host="127.0.0.1", port=8888)