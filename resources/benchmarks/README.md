# Бенчмарки и бейзлайны

| Название | Аннотация | Связанные КИМ / компетенции | Доступ | Лицензия | Дата проверки |
|----------|-----------|-----------------------------|--------|----------|---------------|
| Isolation Forest baseline | Обнаружение аномалий на синтетической телеметрии; контрольные Precision/Recall/F1 приведены в отчёте. | М3; ML-4.2, ML-4.3 | [код](../software/examples/isolation-forest/README.md), [отчёт](isolation-forest-report.md) | MIT (код), CC BY 4.0 (отчёт) | 2026-08-07 |
| sklearn Dummy / Linear / Tree baselines | Классические бейзлайны для классификации и регрессии (most_frequent, LinearRegression, DecisionTree). | М3; ML-2, ML-3 | scikit-learn | BSD-3 | 2026-07-27 |
| TFLite Model Benchmark (Edge) | Измерение latency, размера модели и RAM на целевом устройстве (Raspberry Pi / ESP32). | М4; DL-1, LC-5 | [TFLite tools](https://www.tensorflow.org/lite) | Apache 2.0 | 2026-07-27 |
| Home Assistant Energy / Sensor dashboards | Реальные метрики потребления и состояния устройств для сравнения прогнозов. | М2, М4; ML-2, LC-5 | HA Energy dashboard | Apache 2.0 | 2026-07-27 |

## Протокол эксперимента (рекомендуемый)

1. Фиксированный seed (`random_state=42`).
2. Time-based или stratified split.
3. StandardScaler (fit только на train).
4. Метрики: F1 / Precision / Recall (классификация), RMSE / MAE (регрессия), latency + model size (Edge).
5. Сохранение метрик и параметров эксперимента в Markdown/JSON; модель хранится локально как воспроизводимый артефакт.

## Требования к добавлению

Опишите задачу, метрики, протокол эксперимента, базовые решения, требования к воспроизводимости и правила сравнения.
