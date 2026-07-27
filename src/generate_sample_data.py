#!/usr/bin/env python3
"""
Генерация синтетического датасета сенсоров умного дома
для демонстрации Isolation Forest (ML-4: обучение без учителя).

Сценарий: комната с датчиками температуры, влажности, движения, освещённости.
Аномалии: резкие скачки температуры, длительное движение ночью и т.п.
"""

import numpy as np
import pandas as pd
from pathlib import Path

RNG = np.random.default_rng(42)
N_SAMPLES = 2000
OUTPUT = Path(__file__).resolve().parent.parent / "data" / "smart_home_sensors.csv"


def generate():
    timestamps = pd.date_range("2026-01-01", periods=N_SAMPLES, freq="5min")
    hour = (timestamps.hour + timestamps.minute / 60.0).to_numpy(dtype=float)

    # Нормальное поведение
    temperature = 21 + 2 * np.sin(2 * np.pi * hour / 24) + RNG.normal(0, 0.4, N_SAMPLES)
    humidity = 45 + 8 * np.sin(2 * np.pi * (hour - 6) / 24) + RNG.normal(0, 2, N_SAMPLES)
    motion = (RNG.random(N_SAMPLES) < 0.12).astype(float)  # ~12% времени движение
    lux = np.clip(300 * np.sin(np.pi * hour / 24) ** 2 + RNG.normal(0, 30, N_SAMPLES), 0, 800)

    # Внедряем аномалии (~5%)
    n_anom = int(0.05 * N_SAMPLES)
    anom_idx = RNG.choice(N_SAMPLES, size=n_anom, replace=False)

    # Типы аномалий
    for i, idx in enumerate(anom_idx):
        kind = i % 4
        if kind == 0:  # резкий скачок температуры
            temperature[idx] += RNG.choice([-8, 10])
        elif kind == 1:  # аномально высокая влажность
            humidity[idx] = RNG.uniform(85, 98)
        elif kind == 2:  # движение глубокой ночью + низкая освещённость
            if 1 <= hour[idx] <= 4:
                motion[idx] = 1.0
                lux[idx] = RNG.uniform(0, 15)
        else:  # выброс освещённости
            lux[idx] = RNG.uniform(900, 1200)

    df = pd.DataFrame({
        "timestamp": timestamps,
        "temperature": np.round(temperature, 2),
        "humidity": np.round(humidity, 1),
        "motion": motion.astype(int),
        "lux": np.round(lux, 1),
        "is_anomaly": 0,
    })
    df.loc[anom_idx, "is_anomaly"] = 1

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)
    print(f"Сохранён датасет: {OUTPUT}  ({len(df)} строк, {df['is_anomaly'].sum()} аномалий)")
    return df


if __name__ == "__main__":
    generate()
