import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()


def db_init():
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees
        (id INTEGER PRIMARY KEY,
        name TEXT, monthly_salary INTEGER,
        yearly_bonus INTEGER, position TEXT);''')
    conn.commit()


def add_employee():
    name = input("name>")
    monthly_salary = input("monthly_salary>")
    yearly_bonus = input("yearly_bonus>")
    position = input("position>")
    cursor.execute("INSERT INTO employees VALUES(NULL, ?, ?, ?, ?);",
    (name, monthly_salary, yearly_bonus, position))
    conn.commit()


def list_employees():
    query = cursor.execute("SELECT id, name, position FROM employees")
    for row in query:
        print("{} - {} - {}".format(row[0], row[1], row[2]))


def monthly_spending():
    query = cursor.execute("SELECT monthly_salary FROM employees")
    monthly_salary = 0
    for row in query:
        monthly_salary += row[0]
    print("The company is spending ${} every month!".format(monthly_salary))


def yearly_spending():
    query = cursor.execute("SELECT monthly_salary, yearly_bonus FROM employees")
    yearly_salary = 0
    for row in query:
        yearly_salary += row[0] * 12 + row[1]
    print("The company is spending ${} every year!".format(yearly_salary))


def delete_employee(id):
    cursor.execute("DELETE FROM employees WHERE id = {}".format(id))
    conn.commit()


def update_employee(id):
    name = input("name>")
    monthly_salary = input("monthly_salary>")
    yearly_bonus = input("yearly_bonus>")
    position = input("position>")
    cursor.execute('''UPDATE employees SET name = ?, monthly_salary = ?,
    yearly_bonus = ?, position = ? WHERE id = ?''', (
    name, monthly_salary, yearly_bonus, position, id))
    conn.commit()


def main():
    db_init()
    command = ""
    while command != "exit":
        command = input("command>")
        if command == "list_employees":
            list_employees()
        elif command == "add_employee":
            add_employee()
        elif command == "monthly_spending":
            monthly_spending()
        elif command == "yearly_spending":
            yearly_spending()
        elif command.startswith("update_employee"):
            update_employee(command.split(' ')[1])
        elif command.startswith("delete_employee"):
            delete_employee(command.split(' ')[1])
        elif command == "exit":
            print("Goodbye!")
        else:
            print('''Unknown command!\nPlease select one of the following:
    list_employees - Prints out all employees
    monthly_spending - Prints out the total sum for monthly spending
    yearly_spending - Prints out the total sum for one year
    add_employee - Starts to promt for data, to create a new employee
    delete_employee <employee_id> - Delete the given employee
    update_employee <employee_id> - Update the given employee''')


if __name__ == '__main__':
    main()
