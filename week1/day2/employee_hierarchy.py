class Employee():
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_wage):
        super().__init__(name)
        self.hourly_wage = hourly_wage

    def weeklyPay(self, hours):
        salary = 0
        if(hours > 40):
            salary += self.hourly_wage * 40
            salary += self.hourly_wage * (hours - 40) * 1.5
        else:
            salary += self.hourly_wage * hours
        return salary


class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def weeklyPay(self, hours):
        return self.salary / 52


class Manager(SalariedEmployee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def weeklyPay(self, hours):
        return (self.salary / 52) + self.bonus


def main():
    staff = []
    staff.append(HourlyEmployee("Morgan, Harry", 30.0))
    staff.append(SalariedEmployee("Lin, Sally", 52000.0))
    staff.append(Manager("Smith, Mary", 104000.0, 50.0))

    for employee in staff:
        hours = int(input("Hours worked by " + employee.getName() + ": "))
        pay = employee.weeklyPay(hours)
        print("Salary: %.2f" % pay)

if __name__ == "__main__":
    main()