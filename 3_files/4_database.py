import csv

groups = ("б03-107", "б03-108")

def add_student(db):
    try:
        entry = check_entry(input("Введите ФИО, курс и группу: ").strip())
        db.append(entry)
    except Exception as e:
        print(e.args[0])


def remove_student(db):
    name = tuple(input("Введите ФИО студента: ").strip().split())
    try:
        db.pop(db.index(next(e for e in db if e[:3] == name)))
    except StopIteration:
        print("Студент не найден!")


def list_group(db, args):
    try:
        group = args[1]

        for entry in db:
            if entry[-1].lower() == group:
                print(" ".join(entry))
    except IndexError:
        print("Укажите группу.")


def find_student(db, args):
    try:
        surname, name = args[2], args[3]

        for entry in db:
            if surname == entry[0].lower() and name == entry[1].lower():
                print(" ".join(entry))
    except IndexError:
        print("Укажите фамилию и имя студента.")


def check_entry(entry):
    entry = entry.split()

    try:
        year, group = entry[3], entry[4]
        if not ( float(year).is_integer() and 1 <= int(year) <= 6 ):
            raise ValueError("Недопустимый номер курса!")
        if group.lower() not in groups:
            raise ValueError("Недопустимая группа!")
    except IndexError:
        raise ValueError("Требуемый формат записи: ФИО, номер курса, группа")

    return tuple(entry)


def save_data(f, db):
    f.seek(0)
    f.truncate()
    writer = csv.writer(f)
    writer.writerows(db)
    # Закрываем, иначе файл пустой
    f.close()
    return open(f.name, "r+", encoding="utf8")



def end(f, db):
    print("\nСохранение изменений...")
    f = save_data(f, db)
    f.close()
    print("Выход")
    exit()


def main_loop(f, db):
    while True:
        try:
            cmd = input("Введите команду: ").strip().lower()
            if cmd == "сохранить изменения":
                f = save_data(f, db)
            elif cmd == "добавить студента":
                add_student(db)
            elif cmd == "удалить студента":
                remove_student(db)
            elif cmd.startswith("группа"):
                list_group(db, cmd.split())
            elif cmd.startswith("найти студента"):
                find_student(db, cmd.split())
            elif cmd in ("выход", "выйти"):
                end(f, db)
            else:
                print("Неизвестная команда!")
        except KeyboardInterrupt:
            end(f, db)


def read_data(f):
    db = []
    success = True
    
    for i, row in enumerate(csv.reader(f)):
        try:
            db.append(check_entry(" ".join(row)))
        except Exception as e:
            print(f"При чтении файла на строке {i+1} возникла ошибка:")
            print(e.args[0])
            success = False
            break

    return db if success else None


def start_main_loop(f):
    db = read_data(f)
    if db is not None:
        main_loop(f, db)
    exit() 


def open_file():
    path = input("Укажите путь к файлу базы данных: ")
    success = False
    f = None
    try:
        f = open(path, "r+", encoding="utf8")
        success = True
    except FileNotFoundError:
        print("По указанному пути файл базы данных не найден!")
    except PermissionError:
        print("Доступ к файлу базы данных запрещён!")
    except:
        print("Неизвестная ошибка при открытии файла базы данных!")
    else:
        start_main_loop(f)
    finally:
        if not success:
            open_dialogue(path)


def create_file(path):
    try:
        f = open(path, "x", encoding="utf8")
    except FileExistsError:
        print("Такой файл уже существует!")
    except PermissionError:
        print("Недостаточно прав для создания такого файла!")
    except:
        print("Неизвестная ошибка при создании файла!")
    else:
        print(f"Файл {path} создан.")
        f = open(f.name, "r+", encoding="utf8")
        start_main_loop(f)


def open_dialogue(path):
    print("""Выберите:
    1) Ввести другой путь
    2) Создать по указанному пути пустой файл базы данных""")
    try:
        ans = int(input())

        if ans == 1:
            open_file()
        elif ans == 2:
            create_file(path)
        else:
            raise ValueError
    except ValueError:
        print("Введите число от 1 или 2!")


open_file()
