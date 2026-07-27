# Python-библиотеки и программные средства

| Название | Аннотация | Связанные КИМ / компетенции | Доступ / установка | Лицензия | Дата проверки |
|----------|-----------|-----------------------------|--------------------|----------|---------------|
| scikit-learn | Классическое МО: Isolation Forest, preprocessing, метрики, pipelines. | М3; ML-2, ML-3, ML-4 | `pip install scikit-learn` | BSD-3 | 2026-07-27 |
| pandas / numpy | Работа с табличными и временными данными, feature engineering. | М2, М3; BD-1 | `pip install pandas numpy` | BSD | 2026-07-27 |
| TensorFlow / Keras или PyTorch | Глубокие сети, LSTM/CNN, export в TFLite / ONNX. | М3, М4; DL-1 | `pip install tensorflow` / `torch` | Apache 2.0 / BSD | 2026-07-27 |
| paho-mqtt | MQTT-клиент для публикации/подписки сенсорных данных и событий. | М2, М4; BD-1, LC-5 | `pip install paho-mqtt` | EPL / ED L | 2026-07-27 |
| joblib | Сохранение/загрузка sklearn-моделей (используется в baseline). | М3; ML-4 | `pip install joblib` | BSD | 2026-07-27 |
| onnxruntime / tflite-runtime | Инференс на Edge без полного фреймворка. | М4; DL-1, LC-5 | `pip install onnxruntime` | MIT / Apache | 2026-07-27 |
| Home Assistant Core | Платформа автоматизации (Docker / venv). | М4; LC-5, AI S-1 | [home-assistant.io](https://www.home-assistant.io/) | Apache 2.0 | 2026-07-27 |

## Минимальный requirements.txt (репозиторий)

См. корневой `requirements.txt`:

```
numpy>=1.24
pandas>=2.0
scikit-learn>=1.3
matplotlib>=3.7
joblib>=1.3
jupyter>=1.0
```

## Требования к добавлению

Фиксируйте версию, команду установки, назначение, совместимость, лицензию и пример минимального использования.
