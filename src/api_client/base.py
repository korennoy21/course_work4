from abc import ABC, abstractmethod

from src.dto import Vacancy


class ApiBase(ABC):
    """Базовый класс для подключения к API """
    @abstractmethod
    def connect_api(self, url: str, params: dict):
        pass


class VacancyApiClient(ABC):
    """Базовый класс api с методом получения вакансий"""

    @abstractmethod
    def get_vacancies(self, search_text: str) -> list[Vacancy]:
        pass