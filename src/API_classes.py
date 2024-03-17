from abc import ABC, abstractmethod
import requests
import json


class API(ABC):
    """абстрактный класс для работы с API сервиса с вакансиями"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancy_from_hh(self):
        pass

    @abstractmethod
    def api_connecton(self):
        pass


class VacancyFromHH(API):
    """
    класс, наследующийся от абстрактного класса, для работы с платформой hh.ru.
    Класс умеет подключаться к API и получать вакансии."""
    @classmethod
    def get_vacancy_from_hh(self, text):
        parameters = {'text': text,
                      'currency': 'RUR',
                      'order_by': 'salary_desc'
                      }
        response = requests.get("https://api.hh.ru/vacancies", params=parameters)
        return response.json()['items']


a = VacancyFromHH.get_vacancy_from_hh('python')

with open('Vacancies_JSON.json', 'w', encoding="UTF-8") as f:
    json.dump(a, f, indent=2, ensure_ascii=False)
[print(item) for item in a]

