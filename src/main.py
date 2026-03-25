from class_task import Task

def main():
    task1 = Task("1", "Написать код", priority="high")
    task2 = Task("2", "Сделать тесты", priority="low", status="new")
    task3 = Task("3", "Задокументировать", status="in_progress")
    
    print("Создано:")
    print(task1)
    print(task2)
    print(task3)
    print()
    print(f"Task 1 (high, new): {task1.is_ready}")
    print(f"Task 2 (low, new): {task2.is_ready}")
    print(f"Task 3 (medium, in_progress): {task3.is_ready}")
    print()
    try:
        Task("", "Пустой ID")
    except ValueError as e:
        print(f"Пустой ID: {e}")
    try:
        task1.priority = "urgent"
    except ValueError as e:
        print(f"Ошибка приоритета: {e}")
    try:
        task1.id = "new_id"
    except AttributeError as e:
        print(f"Ошибка изменения: {e}")
    try:
        task1.status = "invalid_status"
    except ValueError as e:
        print(f"Ошибка статуса: {e}")

    task1.status = "in_progress"
    print(f"После изменения статуса: {task1}")
    print(f"Готовность: {task1.is_ready}")
    
    task1.status = "done"
    print(f"После завершения: {task1}")
    print(f"Готовность: {task1.is_ready}")
    
    print(f"ID: {task1.id}")
    print(f"Описание: {task1.description}")
    print(f"Приоритет: {task1.priority}")
    print(f"Статус: {task1.status}")
    print(f"Время создания: {task1.created_at}")
    print(f"repr: {repr(task1)}")

if __name__ == "__main__":
    main()