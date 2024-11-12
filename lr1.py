import sqlite3

# Создаем или подключаемся к базе данных
conn = sqlite3.connect('accounting.db')
cursor = conn.cursor()

# Создаем таблицу для сотрудников
cursor.execute('''CREATE TABLE IF NOT EXISTS employees (

                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  position TEXT,
                  salary REAL)''')

# Создаем таблицу для счетов
cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  account_number TEXT,
                  account_type TEXT,
                  balance REAL)''')

# Создаем таблицу для транзакций
cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  description TEXT,
                  amount REAL,
                  account_id INTEGER,
                  FOREIGN KEY (account_id) REFERENCES accounts(id))''')

# Функция для добавления нового сотрудника
def add_employee(name, position, salary):
    cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", (name, position, salary))
    conn.commit()
    print("Employee added successfully.")

# Функция для добавления нового счета
def add_account(account_number, account_type, balance):
    cursor.execute("INSERT INTO accounts (account_number, account_type, balance) VALUES (?, ?, ?)", (account_number, account_type, balance))
    conn.commit()
    print("Account added successfully.")

# Функция для добавления новой транзакции
def add_transaction(description, amount, account_id):
    cursor.execute("INSERT INTO transactions (description, amount, account_id) VALUES (?, ?, ?)", (description, amount, account_id))
    conn.commit()
    print("Transaction added successfully.")

# Функция для просмотра всех сотрудников
def view_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    for employee in employees:
        print(employee)

# Функция для просмотра всех счетов
def view_accounts():
    cursor.execute("SELECT * FROM accounts")
    accounts = cursor.fetchall()
    for account in accounts:
        print(account)

# Функция для просмотра всех транзакций
def view_transactions():
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    for transaction in transactions:
        print(transaction)

# Основной цикл приложения
while True:
    print("\n1. Add an employee")
    print("2. Add an account")
    print("3. Add a transaction")
    print("4. View employees")
    print("5. View accounts")
    print("6. View transactions")
    print("7. Exit")

    choice = input("Choose an action: ")

    if choice == '1':
        name = input("Enter employee name: ")
        position = input("Enter employee position: ")
        salary = float(input("Enter employee salary: "))
        add_employee(name, position, salary)
    elif choice == '2':
        account_number = input("Enter account number: ")
        account_type = input("Enter account type (e.g., Checking, Savings): ")
        balance = float(input("Enter account balance: "))
        add_account(account_number, account_type, balance)
    elif choice == '3':
        description = input("Enter transaction description: ")
        amount = float(input("Enter transaction amount: "))
        account_id = int(input("Enter account ID: "))
        add_transaction(description, amount, account_id)
    elif choice == '4':
        view_employees()
    elif choice == '5':
        view_accounts()
    elif choice == '6':
        view_transactions()
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please try again.")

# Закрываем соединение с базой данных
conn.close()
