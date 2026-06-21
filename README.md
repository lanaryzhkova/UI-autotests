# UI-autotests
Блок U. UI autotests

## Описание

Автоматизированные UI тесты на Python + Selenium + pytest для сервиса https://www.way2automation.com

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск

```bash
pytest -n auto --alluredir=./allure-results
allure serve
```

### Тесты подготовлены в соответствии с чек-листом для страниц авторизации и банкинга