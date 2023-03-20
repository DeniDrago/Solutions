import csv

TASKS_FILE = "tasks.csv"


def main(tasks):
    while True:
        print("Выберите действие:")
        print("1. Вывести список задач")
        print("2. Добавить задачу")
        print("3. Отметить задачу выполненной")
        print("4. Редактировать список задач")
        print("5. Выход")

        choice = input("> ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            edit_list(tasks)
        elif choice == "5":
            break
        else:
            print("Неправильный выбор. Попробуйте еще раз.")


def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст")
    else:
        print("Список задач:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_tasks(tasks):
    task = input("Введите задачу: ")
    if not task:
        print("Нельзя добавить пустую задачу")
        return

    if task in tasks:
        print("Такая задача уже существует")
        return

    tasks.append(task)
    write_tasks(tasks)
    print("Задача добавлена")


def complete_task(tasks):
    if not tasks:
        print("Список задач пуст")
        return

    print("Выберите номер задачи, которую хотите отметить выполненной:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    choice = input("> ")

    try:
        task_number = int(choice)
        if task_number < 1 or task_number > len(tasks):
            raise ValueError
    except ValueError:
        print("Неправильный выбор. Попробуйте еще раз.")
        return

    task = tasks[task_number - 1]
    tasks.remove(task)
    write_tasks(tasks)
    print(f"Задача '{task}' отмечена выполненной")


def edit_list(tasks):
    if not tasks:
        print('\nЗадач для редактирования нет')
        return

    print('\nСписок задач для редактирования:')
    for i, task in enumerate(tasks, 1):
        print(f'{i}. {task}')

    while True:
        num_task = input('\nВведите номер задачи для редактирования или "Q/q" для выхода в основное меню: ')
        if num_task in ('Q', 'q'):
            break

        try:
            task_number = int(num_task)
        except ValueError:
            print("Неправильный ввод. Введите число.")
            continue

        if task_number < 1 or task_number > len(tasks):
            print("Неправильный номер задачи. Попробуйте еще раз.")
            continue

        task = tasks[task_number - 1]
        new_task = input(f'Введите новое название задачи "{task}": ')
        if not new_task:
            print("Нельзя добавить пустую задачу")
            continue
        if new_task == task:
            print("Название задачи не изменено, так как оно осталось таким же")
            continue
        if new_task in tasks:
            print("Такая задача уже существует")
            continue

        tasks[task_number - 1] = new_task

        write_tasks(tasks)
        print(f"Задача '{task}' была изменена на '{new_task}'")
        break


def read_tasks():
    try:
        with open(TASKS_FILE, "r", newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            tasks = []
            for row in reader:
                tasks.append(row[0])

    except FileNotFoundError:
        tasks = []
    return tasks


def write_tasks(tasks):
    with open(TASKS_FILE, "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task])


if __name__ == "__main__":
    read_file = read_tasks()
    main(read_file)
