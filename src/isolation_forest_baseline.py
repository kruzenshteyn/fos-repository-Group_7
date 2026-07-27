#!/usr/bin/env python3
"""
Baseline: Isolation Forest для обнаружения аномалий в сенсорных данных умного дома.

Соответствует компетенции КРМ ML-4 (обучение без учителя).
Используется в модуле M3 дисциплины «Прикладной искусственный интеллект для систем умного дома».

Запуск:
    python src/generate_sample_data.py          # создать датасет
    python src/isolation_forest_baseline.py     # обучить и оценить

Артефакты:
    - data/smart_home_sensors.csv
    - models/isolation_forest.joblib
    - reports/anomaly_report.md
"""

from __future__ import annotations

import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    precision_recall_fscore_support,
)
from sklearn.preprocessing import StandardScaler

# ---------------------------------------------------------------------------
# Пути
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "smart_home_sensors.csv"
MODEL_DIR = ROOT / "models"
REPORT_DIR = ROOT / "reports"
MODEL_PATH = MODEL_DIR / "isolation_forest.joblib"
SCALER_PATH = MODEL_DIR / "scaler.joblib"
REPORT_PATH = REPORT_DIR / "anomaly_report.md"

FEATURES = ["temperature", "humidity", "motion", "lux", "hour"]
RANDOM_STATE = 42
CONTAMINATION = 0.05  # ожидаемая доля аномалий


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(
            f"Датасет не найден: {path}\n"
            "Сначала выполните: python src/generate_sample_data.py"
        )
    df = pd.read_csv(path, parse_dates=["timestamp"])
    df["hour"] = df["timestamp"].dt.hour + df["timestamp"].dt.minute / 60.0
    return df


def train_isolation_forest(df: pd.DataFrame) -> tuple[IsolationForest, StandardScaler, np.ndarray]:
    X = df[FEATURES].values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = IsolationForest(
        n_estimators=200,
        contamination=CONTAMINATION,
        max_samples="auto",
        random_state=RANDOM_STATE,
        n_jobs=-1,
    )
    model.fit(X_scaled)

    # decision_function: чем меньше (отрицательнее) — тем более аномально
    scores = model.decision_function(X_scaled)
    preds = model.predict(X_scaled)  # 1 = normal, -1 = anomaly
    preds_binary = (preds == -1).astype(int)

    return model, scaler, preds_binary, scores


def evaluate(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true, y_pred, average="binary", zero_division=0
    )
    cm = confusion_matrix(y_true, y_pred)
    report = classification_report(y_true, y_pred, target_names=["normal", "anomaly"], zero_division=0)
    return {
        "precision": float(precision),
        "recall": float(recall),
        "f1": float(f1),
        "confusion_matrix": cm.tolist(),
        "classification_report": report,
    }


def save_artifacts(model, scaler, metrics: dict, df: pd.DataFrame, preds: np.ndarray):
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)

    # Добавляем предсказания в датасет для анализа
    df_out = df.copy()
    df_out["pred_anomaly"] = preds
    df_out.to_csv(REPORT_DIR / "predictions.csv", index=False)

    # Markdown-отчёт
    cm = metrics["confusion_matrix"]
    md = f"""# Отчёт: Isolation Forest baseline (умный дом)

## Параметры модели
- Алгоритм: Isolation Forest (sklearn)
- n_estimators: 200
- contamination: {CONTAMINATION}
- random_state: {RANDOM_STATE}
- Признаки: {", ".join(FEATURES)}

## Метрики (на размеченных аномалиях)
| Метрика    | Значение |
|------------|----------|
| Precision  | {metrics["precision"]:.3f} |
| Recall     | {metrics["recall"]:.3f} |
| F1-score   | {metrics["f1"]:.3f} |

## Confusion Matrix
```
              pred_normal  pred_anomaly
true_normal      {cm[0][0]:6d}       {cm[0][1]:6d}
true_anomaly     {cm[1][0]:6d}       {cm[1][1]:6d}
```

## Classification Report
```
{metrics["classification_report"]}
```

## Файлы
- Модель: `{MODEL_PATH.relative_to(ROOT)}`
- Scaler: `{SCALER_PATH.relative_to(ROOT)}`
- Предсказания: `reports/predictions.csv`

## Компетенция КРМ
**ML-4** — Обучение без учителя (обнаружение аномалий в сенсорных потоках умного дома).

## Как воспроизвести
```bash
python src/generate_sample_data.py
python src/isolation_forest_baseline.py
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"Отчёт сохранён: {REPORT_PATH}")


def main():
    print("=== Isolation Forest Baseline (Smart Home) ===\n")
    df = load_data()
    print(f"Загружено {len(df)} записей, аномалий (разметка): {df['is_anomaly'].sum()}")

    model, scaler, preds, scores = train_isolation_forest(df)
    metrics = evaluate(df["is_anomaly"].values, preds)

    print("\nМетрики:")
    print(f"  Precision: {metrics['precision']:.3f}")
    print(f"  Recall:    {metrics['recall']:.3f}")
    print(f"  F1:        {metrics['f1']:.3f}")
    print("\nClassification report:")
    print(metrics["classification_report"])

    save_artifacts(model, scaler, metrics, df, preds)
    print(f"\nМодель сохранена: {MODEL_PATH}")
    print("Готово.")


if __name__ == "__main__":
    main()
