# UI-autotests
Блок U. UI autotests

## Описание

Автоматизированные UI тесты на Python + Selenium + pytest для сервиса https://www.way2automation.com

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск

### Запуск Selenium Grid

Запустить Hub:

```bash
./grid_scripts/start_hub.sh
```

Запустить Node:
```bash
./grid_scripts/start_node.sh
```

Проверить состояние Grid можно по адресу:
http://localhost:4444/ui


Запускать тесты можно с указанием количества потоков:
```bash
./grid_scripts/run_tests.sh 4
```
где 4 - количество потоков, 
если количество потоков не указано, то по умолчанию будет запуск в 2 потока

После выполнения тестов сгенерировать отчет:
```bash
allure serve
```

### Тесты подготовлены в соответствии с чек-листом для страниц авторизации и банкинга
