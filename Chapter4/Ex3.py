class Employee:
    # Hàm khởi tạo
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    # Hàm tính lương
    def calculate_salary(self):
        return "Undefined"


class FullTimeEmployee(Employee):
    # Hàm khởi tạo
    def __init__(self, emp_id, name, base_salary):
        super().__init__(emp_id, name)
        self.base_salary = base_salary

    # Ghi đè hàm tính lương
    def calculate_salary(self):
        return self.base_salary


class PartTimeEmployee(Employee):
    # Hàm khởi tạo
    def __init__(self, emp_id, name, work_hours, hourly_rate):
        super().__init__(emp_id, name)
        self.work_hours = work_hours
        self.hourly_rate = hourly_rate

    # Ghi đè hàm tính lương
    def calculate_salary(self):
        return self.work_hours * self.hourly_rate


employees = [
    FullTimeEmployee("E01", "Nguyen Van A", 8000000),
    PartTimeEmployee("E02", "Tran Thi B", 40, 50000),
    FullTimeEmployee("E03", "Le Van C", 10000000),
    PartTimeEmployee("E04", "Pham Thi D", 25, 60000)
]


for employee in employees:
    print("Tên nhân viên:", employee.name)
    print("Lương:", employee.calculate_salary())
    print("--------------------------------")