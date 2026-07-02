# UI-autotests
Блок U. UI autotests

## Описание

Автоматизированные UI тесты на Python + Selenium + pytest для сервиса https://www.way2automation.com

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск

### Запуск локально


```bash
pytest --browser chrome
```
--browser — chrome / firefox / edge / ie

### Запуск через Selenium Grid

```bash
./scripts/start_hub.sh
```

```bash
./scripts/start_node.sh
```

```bash
pytest --remote --browser chrome  
```
--browser — chrome / firefox / edge / ie
--hub=http://localhost:4444 (по умолчанию)

**Проверить состояние Grid можно по адресу:**
http://localhost:4444/ui


**Запускать тесты можно с указанием количества потоков:**
```bash
pytest -n 4 --browser chrome
```
где 4 - количество потоков

После выполнения тестов сгенерировать отчет:
```bash
allure serve
```

### Тесты подготовлены в соответствии с чек-листом для страниц авторизации и банкинга
