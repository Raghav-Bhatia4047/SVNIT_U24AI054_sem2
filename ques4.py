class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee: {self.name}, Salary: ${self.salary}"

    def __add__(self, other):
        if isinstance(other, Employee):
            combined_salary = self.salary + other.salary
            combined_name = self.name + " & " + other.name
            return Employee(combined_name, combined_salary)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Employee):
            salary_difference = abs(self.salary - other.salary)
            return salary_difference
        return NotImplemented

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
emp3 = Employee("Charlie", 45000)

combined_emp = emp1 + emp2
print(f"Combined Employee: {combined_emp}")

salary_diff = emp1 - emp2
print(f"Salary Difference between {emp1.name} and {emp2.name}: ${salary_diff}")

salary_diff_2 = emp1 - emp3
print(f"Salary Difference between {emp1.name} and {emp3.name}: ${salary_diff_2}")
