# Датасеты

| Название | Аннотация | Связанные КИМ / компетенции | Доступ | Лицензия | Дата проверки |
|----------|-----------|-----------------------------|--------|----------|---------------|
| **isolation-forest-sample.csv** (синтетический) | 2000 записей: temperature, humidity, motion, lux и разметка аномалий (~5 %). | М3; ML-4.2, ML-4.3 | [файл](isolation-forest-sample.csv) | CC BY 4.0 | 2026-08-07 |
| **3_2_dataset_smart_home.csv** | Телеметрия для практической работы М3 по обнаружению аномалий. | М3; ML-4.2, PL-1.2 | [файл](3_2_dataset_smart_home.csv) | Учебное использование; источник описывается в задании | 2026-08-07 |
| **Individual household electric power consumption** | Архив временного ряда энергопотребления для практики М2. | М2; ML-2.2, ML-3.2 | [архив](2_2_dataset_individual+household+electric+power+consumption.zip) | Условия исходного набора UCI | 2026-08-07 |
| UCI Appliances Energy Prediction | Временные ряды энергопотребления бытовых приборов (10-мин интервал), 19 735 образцов, 27 признаков. | М2, М3; ML-2, ML-3, BD-1 | [UCI](https://archive.ics.uci.edu/ml/datasets/appliances+energy+prediction) | CC BY 4.0 | 2026-07-27 |
| UCI Occupancy Detection | Присутствие людей по CO₂, температуре, влажности, свету. 20 560 образцов, бинарная классификация. | М2, М3; ML-2, ML-3 | [UCI](https://archive.ics.uci.edu/ml/datasets/occupancy+detection+) | CC BY 4.0 | 2026-07-27 |
| UCI Energy Efficiency | 768 образцов, 8 признаков конструкции здания → отопление/охлаждение. Регрессия для климат-контроля. | М3; ML-2, ML-3 | [UCI](https://archive.ics.uci.edu/ml/datasets/energy+efficiency) | CC BY 4.0 | 2026-07-27 |
| MNIST / Fashion-MNIST (для Edge) | Классические датасеты для демонстрации квантизации и развёртывания на Edge (TFLite / ONNX). | М3, М4; DL-1, LC-5 | [TFDS](https://www.tensorflow.org/datasets) | Public Domain / MIT | 2026-07-27 |
| Home Assistant Community / demo data | Примеры реальных сенсорных потоков и автоматизаций HA. | М2, М4; BD-1, LC-5 | [HA docs / GitHub](https://www.home-assistant.io/) | Apache 2.0 | 2026-07-27 |

## Рекомендации по использованию

- **Разбиение:** для временных рядов — time-based split (не случайный); для табличных — 70/15/15.
- **Смещения:** дисбаланс аномалий, сезонность, пропуски в реальных IoT-потоках.
- **Предобработка:** StandardScaler / MinMax, forward-fill, IQR для выбросов.
- **Связь с кодом:** [воспроизводимый пример Isolation Forest](../software/examples/isolation-forest/README.md).

## Требования к добавлению

Укажите источник, лицензию, состав признаков, целевую переменную, объём, ограничения, возможные смещения и рекомендуемое разбиение.
