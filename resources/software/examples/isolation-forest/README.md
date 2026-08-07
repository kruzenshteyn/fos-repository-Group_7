# Isolation Forest: воспроизводимый пример

Пример демонстрирует генерацию синтетической телеметрии умного дома, обучение Isolation Forest и оценку обнаружения аномалий.

## Состав

- `src/generate_sample_data.py` — генератор синтетического набора данных;
- `src/isolation_forest_baseline.py` — обучение, оценка и сохранение локальных результатов;
- `notebooks/01_isolation_forest_baseline.ipynb` — учебный ноутбук;
- `requirements.txt` — зависимости примера;
- [входной датасет](../../../datasets/isolation-forest-sample.csv);
- [контрольный отчёт](../../../benchmarks/isolation-forest-report.md).

## Запуск

```bash
cd resources/software/examples/isolation-forest
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python src/isolation_forest_baseline.py
```

Модели и таблицы предсказаний создаются локально и не являются частью репозитория. Код распространяется по лицензии MIT.
