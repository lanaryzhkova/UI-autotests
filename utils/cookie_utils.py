import json
from pathlib import Path

COOKIES_PATH = Path("data/cookies.json")

def cookies_exist() -> bool:
    """Метод проверки наличия файла с cookie
    Returns:
        True, если файл с куки сохранен
    """
    return COOKIES_PATH.exists()

def save_cookies(driver):
    """Сохранение cookie в файл"""
    with open(COOKIES_PATH, "w") as file:
        json.dump(driver.get_cookies(), file)

def load_cookies(driver):
    """Загрузка cookie в браузер"""
    with open("data/cookies.json", "r") as f:
        cookies = json.load(f)

    for cookie in cookies:
        driver.add_cookie(cookie)