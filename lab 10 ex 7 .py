import pickle

class Employee:
    def _init_(self, code, name, doj, salary):
        self.code = code
        self.name = name
        self.doj = doj
        self.salary = salary

emp = Employee("E101", "John Doe", "2022-01-10", 55000)

with open("employee.pkl", "wb") as f:
    pickle.dump(emp, f)

with open("employee.pkl", "rb") as f:
    emp_loaded = pickle.load(f)
    print(emp_loaded._dict_)
