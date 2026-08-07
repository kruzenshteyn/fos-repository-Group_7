Занятие 1_4

МЕТОДИЧЕСКИЕ УКАЗАНИЯ К ПРАКТИЧЕСКОЙ РАБОТЕ

Сбор телеметрии с датчиков. Настройка MQTT. Хранение временных рядов в TimescaleDB. Создание дашборда в Grafana

**Основные технологии:**

- Python;
- MQTT;
- Mosquitto MQTT Broker;
- TimescaleDB;
- PostgreSQL;
- Grafana.

В работе создаётся законченный конвейер обработки телеметрии:

![](attachments/images/image1.png)

**2. Цель работы**

Получить практические навыки построения системы сбора, передачи, хранения и визуализации телеметрии устройств умного дома.

В ходе работы необходимо:

1.  запустить MQTT-брокер;

2.  разработать генератор телеметрии на Python;

3.  опубликовать данные датчиков в MQTT;

4.  создать программу-подписчик;

5.  записать телеметрию в TimescaleDB;

6.  выполнить аналитические SQL-запросы;

7.  создать представление;

8.  создать функцию;

9.  создать триггер регистрации аварийных значений;

10. проанализировать план выполнения запроса;

11. подключить Grafana;

12. создать базовый дашборд.

13. 

**3. Формируемые компетенции**

**3.1. Компетенция BD-3**

**Наименование:** хранение данных.

**Формулировка:** способен организовывать хранение данных, выбирая адекватные технологические решения.

**Индикатор BD-3.1:** разрабатывает, отлаживает и тестирует прикладные решения с применением различных технологий хранения структурированных данных, оценивает качество построенных решений.

**Уровень сформированности --- средний:**

- пишет аналитические запросы;
- анализирует план запроса;
- создаёт представления;
- создаёт функции;
- создаёт триггеры;
- использует специализированное хранилище временных рядов.

**3.2. Компетенция PL-1**

**Наименование:** Python.

**Формулировка:** способен применять язык программирования Python для решения задач в области искусственного интеллекта.

**Индикатор PL-1.2:** осуществляет выбор инструментов разработки на Python, приемлемых для создания прикладной системы обработки научных данных, машинного обучения и визуализации.

**Уровень сформированности --- средний:**

- использует библиотеки Python для обработки телеметрии;
- применяет NumPy для генерации и преобразования данных;
- использует Paho MQTT;
- использует драйвер PostgreSQL;
- организует пакетную запись данных;
- разделяет параметры подключения и программную логику;
- обрабатывает ошибки соединения и некорректные сообщения.

**4. Результат практической работы**

После выполнения работы должна функционировать система, в которой:

- Python-программа формирует показания датчиков;
- данные передаются через MQTT-брокер;
- программа-подписчик принимает JSON-сообщения;
- значения записываются в TimescaleDB;
- SQL-запросы рассчитывают статистику;
- триггер фиксирует превышение допустимой концентрации CO₂;
- Grafana отображает температуру, влажность и CO₂;
- студент может объяснить план выполнения аналитического запроса.

**Исходные условия**

Предполагается, что на компьютере установлены:

- Python 3;
- PostgreSQL с расширением TimescaleDB;
- Mosquitto;
- Grafana.

Допускается использование подготовленного преподавателем сервера.

Необходимые сетевые порты:

  ---------------------------------
  Система                      Порт
  -------------------------- ------
  MQTT Mosquitto               1883

  PostgreSQL / TimescaleDB     5432

  Grafana                      3000
  ---------------------------------

Если компоненты работают на разных компьютерах, необходимо использовать их реальные IP-адреса вместо `localhost`.

**Структура проекта**

Создайте рабочий каталог:

    smart_home_telemetry/
    │
    ├── config.py
    ├── publisher.py
    ├── subscriber.py
    ├── requirements.txt
    └── sql/
        ├── 01_create_database.sql
        ├── 02_analytics.sql
        └── 03_objects.sql

**Ход Работы**

**Этап 1. Подготовка среды Python**

Подготовить окружение для публикации MQTT-сообщений и записи данных в TimescaleDB.

Перейдите в рабочий каталог:

    cd smart_home_telemetry

Создайте виртуальное окружение.

Для Windows:

>     python -m venv venv
>     venv\Scripts\activate

Для Linux:

>     python3 -m venv venv
>     source venv/bin/activate

Создайте файл `requirements.txt`:

>     paho-mqtt
>     psycopg2-binary
>     numpy

Установите библиотеки:

    python -m pip install -r requirements.txt

Проверьте установку:

    python -c "import paho.mqtt.client, psycopg2, numpy; print('Среда готова')"

**Этап считается выполненным, если**

Все три библиотеки импортируются без ошибок.

**9. Этап 2. Создание файла конфигурации**

Вынести параметры подключения из программной логики.

Создайте файл `config.py`:

>     MQTT_HOST = "localhost"
>     MQTT_PORT = 1883
>     MQTT_TOPIC = "home/+/telemetry"
>
>     POSTGRES_HOST = "localhost"
>     POSTGRES_PORT = 5432
>     POSTGRES_DATABASE = "smart_home"
>     POSTGRES_USER = "postgres"
>     POSTGRES_PASSWORD = "postgres"
>
>     PUBLISH_INTERVAL = 1.0

Если MQTT-брокер или TimescaleDB работают на другом компьютере, замените `localhost` на соответствующий IP-адрес.

**Этап считается выполненным, если**

Файл создан и содержит актуальные параметры подключения.

**Этап 3. Запуск и проверка MQTT-брокера**

Проверить передачу сообщения через Mosquitto.

Запустите MQTT-брокер:

    mosquitto -v

Если Mosquitto уже работает как служба, повторный запуск не требуется.

Откройте второе окно терминала и запустите подписчик:

    mosquitto_sub -h localhost -p 1883 -t "home/+/telemetry" -v

Откройте третье окно и отправьте тестовое сообщение:

>     mosquitto_pub -h localhost -p 1883 ^
>     -t "home/living_room/telemetry" ^
>     -m "{\"temperature\":22.5,\"humidity\":45.0,\"co2\":650}"

Для Linux команда может быть записана в одну строку:

>     mosquitto_pub -h localhost -p 1883 \
>     -t "home/living_room/telemetry" \
>     -m '{"temperature":22.5,"humidity":45.0,"co2":650}'

В окне `mosquitto``_``sub` должно появиться:

    home/living_room/telemetry {"temperature":22.5,"humidity":45.0,"co2":650}

**Зафиксируйте в отчёте**

- адрес брокера;
- порт;
- MQTT-тему;
- полученное сообщение.

**Этап считается выполненным, если**

Тестовое сообщение проходит через брокер и отображается у подписчика.

**Этап 4. Разработка генератора телеметрии**

Создать Python-программу, имитирующую работу датчиков умного дома.

Создайте файл `publisher.py`:

>     import json
>     import random
>     import time
>     from datetime import datetime, timezone
>
>     import numpy as np
>     import paho.mqtt.client as mqtt
>
>     from config import (
>         MQTT_HOST,
>         MQTT_PORT,
>         PUBLISH_INTERVAL,
>     )
>
>
>     ROOMS = [
>         "living_room",
>         "kitchen",
>         "bedroom",
>     ]
>
>
>     def generate_telemetry(room: str) -> dict:
>         """Формирует показания виртуальных датчиков."""
>
>         base_temperature = {
>             "living_room": 22.0,
>             "kitchen": 23.5,
>             "bedroom": 21.0,
>         }[room]
>
>         temperature = base_temperature + np.random.normal(
>             loc=0.0,
>             scale=0.4,
>         )
>
>         humidity = 45.0 + np.random.normal(
>             loc=0.0,
>             scale=3.0,
>         )
>
>         co2 = int(
>             550 + np.random.normal(
>                 loc=0.0,
>                 scale=80.0,
>             )
>         )
>
>         # Иногда создаём повышенную концентрацию CO₂.
>         if random.random() < 0.05:
>             co2 += random.randint(700, 1200)
>
>         power = max(
>             0.0,
>             150.0 + np.random.normal(
>                 loc=0.0,
>                 scale=30.0,
>             ),
>         )
>
>         return {
>             "device_id": f"sensor_{room}",
>             "room": room,
>             "timestamp": datetime.now(
>                 timezone.utc
>             ).isoformat(),
>             "temperature": round(
>                 float(temperature),
>                 2,
>             ),
>             "humidity": round(
>                 float(humidity),
>                 2,
>             ),
>             "co2": max(co2, 350),
>             "power": round(
>                 float(power),
>                 2,
>             ),
>         }
>
>
>     def on_connect(
>         client,
>         userdata,
>         flags,
>         reason_code,
>         properties,
>     ):
>         if reason_code == 0:
>             print("Подключение к MQTT выполнено")
>         else:
>             print(
>                 "Ошибка подключения:",
>                 reason_code,
>             )
>
>
>     def main() -> None:
>         client = mqtt.Client(
>             mqtt.CallbackAPIVersion.VERSION2
>         )
>
>         client.on_connect = on_connect
>
>         client.connect(
>             MQTT_HOST,
>             MQTT_PORT,
>             keepalive=60,
>         )
>
>         client.loop_start()
>
>         try:
>             while True:
>                 for room in ROOMS:
>                     telemetry = generate_telemetry(
>                         room
>                     )
>
>                     topic = (
>                         f"home/{room}/telemetry"
>                     )
>
>                     payload = json.dumps(
>                         telemetry,
>                         ensure_ascii=False,
>                     )
>
>                     result = client.publish(
>                         topic,
>                         payload,
>                         qos=1,
>                     )
>
>                     result.wait_for_publish()
>
>                     print(
>                         topic,
>                         payload,
>                     )
>
>                 time.sleep(
>                     PUBLISH_INTERVAL
>                 )
>
>         except KeyboardInterrupt:
>             print(
>                 "\nПубликация остановлена"
>             )
>
>         finally:
>             client.loop_stop()
>             client.disconnect()
>
>
>     if __name__ == "__main__":
>         main()

Запустите программу:

    python publisher.py

Параллельно должен работать терминальный подписчик:

    mosquitto_sub -h localhost -t "home/+/telemetry" -v

**Ожидаемый результат**

Раз в секунду для трёх комнат публикуются JSON-сообщения:

>     {
>         "device_id": "sensor_living_room",
>         "room": "living_room",
>         "timestamp": "2026-07-23T10:30:15+00:00",
>         "temperature": 22.18,
>         "humidity": 47.21,
>         "co2": 618,
>         "power": 164.50
>     }

**Этап считается выполненным, если**

Программа непрерывно публикует корректные JSON-сообщения в три MQTT-темы.

**Этап 5. Создание базы данных временных рядов**

Создать структуру TimescaleDB для хранения телеметрии.

Подключитесь к PostgreSQL:

    psql -U postgres

Создайте базу:

    CREATE DATABASE smart_home;

Подключитесь к ней:

    \c smart_home

Создайте файл `sql/01_create_database.sql`:

>     CREATE EXTENSION IF NOT EXISTS timescaledb;
>
>     CREATE TABLE IF NOT EXISTS telemetry (
>         time            TIMESTAMPTZ NOT NULL,
>         device_id       TEXT NOT NULL,
>         room            TEXT NOT NULL,
>         temperature     DOUBLE PRECISION,
>         humidity        DOUBLE PRECISION,
>         co2             INTEGER,
>         power           DOUBLE PRECISION
>     );
>
>     SELECT create_hypertable(
>         'telemetry',
>         'time',
>         if_not_exists => TRUE
>     );
>
>     CREATE INDEX IF NOT EXISTS
>     idx_telemetry_room_time
>     ON telemetry (
>         room,
>         time DESC
>     );
>
>     CREATE TABLE IF NOT EXISTS alerts (
>         alert_id        BIGSERIAL PRIMARY KEY,
>         event_time      TIMESTAMPTZ NOT NULL,
>         device_id       TEXT NOT NULL,
>         room            TEXT NOT NULL,
>         alert_type      TEXT NOT NULL,
>         measured_value  DOUBLE PRECISION NOT NULL,
>         message         TEXT NOT NULL
>     );

Выполните файл:

    psql -U postgres -d smart_home -f sql/01_create_database.sql

Проверьте таблицу:

    \d telemetry

Созданы:

- расширение TimescaleDB;
- гипертаблица `telemetry`;
- индекс;
- таблица `alerts`.

**Этап считается выполненным, если**

Команда просмотра структуры показывает таблицу `telemetry`, а TimescaleDB распознаёт её как гипертаблицу.

**13. Этап 6. Разработка MQTT-подписчика**

Принимать сообщения MQTT, проверять их структуру и записывать значения в TimescaleDB.

Создайте файл `subscriber.py`:

>     import json
>     import queue
>     import threading
>     from datetime import datetime
>
>     import paho.mqtt.client as mqtt
>     import psycopg2
>     from psycopg2.extras import execute_values
>
>     from config import (
>         MQTT_HOST,
>         MQTT_PORT,
>         MQTT_TOPIC,
>         POSTGRES_HOST,
>         POSTGRES_PORT,
>         POSTGRES_DATABASE,
>         POSTGRES_USER,
>         POSTGRES_PASSWORD,
>     )
>
>
>     BATCH_SIZE = 10
>
>     message_queue: queue.Queue = queue.Queue()
>
>
>     def create_db_connection():
>         return psycopg2.connect(
>             host=POSTGRES_HOST,
>             port=POSTGRES_PORT,
>             dbname=POSTGRES_DATABASE,
>             user=POSTGRES_USER,
>             password=POSTGRES_PASSWORD,
>         )
>
>
>     def validate_payload(
>         payload: dict
>     ) -> tuple:
>         required_fields = {
>             "device_id",
>             "room",
>             "timestamp",
>             "temperature",
>             "humidity",
>             "co2",
>             "power",
>         }
>
>         missing = (
>             required_fields
>             - payload.keys()
>         )
>
>         if missing:
>             raise ValueError(
>                 f"Отсутствуют поля: {missing}"
>             )
>
>         timestamp = datetime.fromisoformat(
>             payload["timestamp"]
>         )
>
>         return (
>             timestamp,
>             str(payload["device_id"]),
>             str(payload["room"]),
>             float(payload["temperature"]),
>             float(payload["humidity"]),
>             int(payload["co2"]),
>             float(payload["power"]),
>         )
>
>
>     def database_worker() -> None:
>         connection = create_db_connection()
>
>         insert_sql = """
>             INSERT INTO telemetry (
>                 time,
>                 device_id,
>                 room,
>                 temperature,
>                 humidity,
>                 co2,
>                 power
>             )
>             VALUES %s
>         """
>
>         batch = []
>
>         try:
>             while True:
>                 item = message_queue.get()
>
>                 if item is None:
>                     break
>
>                 batch.append(item)
>
>                 if len(batch) >= BATCH_SIZE:
>                     with connection.cursor() as cursor:
>                         execute_values(
>                             cursor,
>                             insert_sql,
>                             batch,
>                         )
>
>                     connection.commit()
>
>                     print(
>                         f"Записано строк: "
>                         f"{len(batch)}"
>                     )
>
>                     batch.clear()
>
>         except Exception:
>             connection.rollback()
>             raise
>
>         finally:
>             if batch:
>                 with connection.cursor() as cursor:
>                     execute_values(
>                         cursor,
>                         insert_sql,
>                         batch,
>                     )
>
>                 connection.commit()
>
>             connection.close()
>
>
>     def on_connect(
>         client,
>         userdata,
>         flags,
>         reason_code,
>         properties,
>     ):
>         if reason_code != 0:
>             print(
>                 "Ошибка MQTT:",
>                 reason_code,
>             )
>             return
>
>         client.subscribe(
>             MQTT_TOPIC,
>             qos=1,
>         )
>
>         print(
>             "Подписка выполнена:",
>             MQTT_TOPIC,
>         )
>
>
>     def on_message(
>         client,
>         userdata,
>         message,
>     ):
>         try:
>             payload_text = (
>                 message.payload.decode(
>                     "utf-8"
>                 )
>             )
>
>             payload = json.loads(
>                 payload_text
>             )
>
>             row = validate_payload(
>                 payload
>             )
>
>             message_queue.put(
>                 row
>             )
>
>         except (
>             UnicodeDecodeError,
>             json.JSONDecodeError,
>             ValueError,
>             TypeError,
>         ) as error:
>             print(
>                 "Некорректное сообщение:",
>                 error,
>             )
>
>
>     def main() -> None:
>         worker = threading.Thread(
>             target=database_worker,
>             daemon=True,
>         )
>
>         worker.start()
>
>         client = mqtt.Client(
>             mqtt.CallbackAPIVersion.VERSION2
>         )
>
>         client.on_connect = on_connect
>         client.on_message = on_message
>
>         client.connect(
>             MQTT_HOST,
>             MQTT_PORT,
>             keepalive=60,
>         )
>
>         try:
>             client.loop_forever()
>
>         except KeyboardInterrupt:
>             print(
>                 "\nПодписчик остановлен"
>             )
>
>         finally:
>             message_queue.put(None)
>             worker.join()
>             client.disconnect()
>
>
>     if __name__ == "__main__":
>         main()

Почему используется пакетная запись

Программа не выполняет отдельный SQL-запрос для каждого сообщения. Данные собираются в пакет по 10 строк и записываются одной операцией.

Это:

- уменьшает число транзакций;
- снижает нагрузку на базу;
- повышает скорость записи;
- демонстрирует оптимизацию Python-кода.

**Порядок запуска системы**

Откройте три терминала.

Терминал 1:

    mosquitto -v

Терминал 2:

    python subscriber.py

Терминал 3:

    python publisher.py

Оставьте систему работать не менее двух минут.

**Проверка записи**

Выполните:

>     SELECT COUNT(*)
>     FROM telemetry;
>
> Просмотрите последние записи:
>
>     SELECT *
>     FROM telemetry
>     ORDER BY time DESC
>     LIMIT 10;

**Этап считается выполненным, если**

В таблице присутствуют данные трёх комнат, а число строк непрерывно увеличивается.

**тап 7. Выполнение аналитических запросов**

Получить основные показатели телеметрии средствами SQL.

Создайте файл `sql``/02_``analytics``.``sql`.

**Средние значения по комнатам**

>     SELECT
>         room,
>         ROUND(
>             AVG(temperature)::numeric,
>             2
>         ) AS avg_temperature,
>         ROUND(
>             AVG(humidity)::numeric,
>             2
>         ) AS avg_humidity,
>         ROUND(
>             AVG(co2)::numeric,
>             2
>         ) AS avg_co2
>     FROM telemetry
>     WHERE time >= NOW() - INTERVAL '10 minutes'
>     GROUP BY room
>     ORDER BY room;

**Агрегирование по минутам**

>     SELECT
>         time_bucket(
>             INTERVAL '1 minute',
>             time
>         ) AS minute,
>         room,
>         ROUND(
>             AVG(temperature)::numeric,
>             2
>         ) AS avg_temperature,
>         MAX(co2) AS max_co2,
>         ROUND(
>             AVG(power)::numeric,
>             2
>         ) AS avg_power
>     FROM telemetry
>     WHERE time >= NOW() - INTERVAL '30 minutes'
>     GROUP BY minute, room
>     ORDER BY minute, room;

**Поиск превышений CO₂**

>     SELECT
>         time,
>         room,
>         device_id,
>         co2
>     FROM telemetry
>     WHERE co2 > 1200
>     ORDER BY time DESC;

**Максимальная мощность по помещениям**

>     SELECT
>         room,
>         MAX(power) AS max_power
>     FROM telemetry
>     GROUP BY room
>     ORDER BY max_power DESC;

**В отчёт включите**

- результат каждого запроса;
- назначение `GROUP BY`;
- назначение `time_bucket`;
- интервал, по которому выполнялось агрегирование.

**Этап считается выполненным, если**

Получены статистические показатели для всех трёх комнат.

**Этап 8. Создание представления**

Создать повторно используемый объект для получения минутной статистики.

Добавьте в файл `sql``/03_``objects``.``sql`:

>     CREATE OR REPLACE VIEW telemetry_per_minute AS
>     SELECT
>         time_bucket(
>             INTERVAL '1 minute',
>             time
>         ) AS minute,
>         room,
>         AVG(temperature) AS avg_temperature,
>         AVG(humidity) AS avg_humidity,
>         AVG(co2) AS avg_co2,
>         MAX(co2) AS max_co2,
>         AVG(power) AS avg_power
>     FROM telemetry
>     GROUP BY minute, room;
>
> Выполните:
>
>     psql -U postgres -d smart_home -f sql/03_objects.sql
>
> Проверьте представление:
>
>     SELECT *
>     FROM telemetry_per_minute
>     ORDER BY minute DESC, room
>     LIMIT 20;

**Этап считается выполненным, если**

Запрос к представлению возвращает агрегированные данные без повторного написания полного SQL-запроса.

**Этап 9. Создание SQL-функции**

Создать функцию получения статистики по выбранной комнате и временному интервалу.

Добавьте в `sql``/03_objects.sql`:

>     CREATE OR REPLACE FUNCTION room_statistics(
>         selected_room TEXT,
>         period_start TIMESTAMPTZ,
>         period_end TIMESTAMPTZ
>     )
>     RETURNS TABLE (
>         avg_temperature DOUBLE PRECISION,
>         min_temperature DOUBLE PRECISION,
>         max_temperature DOUBLE PRECISION,
>         avg_humidity DOUBLE PRECISION,
>         avg_co2 DOUBLE PRECISION,
>         max_co2 INTEGER,
>         avg_power DOUBLE PRECISION
>     )
>     LANGUAGE SQL
>     AS $$
>         SELECT
>             AVG(temperature),
>             MIN(temperature),
>             MAX(temperature),
>             AVG(humidity),
>             AVG(co2),
>             MAX(co2),
>             AVG(power)
>         FROM telemetry
>         WHERE room = selected_room
>           AND time >= period_start
>           AND time < period_end;
>     $$;
>
> Выполните файл повторно:
>
>     psql -U postgres -d smart_home -f sql/03_objects.sql
>
> Вызовите функцию:
>
>     SELECT *
>     FROM room_statistics(
>         'living_room',
>         NOW() - INTERVAL '15 minutes',
>         NOW()
>     );

**Этап считается выполненным, если**

Функция возвращает статистику только для указанной комнаты и интервала.

**17. Этап 10. Создание триггера**

Автоматически регистрировать значения CO₂ выше заданного порога.

Добавьте в `sql``/03_``objects``.``sql` функцию триггера:

>     CREATE OR REPLACE FUNCTION register_co2_alert()
>     RETURNS TRIGGER
>     LANGUAGE plpgsql
>     AS $$
>     BEGIN
>         IF NEW.co2 > 1200 THEN
>             INSERT INTO alerts (
>                 event_time,
>                 device_id,
>                 room,
>                 alert_type,
>                 measured_value,
>                 message
>             )
>             VALUES (
>                 NEW.time,
>                 NEW.device_id,
>                 NEW.room,
>                 'HIGH_CO2',
>                 NEW.co2,
>                 'Превышен уровень CO2'
>             );
>         END IF;
>
>         RETURN NEW;
>     END;
>     $$;

Создайте триггер:

>     DROP TRIGGER IF EXISTS
>     telemetry_co2_alert
>     ON telemetry;
>
>     CREATE TRIGGER telemetry_co2_alert
>     AFTER INSERT ON telemetry
>     FOR EACH ROW
>     EXECUTE FUNCTION register_co2_alert();

Выполните файл:

    psql -U postgres -d smart_home -f sql/03_objects.sql

Оставьте Publisher работать до появления повышенного значения CO₂.

Проверьте журнал:

>     SELECT *
>     FROM alerts
>     ORDER BY event_time DESC;

Для немедленной проверки можно вручную добавить запись:

>     INSERT INTO telemetry (
>         time,
>         device_id,
>         room,
>         temperature,
>         humidity,
>         co2,
>         power
>     )
>     VALUES (
>         NOW(),
>         'test_sensor',
>         'laboratory',
>         22.0,
>         45.0,
>         1800,
>         100.0
>     );

В таблице `alerts` автоматически появляется запись типа `HIGH``_``CO``2`.

**Этап считается выполненным, если**

Превышение порога приводит к созданию строки в таблице `alerts` без отдельного SQL-запроса со стороны Python-программы.

**Этап 11. Анализ плана запроса**

Определить способ выполнения аналитического SQL-запроса.

Выполните:

>     EXPLAIN ANALYZE
>     SELECT
>         time_bucket(
>             INTERVAL '1 minute',
>             time
>         ) AS minute,
>         room,
>         AVG(temperature)
>     FROM telemetry
>     WHERE room = 'living_room'
>       AND time >= NOW() - INTERVAL '30 minutes'
>     GROUP BY minute, room
>     ORDER BY minute;

Найдите в результате:

- общее время выполнения;
- число обработанных строк;
- способ доступа к данным;
- операцию агрегирования;
- операцию сортировки.

Обратите внимание на возможные элементы плана:

    Index Scan
    Bitmap Index Scan
    Seq Scan
    HashAggregate
    GroupAggregate
    Sort

Проверьте наличие индекса:

>     SELECT
>         indexname,
>         indexdef
>     FROM pg_indexes
>     WHERE tablename = 'telemetry';

    В отчёт включите

- фрагмент плана;
- фактическое время выполнения;
- способ чтения таблицы;
- объяснение, использован ли индекс;
- назначение индекса `(``room``, ``time`` ``DESC``)`.

<!-- -->

    Этап считается выполненным, если

Студент может указать способ доступа к данным и фактическое время выполнения запроса.

**19. Этап 12. Подключение Grafana к TimescaleDB**

Добавить TimescaleDB как источник данных Grafana.

**Порядок выполнения**

Откройте в браузере:

    http://localhost:3000

Выполните вход.

Перейдите:

>     Connections
>     → Data sources
>     → Add data source
>     → PostgreSQL

Укажите параметры:

  ----------------------------------------------
  Параметр             Значение
  -------------------- -------------------------
  Host                 localhost:5432

  Database             smart_home

  User                 postgres

  Password             postgres

  TLS/SSL Mode         disable

  PostgreSQL version   соответствующая серверу

  TimescaleDB          включить
  ----------------------------------------------

Нажмите:

    Save & test

Grafana выводит сообщение об успешном подключении к базе.

**Этап считается выполненным, если**

Источник данных сохраняется без ошибки подключения.

**Этап 13. Создание дашборда**

Создать панель мониторинга телеметрии умного дома.

Перейдите:

    Dashboards
    → New
    → New dashboard
    → Add visualization

Выберите источник TimescaleDB.

**Панель температуры**

Задайте SQL-запрос:

>     SELECT
>         $__timeGroupAlias(
>             time,
>             '10s'
>         ),
>         room AS metric,
>         AVG(temperature) AS value
>     FROM telemetry
>     WHERE $__timeFilter(time)
>     GROUP BY 1, room
>     ORDER BY 1;

Настройте:

    Panel title: Температура
    Visualization: Time series
    Unit: Celsius

**Панель влажности**

>     SELECT
>         $__timeGroupAlias(
>             time,
>             '10s'
>         ),
>         room AS metric,
>         AVG(humidity) AS value
>     FROM telemetry
>     WHERE $__timeFilter(time)
>     GROUP BY 1, room
>     ORDER BY 1;

Настройте:

    Panel title: Влажность
    Unit: Percent

**Панель CO₂**

>     SELECT
>         $__timeGroupAlias(
>             time,
>             '10s'
>         ),
>         room AS metric,
>         AVG(co2) AS value
>     FROM telemetry
>     WHERE $__timeFilter(time)
>     GROUP BY 1, room
>     ORDER BY 1;

Настройте:

    Panel title: CO₂
    Unit: ppm

Добавьте порог:

    Warning: 800 ppm
    Critical: 1200 ppm

**Панель последних аварий**

Добавьте панель типа `Table`.

>     SELECT
>         event_time AS "Время",
>         room AS "Помещение",
>         measured_value AS "CO₂, ppm",
>         message AS "Сообщение"
>     FROM alerts
>     WHERE $__timeFilter(event_time)
>     ORDER BY event_time DESC
>     LIMIT 20;

Сохраните дашборд под названием:

    Smart Home Telemetry

**Этап считается выполненным, если**

Дашборд содержит не менее четырёх панелей:

- температура;
- влажность;
- CO₂;
- журнал аварий.

**Этап 14. Проверка всей системы**

Подтвердить работоспособность полного конвейера.

Выполните следующую последовательность:

1.  Запустите Mosquitto.

2.  Запустите `subscriber.py`.

3.  Запустите `publisher.py`.

4.  Убедитесь, что Publisher выводит JSON.

5.  Убедитесь, что Subscriber сообщает о пакетной записи.

6.  Выполните:

<!-- -->

    SELECT COUNT(*)
    FROM telemetry;

7.  Откройте Grafana.

8.  Установите временной диапазон:

<!-- -->

    Last 15 minutes

9.  Убедитесь, что графики обновляются.

10. Дождитесь превышения CO₂ либо вставьте тестовую строку.

11. Убедитесь, что авария появилась в Grafana.

**Результаты, которые необходимо получить**

Заполните таблицу:

  -----------------------------------------------
  Проверяемый элемент                 Результат
  ----------------------------------- -----------
  MQTT-брокер запущен                 

  Publisher подключён                 

  Subscriber подключён                

  Сообщения имеют формат JSON         

  Данные записываются пакетами        

  Гипертаблица создана                

  Аналитические запросы выполняются   

  Представление создано               

  SQL-функция работает                

  Триггер создаёт аварии              

  План запроса проанализирован        

  Grafana подключена                  

  Дашборд отображает телеметрию       
  -----------------------------------------------

**Условия выполнения практической работы**

Работа считается выполненной, если студент:

1.  запустил MQTT-брокер;

2.  передал тестовое сообщение;

3.  разработал Publisher на Python;

4.  сформировал JSON с телеметрией;

5.  создал гипертаблицу TimescaleDB;

6.  разработал Subscriber;

7.  реализовал проверку структуры сообщений;

8.  реализовал пакетную запись;

9.  накопил данные не менее чем за две минуты;

10. выполнил не менее трёх аналитических запросов;

11. использовал `time_bucket`;

12. создал SQL-представление;

13. создал SQL-функцию;

14. создал триггер;

15. проверил регистрацию аварии;

16. выполнил `EXPLAIN ANALYZE`;

17. подключил Grafana;

18. создал не менее трёх временных графиков;

19. создал таблицу аварий;

20. сформулировал вывод.

**Отчёт должен содержать:**

1.  Тему работы.

2.  Цель работы.

3.  Используемые технологии.

4.  Схему системы.

5.  Структуру MQTT-тем.

6.  Пример JSON-сообщения.

7.  Листинг Publisher.

8.  Структуру таблицы `telemetry`.

9.  Листинг Subscriber.

10. Результат проверки количества строк.

11. Результаты аналитических запросов.

12. SQL-код представления.

13. SQL-код функции.

14. SQL-код триггера.

15. Содержимое таблицы `alerts`.

16. Результат `EXPLAIN ANALYZE`.

17. Скриншот дашборда Grafana.

18. Ответы на контрольные вопросы.

19. Итоговый вывод.

**Требования к выводу**

В выводе необходимо указать:

- почему MQTT подходит для передачи телеметрии;
- какую роль выполняет брокер;
- почему телеметрия хранится как временной ряд;
- какие преимущества дала TimescaleDB;
- для чего использовалась гипертаблица;
- зачем создан индекс;
- как выполнялось агрегирование по времени;
- для чего создано представление;
- какую задачу решала SQL-функция;
- какую задачу решал триггер;
- какой способ доступа к данным показал план запроса;
- зачем применялась пакетная запись;
- какие панели были созданы в Grafana;
- где может применяться разработанная система.

**Контрольные вопросы**

1.  Какую задачу выполняет MQTT-брокер?

2.  Чем Publisher отличается от Subscriber?

3.  Что называется MQTT-темой?

4.  Для чего используются символы `+` и `#`?

5.  Что содержит Payload?

6.  Почему для телеметрии удобен JSON?

7.  Что такое временной ряд?

8.  Чем TimescaleDB отличается от обычной таблицы PostgreSQL?

9.  Что такое гипертаблица?

10. Для чего используется `time``_``bucket`?

11. Зачем нужен индекс по комнате и времени?

12. Что выполняет SQL-представление?

13. Чем представление отличается от таблицы?

14. Для чего используется SQL-функция?

15. Когда вызывается триггер?

16. Почему регистрацию аварии удобно выполнять триггером?

17. Что показывает `EXPLAIN ANALYZE`?

18. Чем `Index`` ``Scan` отличается от `Seq`` ``Scan`?

19. Почему пакетная запись быстрее отдельных операций вставки?

20. Какую роль выполняет очередь в программе Subscriber?

21. Почему обработка MQTT и запись в БД выполняются раздельно?

22. Как Grafana получает данные?

23. Что означает порог на панели CO₂?

24. Какие изменения необходимы для работы с реальными датчиками?

25. Какие меры безопасности необходимы в промышленной системе?

**Критерии оценивания**

  --------------------------------------
  Элемент работы                   Баллы
  ---------------------------- ---------
  Настройка MQTT                      10

  Publisher на Python                 10

  Структура TimescaleDB               10

  Subscriber и проверка JSON          15

  Пакетная запись                     10

  Аналитические запросы               10

  Представление и функция             10

  Триггер                             10

  Анализ плана запроса                 5

  Дашборд Grafana                     10

  **Итого**                      **100**
  --------------------------------------

Оценка:

  --------------------------------
       Баллы Оценка
  ---------- ---------------------
     86--100 отлично

      71--85 хорошо

      56--70 удовлетворительно

    менее 56 неудовлетворительно
  --------------------------------
