import utils


def main():
    try:
        pk = int(input("Введите номер студента: "))
    except:
        print("неккоректный ввод")
        return
    student = utils.get_student_by_pk(pk)
    if not student:
        print("У нас нет такого студента")
        return
    print(f"Студент {student['full_name']}\nЛогин: {student['login']} ({'валидный' if utils.is_valid(student['login']) else 'не валидный'})\nЗнает ", end="")
    print(*student['skills'], sep=", ")
    title = input(f"\nВыберите специальность для оценки студента {student['full_name']}: ").capitalize()
    profession = utils.get_profession_by_title(title)
    if not profession:
        print("У нас нет такой специальности")
        return
    result = utils.check_fitness(student, profession)
    print(f"\nПригодность {result['fit_percent']}%")
    if result['has'] != []:
        print(f"{student['full_name']} знает ", end="")
        print(*result['has'], sep=", ")
    if result['lacks'] != []:
        print(f"{student['full_name']} не знает ", end="")
        print(*result['lacks'], sep=", ")


if __name__ == "__main__":
    main()
