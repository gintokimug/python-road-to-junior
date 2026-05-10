class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def get_total_salary(self):
        return self.base_salary

class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name,base_salary)
        self.bonus = bonus

    def get_total_salary(self):
        return self.base_salary + self.bonus
    
class Director(Manager):
    def __init__(self, name, base_salary,bonus, stock_options):
        super().__init__(name, base_salary,bonus)
        self.stock_options = stock_options
    
    def get_total_salary(self):
        return super().get_total_salary() + self.stock_options
    


emp = Employee("Anton", 50000)
man = Manager("Oleg", 25000, 25000)
dir = Director("Sergey", 25000, 50000, 75000)

print(f"{dir.name}: {dir.get_total_salary()}")
print(f"{emp.name}: {emp.get_total_salary()}") 
print(f"{man.name}: {man.get_total_salary()}")




        