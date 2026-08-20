# Python-библиотеки и программные средства

| Название | Аннотация | Связанные КИМ / компетенции | Доступ / установка | Лицензия | Дата проверки |
|----------|-----------|-----------------------------|--------------------|----------|---------------|
| scikit-learn | Классическое МО: Isolation Forest, preprocessing, метрики, pipelines. | М2, М3; ML-2.2, ML-3.2, ML-4.2/4.3 | `pip install scikit-learn` | BSD-3 | 2026-07-27 |
| pandas / numpy | Работа с табличными и временными данными, feature engineering. | М1–М3; BD-1.2/1.3, PL-1.2 | `pip install pandas numpy` | BSD | 2026-07-27 |
| TensorFlow / Keras или PyTorch | Глубокие сети, LSTM/CNN, экспорт в TFLite / ONNX. | М2, М4; DL-3.1, ML-3.2, LC-5.1 | `pip install tensorflow` / `torch` | Apache 2.0 / BSD | 2026-07-27 |
| paho-mqtt | MQTT-клиент для публикации/подписки сенсорных данных и событий. | М1, М4; BD-3.1, LC-3.1, PL-1.2 | `pip install paho-mqtt` | EPL / EDL | 2026-07-27 |
| joblib | Локальное сохранение/загрузка sklearn-моделей при воспроизведении baseline. | М3; ML-4.2, LC-2.1 | `pip install joblib` | BSD-3 | 2026-07-27 |
| onnxruntime / tflite-runtime | Инференс на Edge без полного фреймворка. | М4; LC-5.1, ML-5.1 | `pip install onnxruntime` | MIT / Apache 2.0 | 2026-07-27 |
| Home Assistant Core | Платформа автоматизации (Docker / venv). | М4; LC-3.1, LC-5.2, AI S-1.1 | [home-assistant.io](https://www.home-assistant.io/) | Apache 2.0 | 2026-07-27 |

## Зависимости воспроизводимого примера

Единственный канонический список находится в [`examples/isolation-forest/requirements.txt`](../examples/isolation-forest/requirements.txt); версии не дублируются здесь, чтобы не создавать второй источник требований.

## Требования к добавлению

Фиксируйте версию, команду установки, назначение, совместимость, лицензию и пример минимального использования.
