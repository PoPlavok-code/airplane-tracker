from dataclasses import dataclass
from typing import Optional


@dataclass
class Vacancy:
    """
    Класс для представления вакансии.

    Attributes:
        vacancy_id (int): Идентификатор вакансии.
        name (str): Название вакансии.
        employer_name (str): Название работодателя.
        salary_from (Optional[int]): Минимальная зарплата.
        salary_to (Optional[int]): Максимальная зарплата.
        salary_currency (Optional[str]): Валюта зарплаты.
        url (str): Ссылка на вакансию.
    """
    vacancy_id: int
    name: str
    employer_name: str
    salary_from: Optional[int]
    salary_to: Optional[int]
    salary_currency: Optional[str]
    url: str

    def __str__(self) -> str:
        """Возвращает строковое представление вакансии."""
        salary = f"{self.salary_from or ''} - {self.salary_to or ''} {self.salary_currency or ''}".strip()
        return f"{self.name} ({self.employer_name}) | ЗП: {salary or 'не указана'} | {self.url}"