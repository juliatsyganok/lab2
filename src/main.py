from class_task import Task, EmptyFieldError, InvalidPriorityError, InvalidStatusError, ReadOnlyFieldError

def main():
    task1 = Task("1", "Написать код", priority="high")
    task2 = Task("2", "Сделать тесты", priority="low", status="new")
    task3 = Task("3", "Задокументировать", status="in_progress")
    print(task1)
    print(task2)
    print(task3)
    print('\n')
    print(f"Task 1: {task1.is_ready}")
    print(f"Task 2: {task2.is_ready}")
    print(f"Task 3: {task3.is_ready}")
    print('\n')
    try:
        Task("", "Пустой ID")
    except EmptyFieldError as e:
        print(f"Пустой id: {e}")
    try:
        task1.priority = "urgent"
    except InvalidPriorityError as e:
        print(f"Неверный приоритет: {e}")
    try:
        task1.id = "new_id"
    except ReadOnlyFieldError as e:
        print(f"Нельзя менять id: {e}")
    try:
        task1.status = "invalid_status"
    except InvalidStatusError as e:
        print(f"Неверный статус: {e}")
    task1.status = "in_progress"
    print(f"После изменения статуса: {task1}")
    print(f"Готовность: {task1.is_ready}")
    
    task1.status = "done"
    print(f"После завершения: {task1}")
    print(f"Готовность: {task1.is_ready}")
    
    print("\n=== Информация о задаче ===")
    print(f"Время создания: {task1.created_at}")
    print(f"repr: {repr(task1)}")

if __name__ == "__main__":
    main()