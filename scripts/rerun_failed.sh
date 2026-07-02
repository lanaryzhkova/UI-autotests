cd "$(dirname "$0")/.."
echo "Запуск только упавших тестов..."
pytest --last-failed