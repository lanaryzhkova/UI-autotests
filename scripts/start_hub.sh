JAR="tools/selenium-server-4.44.0.jar"

echo "Запуск Selenium Grid Hub..."
cd "$(dirname "$0")/.."
java -jar "$JAR" hub