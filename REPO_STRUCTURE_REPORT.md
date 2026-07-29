# Отчёт по структуре репозитория  
## `kruzenshteyn/fos-repository-Group_7`

**URL:** https://github.com/kruzenshteyn/fos-repository-Group_7  
**Дата отчёта:** 29 июля 2026  
**Ветка:** `main`  
**Видимость:** public  
**Форк от:** `Vl-Tershch/fos-repository-template`

---

## 1. Общие сведения

| Параметр | Значение |
|----------|----------|
| Назначение | Фонд оценочных средств (ФОС) по дисциплине «Прикладной искусственный интеллект для систем умного дома» |
| Размер репозитория (GitHub) | **~71 086 КБ ≈ 69,4 МБ** |
| Основной язык | Jupyter Notebook (**84,9 %**) |
| Прочие языки | Python 11,1 % · PowerShell 3,5 % · Batchfile 0,5 % |
| Коммитов | **68** |
| Последний push | 28 июля 2026 |
| Создан | 16 июля 2026 |
| Звёзды / форки / issues | 0 / 1 / 0 |
| Лицензия | Other (NOASSERTION) |
| Контрибьюторы (по коммитам) | EvgeniyMR, kruzenshteyn, yuirfa, hhackatons-lab |

---

## 2. Верхний уровень структуры

```text
fos-repository-Group_7/
├── README.md, SYLLABUS.md, COMPETENCIES.md, …
├── M1-Intro_Muratov/
├── M2-Found_Muratov/
├── M3-ML_Models/
├── M4-MK_Baev/
├── M5-Project_Exam/
├── Exam/
├── Project/
├── methodical-guidelines/
├── resources/
├── data/
├── src/
├── notebooks/
├── models/
├── reports/
├── team/
├── review/
└── docs/ (по ссылкам в README)
```

### Корневые документы (ключевые)

| Файл | Назначение |
|------|------------|
| `README.md` | Точка входа, модель измерения, навигация |
| `SYLLABUS.md` | Рабочая программа |
| `COMPETENCIES.md` | Компетенции КРМ 3.0 |
| `LABOR_FUNCTIONS.md` | Трудовые функции / роли |
| `ASSESSMENT_TOOLS.md` | Оценочные средства (КИМ) |
| `MEASUREMENT_MODEL_detailed.md` | Детализированная модель измерения |
| `PROJECT_REQUIREMENTS.md` | Требования к сквозному проекту |
| `COURSE_INFO.md` | Информация о курсе |
| `FIXES_SUMMARY.md` | Сводка исправлений по рецензиям |
| `requirements.txt` | Python-зависимости |
| `КРМ-версия3.0.xlsx` | Компетентностно-ролевая модель |
| `LICENSE.md` / `CONTRIBUTING.md` | Лицензия и вклад |
| `repository-tree.txt` | Дерево репозитория |
| Скрипты `convert_repo_docx.*` | Конвертация DOCX → Markdown |

---

## 3. Учебные модули (M1–M5)

| Модуль | Тема | Файлов (md+данные) | Лекции / практики (по именам) | КИМ / ФОС |
|--------|------|--------------------|-------------------------------|-----------|
| **M1-Intro_Muratov** | Введение и архитектура | ~14 (+ zip, attachments) | 1.1–1.6 (лекции и практики) | kim-01, КИМ/ФОС блока 1 |
| **M2-Found_Muratov** | Фундаментальные технологии ИИ | **~21 md** | 2.1–2.8 (4 лекции + 4 практики) | kim-02, КИМ/ФОС блока 2, глоссарий |
| **M3-ML_Models** | Разработка моделей МО | ~10 md + **1 csv** | 3.1–3.4 (2 лекции + 2 практики) | kim-03, КИМ/ФОС блока 3 |
| **M4-MK_Baev** | Интеграция и Edge AI | ~11 md | Lect_4_1, Lect_4_3, Pract_4_2, Pract_4_4 | kim-04, КИМ/ФОС блока 4 |
| **M5-Project_Exam** | Проект и экзамен | ~6 md | lect_5_1, Pract_5_2 | kim-05, FOS |

**Ориентировочно по модулям:**
- **Лекций (по именам файлов):** ≈ 12–14  
- **Практик:** ≈ 12–14  
- **Markdown в модулях:** ≈ 60+  
- Материалы в основном в **.md** (docx в модулях практически отсутствуют после конвертации)

---

## 4. Датасеты и данные

| Расположение | Файл / набор | Тип |
|--------------|--------------|-----|
| `data/` | `smart_home_sensors.csv` | Синтетический датасет для Isolation Forest |
| `data/` | `krm-v3.0.xlsx` | КРМ (копия/вариант) |
| `data/` | `README.md` | Описание |
| `M3-ML_Models/` | `smart_home(для занятие_3_2).csv` | Учебный CSV |
| `M1-Intro_Muratov/` | `iot_edge_dataset_для занятия 1_3.zip` | Архив для практики Edge |
| `resources/datasets/` | `2_2_dataset_individual+household+electric+power+consumption.zip` | Внешний датасет энергопотребления |
| `resources/datasets/` | `3_2_dataset_smart_home.csv` | Датасет умного дома |
| `resources/datasets/` | `README.md` | Каталог датасетов (UCI и др. по ссылкам) |
| `reports/` | `predictions.csv` | Результаты baseline |

**Итого датасетов/архивов данных в репозитории:** не менее **6–7** файлов (csv/zip) + описания внешних источников в README.

---

## 5. Код, модели, отчёты

| Каталог | Содержимое | Кол-во |
|---------|------------|--------|
| `src/` | `isolation_forest_baseline.py`, `generate_sample_data.py` | **2** Python-скрипта |
| `notebooks/` | `01_isolation_forest_baseline.ipynb` | **1** Jupyter Notebook |
| `models/` | `isolation_forest.joblib`, `scaler.joblib` | **2** сериализованные модели |
| `reports/` | `anomaly_report.md`, `predictions.csv` | **2** артефакта отчёта |
| Корень | `requirements.txt` | зависимости ML-стека |

**Воспроизводимый baseline:** Isolation Forest (unsupervised anomaly detection, компетенция **ML-4**).

---

## 6. Ресурсы (`resources/`)

| Подраздел | Назначение |
|-----------|------------|
| `textbooks/` | Учебники |
| `papers/` | Научные статьи |
| `datasets/` | Датасеты (+ zip/csv) |
| `benchmarks/` | Бенчмарки и бейзлайны |
| `test-banks/` | Банки тестов |
| `problem-banks/` | Банки задач и кейсов |
| `software/python-libs/` | Python-библиотеки |
| `llm-prompts/` | LLM и промпты |
| `other/` | Прочее (в т.ч. справочники) |

В корне `resources/`: `README.md`, `Одноплатные компьютеры.docx`.  
Во всех подразделах — заполненные **README.md** (карточки ресурсов).

---

## 7. Методические материалы и аттестация

| Раздел | Содержимое |
|--------|------------|
| `methodical-guidelines/` | `README.md` + `students/`, `teachers-assessment/`, `teachers-resources/` |
| `Exam/` | `README.md`, `attachments/` |
| `Project/` | `README.md`, `attachments/` |
| `team/` | `README.md`, `images/` |

---

## 8. Сводка по типам файлов (оценка)

| Тип | Оценка количества | Комментарий |
|-----|-------------------|-------------|
| **Markdown (.md)** | **80–100+** | Основной формат документации, лекций, КИМ, README |
| **Python (.py)** | 2 | Baseline Isolation Forest + генератор данных |
| **Jupyter (.ipynb)** | 1 | Учебный notebook |
| **CSV** | 3–4 | Сенсоры, smart home, predictions |
| **ZIP** | 2+ | IoT edge dataset, energy consumption |
| **Joblib / модели** | 2 | Обученные артефакты |
| **XLSX** | 1–2 | КРМ 3.0 |
| **DOCX** | немного | Остатки (например, в resources); модули в основном переведены в md |
| **PPTX / изображения** | несколько | Презентации, картинки в team/attachments |
| **Скрипты (.ps1 / .bat)** | 2+ | Конвертация DOCX |

*Точный полный пересчёт всех вложений в `attachments/` и `media/` по API недоступен без рекурсивного обхода; оценка опирается на видимую структуру GitHub и модули.*

---

## 9. Учебная нагрузка (по программе репозитория)

| Показатель | Значение |
|------------|----------|
| Объём дисциплины | **180 часов (5 ЗЕ)** |
| Модулей | **5** (M1–M5) |
| Форма аттестации | Экзамен + защита проекта |
| Целевые компетенции КРМ | ML-2, ML-4, DL-1, DL-3, DL-4, ML-6, LC-5, AI S-1, BD-1, PL-1, LC-2, SS-1 и др. |
| Роли | ML Engineer (Applied), AI Architect (IoT/Edge), Data Engineer (IoT) |
| Система оценивания | **100 баллов** (кейс, практики, peer-review, экзамен, проект) |

---

## 10. Краткие выводы

1. **Репозиторий — рабочий ФОС**, а не только шаблон: модули M1–M5, методички, ресурсы, код и артефакты моделей.  
2. **Размер ~69 МБ** при **68 коммитах**; доминирует Jupyter/документация (Markdown).  
3. **Лекции и практики** представлены десятками `.md` файлов по блокам 1–5; docx в модулях в основном заменены на markdown.  
4. **Датасеты:** локальные CSV/ZIP + каталог внешних наборов в `resources/datasets`.  
5. **Воспроизводимый код:** Isolation Forest (`src/`, `notebooks/`, `models/`, `reports/`).  
6. **Навигация** строится от корневого `README.md` с моделью измерения и ссылками на модули, КИМ и ресурсы.

---

*Источник данных: публичная страница и API GitHub (`main`, состояние на 28–29.07.2026). Для полной машинной инвентаризации всех вложений рекомендуется локальный `git clone` и `find`/`tree`.*
