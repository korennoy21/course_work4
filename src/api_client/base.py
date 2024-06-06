from abc import ABC, abstractmethod

from src.dto import Vacancy


class VacancyApiClient(ABC):
    """Базовый класс api с методом получения вакансий"""

    @abstractmethod
    def get_vacancies(self, search_text: str) -> list[Vacancy]:
        pass
