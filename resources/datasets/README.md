# Датасеты

| Название | Аннотация | Связанные КИМ / компетенции | Доступ | Лицензия | Дата проверки |
|----------|-----------|-----------------------------|--------|----------|---------------|
| **smart_home_sensors.csv** (синтетический, репозиторий) | 2000 записей: temperature, humidity, motion, lux + разметка аномалий (~5 %). Используется для Isolation Forest baseline (ML-4). | М2, М3; ML-4, BD-1 | `data/smart_home_sensors.csv` | MIT (учебный) | 2026-07-27 |
| UCI Appliances Energy Prediction | Временные ряды энергопотребления бытовых приборов (10-мин интервал), 19 735 образцов, 27 признаков. | М2, М3; ML-2, ML-3, BD-1 | [UCI](https://archive.ics.uci.edu/ml/datasets/appliances+energy+prediction) | CC BY 4.0 | 2026-07-27 |
| UCI Occupancy Detection | Присутствие людей по CO₂, температуре, влажности, свету. 20 560 образцов, бинарная классификация. | М2, М3; ML-2, ML-3 | [UCI](https://archive.ics.uci.edu/ml/datasets/occupancy+detection+) | CC BY 4.0 | 2026-07-27 |
| UCI Energy Efficiency | 768 образцов, 8 признаков конструкции здания → отопление/охлаждение. Регрессия для климат-контроля. | М3; ML-2, ML-3 | [UCI](https://archive.ics.uci.edu/ml/datasets/energy+efficiency) | CC BY 4.0 | 2026-07-27 |
| MNIST / Fashion-MNIST (для Edge) | Классические датасеты для демонстрации квантизации и развёртывания на Edge (TFLite / ONNX). | М3, М4; DL-1, LC-5 | [TFDS](https://www.tensorflow.org/datasets) | Public Domain / MIT | 2026-07-27 |
| Home Assistant Community / demo data | Примеры реальных сенсорных потоков и автоматизаций HA. | М2, М4; BD-1, LC-5 | [HA docs / GitHub](https://www.home-assistant.io/) | Apache 2.0 | 2026-07-27 |

## Рекомендации по использованию

- **Разбиение:** для временных рядов — time-based split (не случайный); для табличных — 70/15/15.
- **Смещения:** дисбаланс аномалий, сезонность, пропуски в реальных IoT-потоках.
- **Предобработка:** StandardScaler / MinMax, forward-fill, IQR для выбросов.
- **Связь с кодом:** baseline Isolation Forest — `src/isolation_forest_baseline.py`, `notebooks/01_isolation_forest_baseline.ipynb`.

## Требования к добавлению

Укажите источник, лицензию, состав признаков, целевую переменную, объём, ограничения, возможные смещения и рекомендуемое разбиение.
