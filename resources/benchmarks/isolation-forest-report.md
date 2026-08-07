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
- Модель: `models/isolation_forest.joblib`
- Scaler: `models/scaler.joblib`
- Предсказания при воспроизведении: `output/reports/predictions.csv`

## Компетенция КРМ
**ML-4** — Обучение без учителя (обнаружение аномалий в сенсорных потоках умного дома).

## Как воспроизвести
```bash
python src/generate_sample_data.py
python src/isolation_forest_baseline.py
```
