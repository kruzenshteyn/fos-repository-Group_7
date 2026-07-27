# Isolation Forest Baseline — код добавлен в репозиторий

## Расположение файлов

```
corrections/
├── src/
│   ├── generate_sample_data.py      # генерация синтетического датасета
│   └── isolation_forest_baseline.py # полный pipeline (обучение + метрики + сохранение)
├── notebooks/
│   └── 01_isolation_forest_baseline.ipynb  # Jupyter-версия для занятий
├── data/
│   └── smart_home_sensors.csv       # 2000 записей, ~5% аномалий
├── models/
│   ├── isolation_forest.joblib
│   └── scaler.joblib
├── reports/
│   ├── anomaly_report.md
│   └── predictions.csv
└── requirements.txt
```

## Быстрый запуск

```bash
cd corrections   # или корень репозитория после копирования
pip install -r requirements.txt

python src/generate_sample_data.py
python src/isolation_forest_baseline.py
```

Или откройте `notebooks/01_isolation_forest_baseline.ipynb` в Jupyter / VS Code / Colab.

## Результаты baseline (на синтетике)

| Метрика   | Значение |
|-----------|----------|
| Precision | 0.640    |
| Recall    | 0.640    |
| F1-score  | 0.640    |
| Accuracy  | 0.96     |

Модель сохраняется в `models/`, отчёт — в `reports/anomaly_report.md`.

## Соответствие компетенциям КРМ

- **ML-4** — Обучение без учителя (Isolation Forest для anomaly detection)
- **ML-3** — Анализ ошибок и метрик
- **LC-5** — Полный цикл: данные → модель → артефакты

## Что можно улучшить студентам (для более высоких баллов)

1. Временные признаки (rolling statistics, lags)
2. Сравнение с LOF / One-Class SVM / Autoencoder
3. Подбор threshold по PR-кривой
4. Экспорт в ONNX/TFLite + MQTT-паблишер (модуль M4)
5. Data Card и описание происхождения данных
