# Завдання 2
# Реалізація програми для додавання, видалення та
# відстеження завдань/заміток. Зберігати ці завдання у
# форматі JSON у файлі. Можливість завантаження
# раніше збережених завдань для подальшої роботи з
# ними.

import json


def load_tasks(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_tasks(tasks, filename):
    with open(filename, 'w') as f:
        json.dump(tasks, f)


def add_task(task, tasks):
    tasks.append(task)
    print("Завдання додано.")


def remove_task(task_index, tasks):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print("Завдання '{}' видалено.".format(removed_task))
    else:
        print("Недійсний індекс завдання.")


def display_tasks(tasks):
    print("Ваші завдання:")
    for i, task in enumerate(tasks):
        print("{}. {}".format(i + 1, task))


if __name__ == "__main__":
    filename = "tasks.json"
    tasks = load_tasks(filename)

    while True:
        print("\nМеню:")
        print("1. Додати завдання")
        print("2. Видалити завдання")
        print("3. Відобразити всі завдання")
        print("4. Вийти")

        choice = input("Виберіть дію: ")

        if choice == "1":
            task = input("Введіть нове завдання: ")
            add_task(task, tasks)
        elif choice == "2":
            task_index = int(input("Введіть індекс завдання, яке потрібно видалити: ")) - 1
            remove_task(task_index, tasks)
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks, filename)
            print("Дані збережено. До побачення!")
            break
        else:
            print("Недійсний вибір. Будь ласка, виберіть знову.")

