import requests
import json
from API_classes import API
from API_classes import Vacancy


def get_vacancy_from_hh():
    url_post = "https://api.hh.ru/vacancies"  # используемый адрес для отправки запроса

    response = requests.post(url_post)  # отправка POST-запроса

    print(response)  # вывод объекта класса Response
    print(response.status_code)  # вывод статуса запроса, 200 означает, что всё хорошо
    print(response.text)  # печать ответа в виде текста того, что вернул нам внешний сервис
    print(response.json())  # печать ответа в виде json объекта того, что нам вернул внешний сервис

get_vacancy_from_hh()

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = API()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancy_from_hh("Python")
"""
# Преобразование набора данных из JSON в список объектов
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
"""
# Пример работы контструктора класса с одной вакансией
vacancy = Vacancy("Python Developer", "", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
manager = Vacancy("Менеджер", "", 50000, "нет описания")

"""# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.add_vacancy(vacancy)
json_saver.delete_vacancy(vacancy)"""