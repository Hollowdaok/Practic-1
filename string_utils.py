def print_string(s):
    if not isinstance(s, str):
        return "Помилка: функція приймає тільки рядки!"
    else:
        return s

def check_case(s):
    if not isinstance(s, str):
        return "Помилка: функція приймає тільки рядки!"

    if s.isupper():
        return "Всі великі"
    elif s.islower():
        return "Всі малі"
    else:
        return "Змішані"

def to_upper_list(word):
    return [ch.upper() for ch in word]