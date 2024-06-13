import requests

from .base import VacancyApiClient, ApiBase
from ..dto import Vacancy, Salary


class ApiHH(ApiBase):
    """Подключение к API с параметрами, вернет ответ от API"""

    def connect_api(self, url: str, params: dict):
        response = requests.get(url=url, params=params, timeout=10)
        if response.status_code != 200:
            print(f"Ошибка\n"
                  f"{response.status_code}\n"
                  f"{response.content}")
            return None
        return response


class HeadHunterAPI(VacancyApiClient):

    def get_vacancies(self, search_text: str) -> list[Vacancy]:
        """Метод получения вакансий с указанного URL."""
        url = 'https://api.hh.ru/vacancies'
        params = {'only_with_salary': True, 'per_page': 100, 'text': search_text}
        response = ApiHH.connect_api(self=self, url=url, params=params)
        if response is None:
            return []
        return [
            self._parse_vacancy(item) for item in response.json()['items']
        ]

    def _parse_vacancy(self, data: dict) -> Vacancy:
        """Возвращает объект класса Vacancy"""
        return Vacancy(
            name=data['name'],
            url=data['alternate_url'],
            employer_name=data['employer']['name'],
            salary=Salary(salary_from=data['salary']['from'],
                          salary_to=data['salary']['to'],
                          currency=data['salary']['currency'])
        )
