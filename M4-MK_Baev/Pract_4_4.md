Практическое занятие: Разработка Custom Integration для Home Assistant с ML-моделью детекции аномалий
Дисциплина: Промышленная разработка систем ИИ
Компетенции: LC‑5, LC‑5.2 (средний уровень); PL‑1, PL‑1.2 (средний уровень)
Продолжительность: 4 академических часа

1. Цели занятия
После выполнения практической работы студент сможет:

Разработать полноценную Custom Integration для Home Assistant на Python

Интегрировать ML-модель детекции аномалий (на базе Isolation Forest) в экосистему умного дома

Настроить Data Update Coordinator для периодического сбора и обработки данных

Создать ML-пайплайн, автоматически запускающий инференс при изменении состояния датчиков

Применить инженерные практики из компетенции LC‑5.2: выбор инструментов управления данными, контроль качества, организация доступа

Связь с компетенциями:

Компетенция	Индикатор	Уровень	Что отрабатывается
LC‑5	LC‑5.2	Средний	Выбор инструментов управления данными (координатор, MQTT, REST API), настройка доступа и контроля качества
PL‑1	PL‑1.2	Средний	Выбор и применение библиотек Python (scikit-learn, asyncio, aiohttp) для ML и интеграции
2. Необходимое ПО и подготовка среды
Программное обеспечение
Компонент	Версия	Назначение
Home Assistant	2025.7+	Платформа автоматизации
Python	3.10+	Язык разработки интеграции
VS Code	Latest	Среда разработки
DevContainer	—	Изолированная среда для разработки
Подготовка среды разработки
Вариант 1: GitHub Codespaces (рекомендуется для начинающих)

Перейдите по ссылке на шаблон интеграции

Нажмите "Use this template" → создайте свой репозиторий

Откройте репозиторий в Codespaces

Вариант 2: Локальная разработка с DevContainer

bash
git clone https://github.com/jpawlowski/hacs.integration_blueprint.git
cd hacs.integration_blueprint
# Открыть в VS Code с установленным расширением Dev Containers
Вариант 3: Ручная настройка (для полного контроля)

bash
# Установка Home Assistant в виртуальном окружении
python3 -m venv ha_env
source ha_env/bin/activate
pip install homeassistant

# Создание директории для custom_components
mkdir -p config/custom_components
Важно: Используйте шаблон, а не форк! Форк копирует всю историю коммитов (~800 коммитов), шаблон даёт чистый старт.

3. Часть 1. Создание структуры Custom Integration (25 минут)
3.1. Генерация базовой структуры через scaffold
Home Assistant предоставляет скрипт для генерации каркаса интеграции:

bash
python3 -m script.scaffold integration
Следуйте инструкциям:

Введите домен (например, anomaly_detector)

Введите название (например, Anomaly Detector)

Структура созданной интеграции:

text
custom_components/anomaly_detector/
├── __init__.py          # Настройка и выгрузка интеграции
├── manifest.json        # Метаданные (версия, зависимости)
├── config_flow.py       # Мастер настройки через UI
├── const.py             # Константы
├── coordinator/         # Data Update Coordinator
│   ├── __init__.py
│   ├── base.py          # Основной класс координатора
│   └── data_processing.py # Обработка и валидация данных
├── sensor.py            # Реализация сенсоров
├── services.yaml        # Описание пользовательских сервисов
├── translations/        # Локализация
│   └── en.json
└── diagnostics.py       # Диагностическая информация
3.2. Настройка manifest.json
json
{
  "domain": "anomaly_detector",
  "name": "Anomaly Detector",
  "version": "1.0.0",
  "requirements": [
    "scikit-learn>=1.2.0",
    "numpy>=1.24.0",
    "pandas>=2.0.0"
  ],
  "dependencies": [],
  "codeowners": ["@yourusername"],
  "config_flow": true,
  "documentation": "https://example.com/docs",
  "issue_tracker": "https://github.com/user/repo/issues"
}
Внимание: Кастомные интеграции обязаны содержать ключ version в manifest.json.

3.3. Реализация init.py
python
"""Anomaly Detector integration for Home Assistant."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .coordinator import AnomalyDetectorCoordinator

PLATFORMS = [Platform.SENSOR]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Настройка интеграции из config entry."""
    hass.data.setdefault(DOMAIN, {})
    
    # Инициализация координатора
    coordinator = AnomalyDetectorCoordinator(hass, entry)
    await coordinator.async_config_entry_first_refresh()
    
    hass.data[DOMAIN][entry.entry_id] = coordinator
    
    # Пересылка платформ
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Выгрузка интеграции."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok
4. Часть 2. Реализация ML-модели детекции аномалий (25 минут)
4.1. Выбор модели: Isolation Forest
Для детекции аномалий в данных умного дома выберем Isolation Forest — алгоритм, эффективно работающий с многомерными данными и не требующий разметки аномалий.

Почему Isolation Forest:

Работает без размеченных аномалий (обучение на "нормальных" данных)

Эффективен для многомерных данных

Хорошо масштабируется

Даёт интерпретируемую оценку аномальности

4.2. Код ML-модели
ml_model.py :

python
"""ML модель для детекции аномалий."""

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

class AnomalyDetectorModel:
    """Класс для обучения и инференса модели детекции аномалий."""
    
    def __init__(self, model_path: str = None):
        self.model = None
        self.model_path = model_path
        self.feature_names = [
            "temperature", "humidity", "power_consumption",
            "motion_count", "light_level"
        ]
        
    def load_model(self) -> bool:
        """Загрузка обученной модели из файла."""
        if self.model_path and os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
            return True
        return False
    
    def train(self, data: pd.DataFrame) -> None:
        """Обучение модели на исторических данных."""
        features = data[self.feature_names].values
        self.model = IsolationForest(
            contamination=0.05,  # ожидаемая доля аномалий
            random_state=42,
            n_estimators=100
        )
        self.model.fit(features)
        
        # Сохранение модели
        if self.model_path:
            os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
            joblib.dump(self.model, self.model_path)
    
    def predict(self, data: dict) -> dict:
        """
        Инференс модели для одного наблюдения.
        
        Возвращает:
        - anomaly_score: float (0..1) — степень аномальности
        - is_anomaly: bool — является ли аномалией
        - features: dict — использованные признаки
        """
        if self.model is None:
            if not self.load_model():
                return {"error": "Model not loaded"}
        
        # Преобразование входных данных в вектор признаков
        features = np.array([[
            data.get(f, 0.0) for f in self.feature_names
        ]])
        
        # Предсказание: -1 = аномалия, 1 = норма
        prediction = self.model.predict(features)[0]
        
        # Оценка аномальности (чем ниже, тем более аномально)
        score = self.model.score_samples(features)[0]
        # Нормализация в диапазон 0..1
        anomaly_score = 1 / (1 + np.exp(-score))
        
        return {
            "is_anomaly": prediction == -1,
            "anomaly_score": float(anomaly_score),
            "features": {f: data.get(f, 0.0) for f in self.feature_names}
        }
4.3. Обучение модели на исторических данных
train_model.py (запускается отдельно на ПК):

python
"""Скрипт для обучения модели на исторических данных из Home Assistant."""

import pandas as pd
from ml_model import AnomalyDetectorModel

# Загрузка исторических данных (экспорт из Home Assistant)
data = pd.read_csv("home_assistant_history.csv")

# Выбор признаков
features = ["temperature", "humidity", "power_consumption", 
            "motion_count", "light_level"]
X = data[features]

# Обучение модели
model = AnomalyDetectorModel(model_path="models/anomaly_model.pkl")
model.train(data)

print("Модель обучена и сохранена!")
5. Часть 3. Реализация Data Update Coordinator (20 минут)
Data Update Coordinator — ключевой компонент для управления периодическим обновлением данных.

coordinator/base.py :

python
"""Data Update Coordinator для Anomaly Detector."""

import asyncio
from datetime import timedelta
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from ..const import DOMAIN
from ..ml_model import AnomalyDetectorModel

_LOGGER = logging.getLogger(__name__)

class AnomalyDetectorCoordinator(DataUpdateCoordinator):
    """Координатор для сбора данных и запуска ML-инференса."""
    
    def __init__(self, hass: HomeAssistant, entry):
        self.hass = hass
        self.entry = entry
        self.model = AnomalyDetectorModel(model_path="/config/models/anomaly_model.pkl")
        self.model.load_model()
        
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(minutes=5),  # Обновление каждые 5 минут
            always_update=True
        )
    
    async def _async_update_data(self):
        """Сбор данных и запуск ML-инференса."""
        try:
            # 1. Сбор данных с датчиков
            sensor_data = await self._fetch_sensor_data()
            
            # 2. Запуск ML-инференса
            result = await self._run_inference(sensor_data)
            
            # 3. Сохранение результата
            self.data = result
            
            return result
            
        except Exception as err:
            _LOGGER.error(f"Ошибка обновления данных: {err}")
            raise UpdateFailed(f"Ошибка обновления: {err}")
    
    async def _fetch_sensor_data(self) -> dict:
        """Сбор данных с датчиков Home Assistant."""
        data = {}
        
        # Получение состояния датчиков
        sensor_mapping = {
            "temperature": "sensor.living_room_temperature",
            "humidity": "sensor.living_room_humidity",
            "power_consumption": "sensor.total_power_consumption",
            "motion_count": "sensor.daily_motion_count",
            "light_level": "sensor.light_sensor"
        }
        
        for key, entity_id in sensor_mapping.items():
            state = self.hass.states.get(entity_id)
            if state:
                try:
                    data[key] = float(state.state)
                except (ValueError, TypeError):
                    data[key] = 0.0
            else:
                data[key] = 0.0
        
        return data
    
    async def _run_inference(self, sensor_data: dict) -> dict:
        """Запуск ML-модели для детекции аномалий."""
        # Запуск в отдельном потоке (блокирующая операция)
        result = await self.hass.async_add_executor_job(
            self.model.predict, sensor_data
        )
        return result
6. Часть 4. Реализация сенсора (20 минут)
sensor.py :

python
"""Сенсор для отображения результатов детекции аномалий."""

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, DEFAULT_NAME
from .coordinator import AnomalyDetectorCoordinator

async def async_setup_entry(hass: HomeAssistant, entry, async_add_entities):
    """Настройка сенсоров."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    
    sensors = [
        AnomalyScoreSensor(coordinator, entry),
        AnomalyStatusBinarySensor(coordinator, entry)
    ]
    async_add_entities(sensors)

class AnomalyScoreSensor(CoordinatorEntity, SensorEntity):
    """Сенсор для отображения степени аномальности."""
    
    _attr_icon = "mdi:alert-circle"
    _attr_native_unit_of_measurement = "%"
    
    def __init__(self, coordinator: AnomalyDetectorCoordinator, entry):
        super().__init__(coordinator)
        self._attr_unique_id = f"{entry.entry_id}_anomaly_score"
        self._attr_name = "Anomaly Score"
        self._attr_device_class = "score"
        
    @property
    def native_value(self):
        """Текущее значение сенсора."""
        if self.coordinator.data and "anomaly_score" in self.coordinator.data:
            return round(self.coordinator.data["anomaly_score"] * 100, 1)
        return None
    
    @property
    def extra_state_attributes(self):
        """Дополнительные атрибуты."""
        if self.coordinator.data and "features" in self.coordinator.data:
            return {
                "features": self.coordinator.data["features"],
                "is_anomaly": self.coordinator.data.get("is_anomaly", False)
            }
        return {}

class AnomalyStatusBinarySensor(CoordinatorEntity, SensorEntity):
    """Бинарный сенсор статуса аномалии."""
    
    _attr_icon = "mdi:security"
    
    def __init__(self, coordinator: AnomalyDetectorCoordinator, entry):
        super().__init__(coordinator)
        self._attr_unique_id = f"{entry.entry_id}_anomaly_status"
        self._attr_name = "Anomaly Status"
        self._attr_device_class = "problem"
        
    @property
    def is_on(self):
        """True если обнаружена аномалия."""
        if self.coordinator.data:
            return self.coordinator.data.get("is_anomaly", False)
        return False
    
    @property
    def extra_state_attributes(self):
        """Дополнительные атрибуты."""
        if self.coordinator.data:
            return {
                "anomaly_score": self.coordinator.data.get("anomaly_score", 0),
                "features": self.coordinator.data.get("features", {})
            }
        return {}
7. Часть 5. ML → Automation Pipeline (20 минут)
7.1. Создание автоматизации через YAML
После установки интеграции, создайте автоматизацию в automations.yaml:

yaml
- id: 'anomaly_alert'
  alias: "Уведомление об аномалии"
  description: "Отправка уведомления при обнаружении аномалии"
  trigger:
    - platform: state
      entity_id: binary_sensor.anomaly_status
      to: 'on'
  condition:
    - condition: template
      value_template: "{{ states('sensor.anomaly_score') | float > 70 }}"
  action:
    - service: notify.mobile_app_phone
      data:
        title: "⚠️ Обнаружена аномалия!"
        message: >
          Обнаружена аномалия в состоянии дома.
          Степень аномальности: {{ states('sensor.anomaly_score') }}%
          Параметры: {{ state_attr('sensor.anomaly_score', 'features') }}
    - service: persistent_notification.create
      data:
        title: "Anomaly Detector"
        message: "Обнаружена аномалия! Проверьте датчики."
        notification_id: "anomaly_alert"
7.2. Автоматизация через UI (Blueprint)
Интеграция может предоставлять Blueprint для быстрого создания автоматизаций:

blueprints/anomaly_alert.yaml :

yaml
blueprint:
  name: Anomaly Alert
  description: Отправка уведомления при обнаружении аномалии
  domain: automation
  input:
    anomaly_sensor:
      name: Anomaly Sensor
      description: Сенсор аномалий
      selector:
        entity:
          domain: binary_sensor
    score_threshold:
      name: Порог аномальности (%)
      description: Минимальный процент аномальности для срабатывания
      default: 70
      selector:
        number:
          min: 0
          max: 100
          unit_of_measurement: "%"
    notify_service:
      name: Сервис уведомлений
      description: Куда отправлять уведомления
      default: notify.persistent_notification
      selector:
        target:
          entity:
            domain: notify

trigger:
  - platform: state
    entity_id: !input anomaly_sensor
    to: 'on'

condition:
  - condition: template
    value_template: >
      {{ states('sensor.anomaly_score') | float > !input score_threshold }}

action:
  - service: !input notify_service
    data:
      title: "⚠️ Обнаружена аномалия!"
      message: >
        Степень аномальности: {{ states('sensor.anomaly_score') }}%
        Параметры: {{ state_attr('sensor.anomaly_score', 'features') }}
7.3. Интеграция с LLM через Custom Tools
Для расширенной аналитики можно зарегистрировать инструмент для LLM:

llm.py :

python
"""Интеграция с LLM через кастомные инструменты."""

from homeassistant.components import llm
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.llm import LLMContext

@callback
def async_get_tools(hass: HomeAssistant, llm_context: LLMContext) -> llm.LLMTools:
    """Регистрация инструментов для LLM."""
    return llm.LLMTools(
        tools=[AnomalyAnalysisTool(hass)],
        prompt="Используй AnomalyAnalysisTool для анализа аномалий в доме..."
    )

class AnomalyAnalysisTool(llm.Tool):
    """Инструмент для анализа аномалий."""
    
    def __init__(self, hass):
        self.hass = hass
        self.name = "analyze_anomalies"
        self.description = "Анализ аномалий в состоянии дома за последний час"
        
    async def async_call(self, llm_context, user_prompt):
        """Вызов инструмента."""
        # Получение истории аномалий
        history = await self._get_anomaly_history()
        return {
            "recent_anomalies": history,
            "summary": f"Обнаружено {len(history)} аномалий за последний час"
        }
8. Часть 6. Тестирование и отладка (15 минут)
8.1. Локальное тестирование
bash
# Запуск Home Assistant в режиме разработки
hass --config config --debug

# Проверка синтаксиса
python3 -m py_compile custom_components/anomaly_detector/*.py
8.2. Диагностика
diagnostics.py :

python
"""Диагностическая информация для интеграции."""

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict:
    """Возврат диагностической информации."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    
    return {
        "entry_id": entry.entry_id,
        "version": entry.version,
        "coordinator": {
            "update_interval": coordinator.update_interval.total_seconds(),
            "last_update_success": coordinator.last_update_success,
            "data": coordinator.data
        },
        "model": {
            "loaded": coordinator.model.model is not None,
            "features": coordinator.model.feature_names
        }
    }
8.3. Установка интеграции через HACS
Добавьте репозиторий в HACS как Custom Repository

Установите интеграцию через HACS

Настройте через Settings → Devices & Services → Add Integration

9. Часть 7. Связь с компетенциями и выводы (10 минут)
9.1. Соответствие компетенции LC‑5.2 (средний уровень)
Аспект LC‑5.2	Реализация в практической работе
Выбор инструментов	Координатор для управления данными, MQTT/REST для коммуникации, scikit-learn для ML
Уровень доступа	Разделение прав через сервисы Home Assistant, безопасная настройка через Config Flow
Контроль качества	Валидация данных в Coordinator, обработка ошибок, диагностика
Скорость запросов	Асинхронная обработка, кэширование через Coordinator, настраиваемый интервал обновления
9.2. Соответствие компетенции PL‑1.2 (средний уровень)
Аспект PL‑1.2	Реализация
Выбор библиотек	scikit-learn для ML, asyncio/aiohttp для асинхронной работы
Оптимизация кода	Использование Coordinator для кэширования, асинхронные операции
Интеграция	Связь с экосистемой Home Assistant через API
9.3. Ключевые выводы
Custom Integration — основной способ расширения функциональности Home Assistant

Data Update Coordinator — ключевой паттерн для управления данными и ML-инференсом

Асинхронная архитектура — критична для производительности системы умного дома

ML-пайплайн должен быть интегрирован через Coordinator, а не блокировать основной цикл

Автоматизации связывают ML-результаты с действиями в доме

10. Домашнее задание
Расширьте ML-модель — добавьте поддержку обучения на новых данных через сервис Home Assistant

Реализуйте дашборд — создайте Lovelace-карточку для визуализации аномалий

Настройте адаптивный порог — реализуйте автоматическую настройку порога аномальности на основе исторических данных

Добавьте MQTT-поддержку — реализуйте публикацию результатов в MQTT для интеграции с другими системами

11. Рекомендуемые источники
Home Assistant Developer Docs — https://developers.home-assistant.io

Integration Blueprint — https://github.com/jpawlowski/hacs.integration_blueprint[reference:14]

LLM API Integration — https://developers.home-assistant.io/docs/core/llm/[reference:15]

Home Generative Agent — пример комплексной ML-интеграции

Scikit-learn Isolation Forest — https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html