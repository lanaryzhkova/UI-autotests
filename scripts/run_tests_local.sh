cd "$(dirname "$0")/.."

THREADS=${1:-2}
BROWSER=${2:-Chrome}

echo "Запуск тестов, количество потоков (воркеров) $THREADS..."
pytest -n "$THREADS" --dist=loadfile \
  --driver "$BROWSER"