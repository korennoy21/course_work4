from abc import ABC, abstractmethod

from src.dto import Vacancy


class BaseConnector(ABC):
    """Базовый класс коннектора файлов. Имеет 3 метода получения
    вакансий,добавления вакнсий,удаление вакансий из файла"""
    @abstractmethod
    def get_vacancies(self) -> list[Vacancy]:
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def del_vacancy(self, vacancy: Vacancy) -> None:
        pass
