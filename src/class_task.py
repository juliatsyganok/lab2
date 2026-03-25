from datetime import datetime
from typing import Optional, Any

class TaskValidationError(Exception):
    """Базовое исключение для ошибок валидации задачи"""
    pass

class InvalidPriorityError(TaskValidationError):
    """Некорректный приоритет"""
    pass

class InvalidStatusError(TaskValidationError):
    """Некорректный статус"""
    pass

class EmptyFieldError(TaskValidationError):
    """Пустое поле"""
    pass

class ReadOnlyFieldError(TaskValidationError):
    """Попытка изменить readonly поле"""
    pass


class NonEmptyString:
    """Дескриптор для непустых строк"""
    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)
    
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f"{self.private_name[1:]} must be a string")
        if not value.strip():
            raise EmptyFieldError(f"{self.private_name[1:]} cannot be empty")
        setattr(instance, self.private_name, value)


class ReadOnlyAfterInit(NonEmptyString):
    """Дескриптор, который можно установить только один раз"""
    def __set__(self, instance, value):
        if hasattr(instance, self.private_name):
            raise ReadOnlyFieldError(f"{self.private_name[1:]} cannot be changed after initialization")
        super().__set__(instance, value)


class ChoiceDescriptor:
    """Дескриптор для атрибута с ограниченным набором значений"""
    def __init__(self, allowed_values, error_class):
        self.allowed_values = allowed_values
        self.error_class = error_class
    
    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)
    
    def __set__(self, instance, value):
        if value not in self.allowed_values:
            raise self.error_class(
                f"{self.private_name[1:]} must be one of {self.allowed_values}, got '{value}'"
            )
        setattr(instance, self.private_name, value)


class Task:
    """класс задачи"""
    id = ReadOnlyAfterInit()
    description = NonEmptyString()
    priority = ChoiceDescriptor(["low", "medium", "high"], InvalidPriorityError)
    status = ChoiceDescriptor(["new", "in_progress", "done"], InvalidStatusError)
    
    def __init__(self, task_id: str, description: str, priority: str = "medium", status: str = "new"):
        self.id = task_id
        self.description = description
        self.priority = priority
        self.status = status
        self._created_at = datetime.now()
    
    @property
    def created_at(self) -> datetime:
        """Время создания задачи"""
        return self._created_at
    
    @property
    def is_ready(self) -> bool:
        return self.status != "done" and self.priority != "low"
    
    def __repr__(self) -> str:
        return (
            f"Task(id={self.id!r}, description={self.description!r}, "
            f"priority={self.priority!r}, status={self.status!r}, "
            f"created_at={self.created_at.isoformat()!r})"
        )
    