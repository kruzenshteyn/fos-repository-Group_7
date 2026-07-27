# Бенчмарки и бейзлайны

| Название | Аннотация | Связанные КИМ / компетенции | Доступ | Лицензия | Дата проверки |
|----------|-----------|-----------------------------|--------|----------|---------------|
| Isolation Forest baseline (репозиторий) | Unsupervised anomaly detection на smart_home_sensors.csv. Precision/Recall/F1 ≈ 0.64. | М3; ML-4, ML-3 | `src/isolation_forest_baseline.py`, `reports/anomaly_report.md` | MIT | 2026-07-27 |
| sklearn Dummy / Linear / Tree baselines | Классические бейзлайны для классификации и регрессии (most_frequent, LinearRegression, DecisionTree). | М3; ML-2, ML-3 | scikit-learn | BSD-3 | 2026-07-27 |
| TFLite Model Benchmark (Edge) | Измерение latency, размера модели и RAM на целевом устройстве (Raspberry Pi / ESP32). | М4; DL-1, LC-5 | [TFLite tools](https://www.tensorflow.org/lite) | Apache 2.0 | 2026-07-27 |
| Home Assistant Energy / Sensor dashboards | Реальные метрики потребления и состояния устройств для сравнения прогнозов. | М2, М4; ML-2, LC-5 | HA Energy dashboard | Apache 2.0 | 2026-07-27 |

## Протокол эксперимента (рекомендуемый)

1. Фиксированный seed (`random_state=42`).
2. Time-based или stratified split.
3. StandardScaler (fit только на train).
4. Метрики: F1 / Precision / Recall (классификация), RMSE / MAE (регрессия), latency + model size (Edge).
5. Сохранение модели + метрик в JSON / Markdown-отчёт.

## Требования к добавлению

Опишите задачу, метрики, протокол эксперимента, базовые решения, требования к воспроизводимости и правила сравнения.
