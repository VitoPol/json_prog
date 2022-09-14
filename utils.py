import json


def load_students():
    with open("students.json") as file:
        students = json.load(file)
    return students


def load_professions():
    with open("professions.json") as file:
        students = json.load(file)
    return students


def get_student_by_pk(pk: int):
    try:
        return load_students()[pk - 1]
    except:
        return None


def get_profession_by_title(title: str):
    for prof in load_professions():
        if prof["title"] == title:
            return prof
    return None


def check_fitness(student: dict, profession: dict):
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
