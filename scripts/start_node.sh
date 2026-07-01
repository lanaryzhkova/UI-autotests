JAR="tools/selenium-server-4.44.0.jar"

echo "Запуск Selenium Grid Node..."
cd "$(dirname "$0")/.."

java -jar "$JAR" node --hub http://localhost:4444 --port 5555 \
    --selenium-manager true
