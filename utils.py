import json


def load_students() -> list:
    """
    Вытаскивает данные из файла students.json
    :return: список студентов
    """
    with open("students.json") as file:
        students = json.load(file)
    return students


def load_professions() -> list:
    """
    Вытаскивает данные из файла professions.json
    :return: список профессий
    """
    with open("professions.json") as file:
        professions = json.load(file)
    return professions


def get_student_by_pk(pk: int) -> dict or None:
    """
    Вытаскивает из файла данные студента по его номеру
    :param pk: номер студента
    :return: словарь с данными студента если он найден
    """
    try:
        return load_students()[pk - 1]
    except:
        return None


def get_profession_by_title(title: str) -> dict or None:
    """
    Вытаскивает из файла данные по профессии по её названию
    :param title: название профессии
    :return: словарь с данными по профессии если она найдена
    """
    for prof in load_professions():
        if prof["title"] == title:
            return prof
    return None


def check_fitness(student: dict, profession: dict) -> dict:
    """
    возвращает информацию о пригодности студента
    :param student: данные студента
    :param profession: данные профессии
    :return: словарь с информацией о пригодности
    """
    student_set = set(student["skills"])
    profession_set = set(profession["skills"])

    has = list(student_set.intersection(profession_set))
    lacks = list(profession_set.difference(student_set))
    fit_percent = round(len(has) / len(profession_set) * 100)

    result = {
        "has": has,
        "lacks": lacks,
        "fit_percent": fit_percent
    }

    return result
