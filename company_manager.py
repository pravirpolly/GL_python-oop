__author__ = 'Endri Dani'


####################################################################################################
# Abstract class Employee and subclasses HourlyEmployee, SalariedEmployee, Manager and Executive.  #
# Every one's pay is calculated differently. Company class that allows you to manage the employees.#
# You should be able to hire, fire and raise employees.                                            #
####################################################################################################


class Employee:
    hourly_pay = 9.62

    def __init__(self, name, worked_hours, salary):
        self.name = name
        self.worked_hours = worked_hours
        self.salary = salary + float(self.worked_hours) * Employee.hourly_pay

    def __str__(self):
        return "Full Name: {}\n  Worked hours: {}\n  Weekly Salary: ${}".format(self.name, self.worked_hours,
                                                                                round(self.salary, 2))


class HourlyEmployee(Employee):
    def __init__(self, name, worked_hours):
        super().__init__(name, worked_hours, salary=0)

    def __str__(self):
        return "Hourly Employee\n  {}".format(Employee.__str__(self))


class SalariedEmployee(Employee):
    def __init__(self, name):
        super().__init__(name, worked_hours=40, salary=0)

    def __str__(self):
        return "Salaried Employee\n  {}".format(Employee.__str__(self))


class Manager(Employee):
    def __init__(self, name, worked_hours):
        super().__init__(name, worked_hours, salary=550)

    def __str__(self):
        return "Manager\n  {}".format(Employee.__str__(self))


class Executive(Employee):
    def __init__(self, name, worked_hours):
        super().__init__(name, worked_hours, salary=850)

    def __str__(self):
        return "Executive\n  {}".format(Employee.__str__(self))


class Company:
    def __init__(self, name):
        self.name = name
        self.employees = {'H': [], 'P': [], 'M': [], 'E': []}

    def __str__(self):
        return self.name

    def hire_hourly_employee(self, employee_type, name, worked_hours):
        self.employees[employee_type].append(HourlyEmployee(name, worked_hours))

    def hire_salaried_employee(self, employee_type, name):
        self.employees[employee_type].append(SalariedEmployee(name))

    def hire_manager(self, employee_type, name, worked_hours):
        self.employees[employee_type].append(Manager(name, worked_hours))

    def hire_executive(self, employee_type, name, worked_hours):
        self.employees[employee_type].append(Executive(name, worked_hours))

    def fire_employee(self, employee_type, name):
        for item in self.employees[employee_type]:
            if item.name == name:
                self.employees[employee_type].remove(item)

    def raise_to_manager(self, to_type):
        name = input("Enter employee name: ")
        from_type = input("Enter employee position: ")
        for item in self.employees[from_type]:
            if item.name == name:
                self.employees[to_type].append(Manager(item.name, item.worked_hours))
                self.employees[from_type].remove(item)

    def raise_to_executive(self, to_type):
        name = input("Enter employee name: ")
        from_type = input("Enter employee position: ")
        for item in self.employees[from_type]:
            if item.name == name:
                self.employees[to_type].append(Executive(item.name, item.worked_hours))
                self.employees[from_type].remove(item)

    def show_employees(self, employee_type):
        for item in self.employees[employee_type]:
            print(item)

    def search_employee(self):
        name = input("Enter the employee name: ")
        for key in self.employees.keys():
            for item in self.employees[key]:
                if item.name == name:
                    print(item)


company = Company("Dani Security")
company.hire_hourly_employee("H", "Endri Dani", 100.35)
company.hire_hourly_employee("H", "Jona Zguri", 56.98)
company.hire_manager("M", "Albano Osmani", 2)
while True:
    print("\nWelcome to Dani Security!")
    print("  1. Show Hourly Employees\n  2. Show Salaried Employees\n  3. Show Managers\n  4. Show Executives\n  "
          "5. Search Employee\n  6. Raise to Manager\n  7. Raise to Executive\n  8. Quit" )
    choice = int(input("Enter your choice: "))
    if choice == 1:
        company.show_employees("H")
    elif choice == 2:
        company.show_employees("P")
    elif choice == 3:
        company.show_employees("M")
    elif choice == 4:
        company.show_employees("E")
    elif choice == 5:
        company.search_employee()
    elif choice == 6:
        company.raise_to_manager("M")
    elif choice == 7:
        company.raise_to_executive("E")
    else:
        print("Have a nice day!")
        break
