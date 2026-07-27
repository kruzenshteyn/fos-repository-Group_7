# Фонд оценочных средств по дисциплине «Прикладной искусственный интеллект для систем умного дома»

> **Статус:** рабочая версия ФОС. Репозиторий содержит модель измерения, КИМ, методические указания, ресурсы и воспроизводимый baseline-код.

Этот репозиторий предназначен для открытого и воспроизводимого представления фонда оценочных средств (ФОС) по дисциплине «Прикладной искусственный интеллект для систем умного дома». Здесь объединены рабочая программа дисциплины, модель измерения результатов обучения, контрольно-измерительные материалы (КИМ), критерии оценивания, методические рекомендации и используемые образовательные ресурсы. Результаты обучения связываются с компетентностно-ролевой моделью в области искусственного интеллекта (КРМ версии 3.0).

## Быстрая навигация

- [Рабочая программа дисциплины (SYLLABUS)](SYLLABUS.md)
- [Компетенции КРМ](COMPETENCIES.md)
- [Трудовые функции / роли](LABOR_FUNCTIONS.md)
- [Модель измерения](MEASUREMENT_MODEL_detailed.md)
- [Оценочные средства (КИМ)](ASSESSMENT_TOOLS.md)
- [Требования к проекту](PROJECT_REQUIREMENTS.md)
- [Методические указания для студентов](methodical-guidelines/students/README.md)
- [Методические указания для преподавателей](methodical-guidelines/teachers-assessment/README.md)
- [Информационные ресурсы](resources/README.md)
- [Команда проекта](team/README.md)

### Модули

- [М1. Введение и архитектура](M1-Intro_Muratov/)
- [М2. Сбор и обработка данных](M2-Found_Muratov/)
- [М3. Разработка моделей МО](M3-ML_Models/)
- [М4. Интеграция и Edge AI](M4-MK_Baev/)
- [М5. Проект и экзамен](M5-Project_Exam/)

## 1. О дисциплине

**Название дисциплины.** Прикладной искусственный интеллект для систем умного дома.

**Цель дисциплины.** Обучающийся должен быть способен в составе междисциплинарной команды самостоятельно спроектировать интеллектуальную функцию умного дома, реализовать прототип, проверить и интегрировать с исполнительными устройствами, оценить качество и обеспечить безопасный контроль человеком.

**Основные задачи.** Формализация бытового сценария как задачи ИИ; выбор архитектуры системы (Device/Edge/Fog/Cloud); разработка и адаптация модели машинного обучения (включая unsupervised, CV, NLP, RL); организация сбора и обработки сенсорных данных; интеграция ИИ-компонентов с системой автоматизации (Home Assistant); анализ ошибок и определение границ применения; документирование архитектуры, данных и результатов; обеспечение безопасности и приватности системы.

**Структура и содержание.** Дисциплина состоит из 5 модулей (180 часов / 5 ЗЕ):

1. **М1. Введение и архитектура ИИ-систем умного дома** (22 ч)
2. **М2. Сбор и обработка данных** (36 ч)
3. **М3. Разработка моделей машинного обучения** (54 ч)
4. **М4. Интеграция и развёртывание (Edge AI + Home Assistant)** (36 ч)
5. **М5. Проектная работа, экзамен и защита** (32 ч)

Обучение включает лекции, практические работы, проектную работу и самостоятельную работу и завершается экзаменом и защитой проекта.

**Пререквизиты и связи с другими дисциплинами.** Базовые знания программирования (Python), основ машинного обучения, электроники/сенсорики, систем управления и автоматики.

**Планируемые результаты обучения.** По завершении дисциплины обучающийся сможет:

- формализовать бытовой сценарий как задачу ИИ;
- выбрать архитектуру системы (Device/Edge/Fog/Cloud);
- разработать и адаптировать модель машинного обучения (включая unsupervised и базовый RL);
- организовать сбор и обработку сенсорных данных с контролем качества;
- интегрировать ИИ-компоненты с платформой автоматизации и Edge-устройствами;
- анализировать ошибки модели, определять границы применения и обеспечивать безопасность;
- документировать архитектуру, данные, модели и результаты.

Полное описание приведено в [SYLLABUS.md](SYLLABUS.md) и [COURSE_INFO.md](COURSE_INFO.md).

## 2. Модель измерения

**Общий объём курса:** 180 часов (5 ЗЕ). **Форма аттестации:** экзамен + защита проекта.  
**Целевые компетенции КРМ:** ML-2, ML-4, DL-1, DL-3, DL-4, ML-6, LC-5, AI S-1, BD-1, PL-1, LC-2, SS-1.  
**Роли:** ML Engineer (Applied), AI Architect (IoT/Edge), Data Engineer (IoT).

| № | Блок / элемент | Компетенция КРМ | Индикатор | Уровень | Дескриптор освоения | Форма | КИМ / материалы | Ресурсы |
|---|----------------|-----------------|-----------|---------|---------------------|-------|-----------------|---------|
| 1 | **Блок 1.** Введение и архитектура умного дома как киберфизической системы ([M1](M1-Intro_Muratov/), 22 ч) | [ML-2](COMPETENCIES.md), [BD-1](COMPETENCIES.md), [LC-5](COMPETENCIES.md), [PL-1](COMPETENCIES.md) | ML-2.1, BD-1.1, LC-5.1, PL-1.2 | Б / С | Различает правила и обучение на данных; выбирает Cloud/Fog/Edge; настраивает MQTT и базовую телеметрию | Л + П (архитектурный кейс) | [M1 README](M1-Intro_Muratov/README.md), [ASSESSMENT_TOOLS.md](ASSESSMENT_TOOLS.md) | [resources/textbooks](resources/textbooks/README.md), лекции М1 |
| 1.1 | Занятие 1.1. Умный дом как киберфизическая система | [ML-2](COMPETENCIES.md) | ML-2.1 | Б | Объясняет эволюцию от автоматизации к ИИ, отличие правил от обучения | Л | [M1-Intro_Muratov/](M1-Intro_Muratov/) | — |
| 1.2 | Занятие 1.2. Сенсоры и данные | [BD-1](COMPETENCIES.md), [ML-2](COMPETENCIES.md) | BD-1.1, ML-2.2 | Б | Классифицирует типы датчиков, описывает шум и проблемы качества данных | Л | [M1-Intro_Muratov/](M1-Intro_Muratov/) | [resources/datasets](resources/datasets/README.md) |
| 1.3 | Занятие 1.3. Архитектура Cloud / Fog / Edge | [LC-5](COMPETENCIES.md), [ML-2](COMPETENCIES.md) | LC-5.1, ML-2.2 | Б / С | Сравнивает задержки и приватность, развёртывает простую модель на Edge | П | [M1-Intro_Muratov/](M1-Intro_Muratov/) | Raspberry Pi / ESP32 |
| 1.4 | Занятие 1.4. MQTT, time-series, Grafana | [BD-3](COMPETENCIES.md), [PL-1](COMPETENCIES.md) | BD-3.1, PL-1.2 | С | Настраивает MQTT-брокер, хранит и визуализирует телеметрию | П | [M1-Intro_Muratov/](M1-Intro_Muratov/), [M2-Found_Muratov/](M2-Found_Muratov/) | Mosquitto, InfluxDB/Grafana |
| 2 | **Блок 2.** Фундаментальные технологии ИИ в контексте умного дома ([M2](M2-Found_Muratov/)–[M3](M3-ML_Models/), 54 ч) | [ML-2](COMPETENCIES.md), [ML-4](COMPETENCIES.md), [DL-3](COMPETENCIES.md), [DL-4](COMPETENCIES.md), [ML-6](COMPETENCIES.md), [PL-1](COMPETENCIES.md) | ML-2.2, ML-4.1, DL-3.1, DL-4.1, ML-6.1, PL-1.2 | Б / С | Строит прогнозы временных рядов, развёртывает CV/NLP/RL-решения с учётом ограничений Edge | Л + П | [M2 README](M2-Found_Muratov/README.md), [M3 README](M3-ML_Models/README.md), [ASSESSMENT_TOOLS.md](ASSESSMENT_TOOLS.md) | [notebooks/](notebooks/), [src/](src/), [resources/benchmarks](resources/benchmarks/README.md) |
| 2.1–2.2 | Прогнозирование (ARIMA / Prophet / LSTM) | [ML-2](COMPETENCIES.md), [ML-4](COMPETENCIES.md), [PL-1](COMPETENCIES.md) | ML-2.2, ML-4.1, PL-1.2 | Б / С | Сравнивает модели на IoT-данных, считает MAE/RMSE | Л + П | [M2-Found_Muratov/](M2-Found_Muratov/), [M3-ML_Models/](M3-ML_Models/) | [resources/datasets](resources/datasets/README.md) |
| 2.3–2.4 | Компьютерное зрение (MobileNet / YOLO-tiny) | [DL-3](COMPETENCIES.md), [LC-5](COMPETENCIES.md) | DL-3.1, LC-5.1 | Б / С | Развёртывает лёгкую CV-модель на Raspberry Pi, измеряет latency | Л + П | [M3-ML_Models/](M3-ML_Models/), [M4-MK_Baev/](M4-MK_Baev/) | TFLite, OpenCV |
| 2.5–2.6 | Голосовой интерфейс (ASR / NLU / HA) | [DL-4](COMPETENCIES.md), [PL-1](COMPETENCIES.md) | DL-4.1, PL-1.2 | Б / С | Собирает pipeline Wake Word → ASR → NLU, интегрирует с Home Assistant | Л + П | [M3-ML_Models/](M3-ML_Models/), [M4-MK_Baev/](M4-MK_Baev/) | Whisper / Rasa |
| 2.7–2.8 | RL для HVAC / освещения | [ML-6](COMPETENCIES.md), [PL-1](COMPETENCIES.md) | ML-6.1, PL-1.2 | Б / С | Формализует reward, обучает агента, сравнивает с правиловым контроллером | Л + П | [M3-ML_Models/](M3-ML_Models/) | Gym / Stable-Baselines |
| 2.9 | Системы рекомендаций в умном доме | [ML-4](COMPETENCIES.md) | ML-4.1 | Б | Описывает content-based / collaborative filtering и privacy-ограничения | Л | [M3-ML_Models/](M3-ML_Models/) | — |
| 3 | **Блок 3.** Специфические задачи умного дома ([M3](M3-ML_Models/), 36 ч) | [ML-4](COMPETENCIES.md), [AI S-1](COMPETENCIES.md), [LC-2](COMPETENCIES.md), [PL-1](COMPETENCIES.md) | ML-4.1, AI S-1.1, LC-2.1, PL-1.2 | Б / С | Обнаруживает аномалии (Isolation Forest / AE), применяет predictive maintenance, учитывает безопасность | Л + П | [M3 README](M3-ML_Models/README.md), [Isolation Forest](src/isolation_forest_baseline.py), [ASSESSMENT_TOOLS.md](ASSESSMENT_TOOLS.md) | [data/smart_home_sensors.csv](data/), [reports/anomaly_report.md](reports/anomaly_report.md) |
| 3.1–3.2 | Anomaly detection / predictive maintenance | [ML-4](COMPETENCIES.md), [LC-2](COMPETENCIES.md), [PL-1](COMPETENCIES.md) | ML-4.1, LC-2.1, PL-1.2 | Б / С | Строит Isolation Forest / Autoencoder, визуализирует аномалии | Л + П | [src/isolation_forest_baseline.py](src/isolation_forest_baseline.py), [notebooks/](notebooks/) | [resources/benchmarks](resources/benchmarks/README.md) |
| 3.3 | Энергоменеджмент / Demand Response | [ML-2](COMPETENCIES.md) | ML-2.2 | Б | Формулирует задачу оптимизации нагрузки с учётом тарифов | Л | [M3-ML_Models/](M3-ML_Models/) | — |
| 3.4 | Безопасность и приватность | [AI S-1](COMPETENCIES.md) | AI S-1 | Б | Описывает federated learning, differential privacy, anomaly behaviour | Л | [M4-MK_Baev/](M4-MK_Baev/), [methodical-guidelines/students/README.md](methodical-guidelines/students/README.md) | [resources/papers](resources/papers/README.md) |
| 4 | **Блок 4.** Практическая реализация и интеграция ([M4](M4-MK_Baev/), 36 ч) | [LC-5](COMPETENCIES.md), [PL-1](COMPETENCIES.md), [AI S-1](COMPETENCIES.md) | LC-5.1, LC-5.2, PL-1.2, AI S-1.2 | Б / С | Квантизует модель, запускает на ESP32/RPi, пишет custom integration для Home Assistant | Л + П | [M4 README](M4-MK_Baev/README.md), [ASSESSMENT_TOOLS.md](ASSESSMENT_TOOLS.md) | [resources/software](resources/software/python-libs/README.md), HA docs |
| 4.1–4.2 | TinyML / TFLite Micro на Edge | [LC-5](COMPETENCIES.md), [PL-1](COMPETENCIES.md) | LC-5.1, PL-1.2 | Б / С | Измеряет latency и энергопотребление на целевом устройстве | Л + П | [M4-MK_Baev/](M4-MK_Baev/) | TFLite Micro, ESP32 |
| 4.3–4.4 | Home Assistant custom integration | [LC-5](COMPETENCIES.md), [PL-1](COMPETENCIES.md) | LC-5.2, PL-1.2 | Б / С | Подключает ML-модель к автоматизациям HA (MQTT / custom component) | Л + П | [M4-MK_Baev/](M4-MK_Baev/) | [resources/other](resources/other/README.md) |
| 5 | **Блок 5.** Проектная работа и этика ([M5](M5-Project_Exam/), 32 ч) | [LC-2](COMPETENCIES.md), [LC-5](COMPETENCIES.md), [SS-1](COMPETENCIES.md) | LC-2.1, LC-5.1, SS-1.1 | С | Реализует полный цикл (данные → модель → Edge → HA), учитывает UX/этику, защищает прототип | П (проект) + дискуссия | [M5 README](M5-Project_Exam/README.md), [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md), [Exam/](Exam/) | [team/](team/README.md), [methodical-guidelines/](methodical-guidelines/students/README.md) |
| 5.1 | Цифровая этика и UX | [SS-1](COMPETENCIES.md) | SS-1.1 | Б | Обсуждает bias, навязчивость уведомлений, контроль пользователя | Л + дискуссия | [M5-Project_Exam/](M5-Project_Exam/) | [resources/papers](resources/papers/README.md) |
| 5.2 | Сквозной проект + защита | [LC-2](COMPETENCIES.md), [LC-5](COMPETENCIES.md), [SS-1](COMPETENCIES.md) | LC-2.1, LC-5.1, SS-1.1 | С | Демонстрирует работающий прототип и документацию | П + защита | [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md) | [data/](data/), [src/](src/) |
| — | **Промежуточная аттестация** | Все основные компетенции курса | Итоговый уровень по индикаторам | Б / С | Теория по всем блокам + защита проекта | Экзамен + защита | [Exam/](Exam/), [M5-Project_Exam/](M5-Project_Exam/) | — |

## 3. Контрольно-измерительные материалы

- [Модуль 1](M1-Intro_Muratov/) — архитектурный кейс, лекции и практики по Device/Edge/Fog/Cloud
- [Модуль 2](M2-Found_Muratov/) — практики с сенсорными данными, MQTT, Data Card
- [Модуль 3](M3-ML_Models/) — модели МО/DL, Isolation Forest baseline, unsupervised, CV, NLP, RL
- [Модуль 4](M4-MK_Baev/) — интеграция с Home Assistant, Edge-развёртывание, безопасность
- [Проектная работа](Project/) / [М5](M5-Project_Exam/) — сквозной прототип, peer-review, защита
- [Экзамен](Exam/) — теория (40 %) + практика (60 %)

Каждый КИМ содержит назначение, проверяемые результаты, условия выполнения, материалы задания, формат сдачи, критерии и шкалу оценивания, правила использования внешних ресурсов и генеративного ИИ.

**Воспроизводимый код:** `src/isolation_forest_baseline.py`, `notebooks/01_isolation_forest_baseline.ipynb`, датасет `data/smart_home_sensors.csv`.

## 4. Итоговая оценка

Единая 100-балльная система:

| Компонент | Баллы |
|-----------|-------|
| Архитектурный кейс (М1) | 10 |
| Практики М2 (данные) | 15 |
| Практики М3 (модели) | 15 |
| Практики М4 (Edge/HA) | 10 |
| Peer-review | 5 |
| Экзамен | 20 |
| Защита проекта | 25 |
| **Итого** | **100** |

**Шкала перевода:**

| Баллы | Оценка |
|-------|--------|
| 86–100 | Отлично |
| 71–85 | Хорошо |
| 56–70 | Удовлетворительно |
| 0–55 | Неудовлетворительно |

Минимальный проходной балл — **60**.  
Правило нижнего порога по проекту: не менее 4 баллов (по 10-балльной рубрике) по осям «программное решение» и «документация» (при наличии).

## 5. Методические материалы

- [Рекомендации обучающимся](methodical-guidelines/students/README.md) — маршрут, среда, сдача, peer-review, академическая честность и LLM
- [Рекомендации преподавателям по оцениванию](methodical-guidelines/teachers-assessment/README.md) — сценарии контроля, рубрики, апелляции
- [Информационные ресурсы](resources/README.md) — учебники, статьи, датасеты, бенчмарки, библиотеки, промпты

## 6. Структура репозитория

```text
.
├── README.md
├── SYLLABUS.md
├── COMPETENCIES.md
├── LABOR_FUNCTIONS.md
├── ASSESSMENT_TOOLS.md
├── PROJECT_REQUIREMENTS.md
├── MEASUREMENT_MODEL_detailed.md
├── requirements.txt
├── LICENSE
├── M1-Intro_Muratov/
├── M2-Found_Muratov/
├── M3-ML_Models/
├── M4-MK_Baev/
├── M5-Project_Exam/
├── Exam/
├── Project/
├── methodical-guidelines/
│   ├── students/
│   └── teachers-assessment/
├── resources/
│   ├── textbooks/
│   ├── papers/
│   ├── datasets/
│   ├── benchmarks/
│   ├── test-banks/
│   ├── problem-banks/
│   ├── llm-prompts/
│   ├── software/python-libs/
│   └── other/
├── data/
├── src/
├── notebooks/
├── models/
├── reports/
└── team/
```

## 7. Порядок заполнения / доработки

1. Заполнены РПД (SYLLABUS) и проверяемые результаты обучения.
2. Выбраны роли КРМ: ML Engineer, AI Architect, Data Engineer (IoT).
3. Для каждого результата указаны индикаторы и уровни (Б/С/П).
4. Заполнена модель измерения (MEASUREMENT_MODEL_detailed.md).
5. Созданы КИМ и рубрики по модулям; добавлен воспроизводимый код.
6. Согласована система итогового балла (100 баллов).
7. Заполнены ресурсы, сведения о команде и методические указания.

## 8. Команда

Сведения об авторах, ролях и вкладе участников — в разделе [«Команда проекта»](team/README.md).  
Основные авторы модулей: Муратов (М1–М2), Баев (М4); корневые документы, методички и код — коллективно.

## 9. Лицензия

Предлагаемая лицензия для открытых образовательных материалов — **Creative Commons Attribution 4.0 International (CC BY 4.0)** или MIT (для кода). Перед публикацией согласуйте выбор лицензии с правообладателем и заполните файл [LICENSE](LICENSE).

---
*Версия с исправлениями по экспертным рецензиям: 27.07.2026.*
