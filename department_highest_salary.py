"""
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 
Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.
 
Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in any order.

The result format is in the following example.
"""
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(employee, department, left_on='departmentId', right_on='id', how='left')
    merged_df = merged_df.rename(columns={'name_x': 'Employee', 'name_y': 'Department', 'salary': 'Salary'})

    merged_df['MaxSalary'] = merged_df.groupby('Department')['Salary'].transform('max')

    result = merged_df[merged_df['Salary'] == merged_df['MaxSalary']]
    return result[['Department', 'Employee', 'Salary']]