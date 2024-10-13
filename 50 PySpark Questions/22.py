# Databricks notebook source
"""write a spark program to find the managers who can ordered more than 4 reporting employees. Return employee ID and name of the employees"""


# COMMAND ----------

class Employee:
    def __init__(self, employee_id, emp_name, hire_date, job_id, salary, manager_id, department_id):
        self.employee_id = employee_id
        self.emp_name = emp_name
        self.hire_date = hire_date
        self.job_id = job_id
        self.salary = salary
        self.manager_id = manager_id
        self.department_id = department_id





employees_data = [
    Employee(100, "Steven", "1987-06-17", "AD_PRES", 24000.00, 0, 90),
    Employee(101, "Neena", "1987-06-18", "AD_VP", 17000.00, 100, 90),
    Employee(102, "Lex", "1987-06-19", "AD_VP", 17000.00, 100, 90),
    # Add more sample data here
]

# Convert list of Employee objects to DataFrame
employees_df = spark.createDataFrame(employees_data)
display(employees_df)

# COMMAND ----------

