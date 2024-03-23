import pytest
from src.vacancy_method import VacancyDataSaver
from src.API_classes import VacancyFromHH
from src.vacancy_classes import Vacancy

@pytest.fixture()
def manager():
    return Vacancy('Менеджер', "", 0, False, "Москва", "Работать", "2024-02-26T18:42:12+0300")

@pytest.fixture()
def developer():
    return Vacancy('Программист', "", 60000, 110000, "Москва", "Писать код", "2024-02-26T18:42:12+0300")

@pytest.fixture()
def driver():
    return Vacancy('Водитель', "", 0, 0, "Москва", "Писать код", "2024-02-26T18:42:12+0300")

@pytest.fixture()
def new_vacancy():
    return {'name': "Художник",
                'url': "нет ссылки",
                "salary": {
                    "from": 0,
                    "to": 0
                },
                "area": {"name": "Москва"},
                "snippet": {"requirements": "Рисовать картины."},
                "published_at": "2024-02-26T18:42:12+0300"
                }

def test_init(developer):
    assert developer.name == 'Программист'

def test_valid_salary(developer, manager):
    assert developer.valid_salary() == ('\n'
                                        '--------------------------------------------------\n\n'
                                        'Название вакансии: Программист\n'
                                        'Город: Москва\n'
                                        'Заработная плата: 60000-110000.\n'
                                        'Требования: Писать код\n'
                                        'Ссылка на вакансию: ')
    assert manager.valid_salary() == ('\n'
                                      '--------------------------------------------------\n\n'
                                      'Название вакансии: Менеджер\n'
                                      'Город: Москва\n'
                                      'Заработная плата: Зарплата не указана...\n'
                                      'Требования: Работать\n'
                                      'Ссылка на вакансию: ')

def test_compare_salary(manager, developer, driver):
    assert manager.compare_salary(developer) == 'Минимальная зарплата по вакансии Программист больше чем по вакансии Менеджер.'
    assert manager.compare_salary(driver) == 'Минимальные зарплата не указаны.'

def test_repr(developer, driver):
    assert repr(developer) == 'Вакансия Программист, опубликована 26.02.2024 18:42'
    assert repr(driver) == 'Вакансия Водитель, опубликована 26.02.2024 18:42'

def test_vacancy_method(new_vacancy):
    b = VacancyDataSaver()
    b.del_data()
    b.add_vacancies_to_file([new_vacancy])
    c = b.get_data_from_file()[-1]
    assert c["name"] == "Художник"

def test_get_vacancy_from_hh():
    data_dict = VacancyFromHH.get_vacancy_from_hh("python", 3)
    assert len(data_dict) <= 3

