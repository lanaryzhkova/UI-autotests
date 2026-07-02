import base64


def get_longest_word_from_elements(elements: list, default: str = "") -> str:
    """Получение самого длинного первого слова из списка элементов"""
    words = [elem.text.strip().split()[0] for elem in elements if elem.text.strip()]
    return max(words, key=len, default=default)

def str_to_base64(text: str) -> str:
    """Преобразование строки в base64"""
    return base64.b64encode(text.encode()).decode()