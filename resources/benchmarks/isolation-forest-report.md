# Отчёт: Isolation Forest baseline (умный дом)

## Параметры модели
- Алгоритм: Isolation Forest (sklearn)
- n_estimators: 200
- contamination: 0.05
- random_state: 42
- Признаки: temperature, humidity, motion, lux, hour

## Метрики (на размеченных аномалиях)
| Метрика    | Значение |
|------------|----------|
| Precision  | 0.640 |
| Recall     | 0.640 |
| F1-score   | 0.640 |

## Confusion Matrix
```
              pred_normal  pred_anomaly
true_normal        1864           36
true_anomaly         36           64
```

## Classification Report
```
              precision    recall  f1-score   support

      normal       0.98      0.98      0.98      1900
     anomaly       0.64      0.64      0.64       100

    accuracy                           0.96      2000
   macro avg       0.81      0.81      0.81      2000
weighted avg       0.96      0.96      0.96      2000

```

## Файлы
- Модель при воспроизведении: `output/models/isolation_forest.joblib`
- Scaler при воспроизведении: `output/models/scaler.joblib`
- Предсказания при воспроизведении: `output/reports/predictions.csv`

## Компетенция КРМ
**ML-4.2** — выявление аномалий; **ML-4.3** — оценивание результата обучения без учителя.

## Как воспроизвести
```bash
python resources/software/examples/isolation-forest/src/isolation_forest_baseline.py
```

Сценарий читает канонический набор `resources/datasets/isolation-forest-sample.csv`. Генератор `src/generate_sample_data.py` сохраняет альтернативный синтетический набор в игнорируемый каталог `output/` и не перезаписывает контрольный набор.
