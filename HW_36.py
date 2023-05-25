class Employee:
    """Class representing an employee."""

    def __init__(self, name, position, salary):
        """
        Initialize an Employee object.

        Args:
            name (str): The name of the employee.
            position (str): The position of the employee.
            salary (float): The salary of the employee.
        """
        self.name = name
        self.position = position
        self.salary = salary

    def work(self):
        """
        Simulate the employee working.

        Returns:
            str: A message indicating that the employee is working.
        """
        return f"{self.name} is working as a {self.position}."

    def get_bonus(self, percentage):
        """
        Calculate the bonus amount based on the employee's salary and a given percentage.

        Args:
            percentage (float): The bonus percentage.

        Returns:
            float: The bonus amount.
        """
        bonus = self.salary * (percentage / 100)
        return bonus


class Company:
    """Class representing a company."""

    total_employees = 0

    def __init__(self, name):
        """
        Initialize a Company object.

        Args:
            name (str): The name of the company.
        """
        self.name = name

    def hire_employee(self, name, position, salary):
        """
        Hire a new employee.

        Args:
            name (str): The name of the employee.
            position (str): The position of the employee.
            salary (float): The salary of the employee.

        Returns:
            Employee: A newly hired Employee object.
        """
        employee = Employee(name, position, salary)
        self.__class__.total_employees += 1
        return employee

    @classmethod
    def get_total_employees(cls):
        """
        Get the total number of employees in the company.

        Returns:
            int: The total number of employees.
        """
        return cls.total_employees

    @staticmethod
    def get_company_info():
        """
        Get information about the company.

        Returns:
            str: Information about the company.
        """
        return "Welcome to our company!"

company = Company("XYZ Corporation")
print(company.get_company_info())  # Выводит "Welcome to our company!"
employee1 = company.hire_employee("John Doe", "Manager", 5000.0)
employee2 = company.hire_employee("Jane Smith", "Engineer", 4000.0)
print(employee1.work())  # Выводит "John Doe is working as a Manager."
print(employee2.get_bonus(10))  # Выводит 400.0

# Получение общего количества сотрудников в компании
total_employees = Company.get_total_employees()
print(f"Total employees: {total_employees}")  # Выводит "Total employees: 2"
