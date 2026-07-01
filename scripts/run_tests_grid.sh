cd "$(dirname "$0")/.."

THREADS=${1:-2}

echo "Запуск тестов, количество потоков (воркеров) $THREADS..."
pytest -n "$THREADS" --dist=loadfile \
  --driver Remote \
  --selenium-host localhost \
  --selenium-port 4444 \
  --capability browserName chrome