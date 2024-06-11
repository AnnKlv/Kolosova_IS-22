# Приложение СТРАХОВАЯ КОМПАНИЯ для некоторой организации. БД должна содержать таблицу Договор
# со следующей структурой записи: дата заключения, страховая сумма, вид страхования, тарифная ставка и филиал,
# в котором заключался договор.

import sqlite3 as sq

# Подключение к базе данных
conn = sq.connect('insurance.db')
c = conn.cursor()

# Создание таблицы Contract, если она не существует
c.execute("""CREATE TABLE IF NOT EXISTS Contract (
    contract_id INTEGER PRIMARY KEY AUTOINCREMENT,
    signing_date DATE,
    insurance_amount DECIMAL,
    insurance_type VARCHAR,
    tariff_rate DECIMAL,
    branch VARCHAR
)""")

# Функция для добавления нового договора
def add_contract(signing_date, insurance_amount, insurance_type, tariff_rate, branch):
    c.execute("INSERT INTO Contract (signing_date, insurance_amount, insurance_type, tariff_rate, branch) VALUES (?, ?, ?, ?, ?)", (signing_date, insurance_amount, insurance_type, tariff_rate, branch))
    conn.commit()

# Вывод всех договоров
def show_contracts():
    c.execute("SELECT * FROM Contract")
    contracts = c.fetchall()
    for contract in contracts:
        print(contract)

# Поиска договора по ID
def find_contract_by_id(contract_id):
    c.execute("SELECT * FROM Contract WHERE contract_id=?", (contract_id,))
    contract = c.fetchone()
    if contract:
        print(contract)
    else:
        print("Контракт не найден")

# Удаления договора по ID
def delete_contract_by_id(contract_id):
    c.execute("DELETE FROM Contract WHERE contract_id=?", (contract_id,))
    conn.commit()

# Редактирования договора
def update_contract_insurance_type(contract_id, new_insurance_type):
    c.execute("UPDATE Contract SET insurance_type=? WHERE contract_id=?", (new_insurance_type, contract_id))
    conn.commit()

# Добавление договоров
add_contract('2023-05-01', 100000.0, 'Автострахование', 0.05, 'Москва')
add_contract('2023-05-15', 50000.0, 'Страхование жизни', 0.03, 'Санкт-Петербург')
add_contract('2023-06-01', 75000.0, 'Медицинское страхование', 0.04, 'Москва')

# Показывает
show_contracts()

# Находит по ID
find_contract_by_id(1)

# Удаляет по ID
delete_contract_by_id(2)

# Обновляет вид страхования для договора
update_contract_insurance_type(1, 'Страхование имущества')

conn.close()