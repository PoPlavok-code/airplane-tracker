CREATE TABLE IF NOT EXISTS employers (
    employer_id INTEGER PRIMARY KEY,
    employer_name VARCHAR NOT NULL,
    employer_area VARCHAR,
    employer_url VARCHAR
);

CREATE TABLE IF NOT EXISTS vacancies (
    vacancy_id INTEGER PRIMARY KEY,
    vacancy_name VARCHAR NOT NULL,
    employer_id INTEGER REFERENCES employers(employer_id),
    salary_from INTEGER,
    salary_to INTEGER,
    salary_currency VARCHAR(10),
    vacancy_url VARCHAR,
    published_at DATE
);