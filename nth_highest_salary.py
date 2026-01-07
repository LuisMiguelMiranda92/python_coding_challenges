"""
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 
Write a solution to find the nth highest distinct salary from the Employee table. 
If there are less than n distinct salaries, return null.

The result format is in the following example.
"""
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    column_name = f'getNthHighestSalary({N})'
    if N <= 0 or N > len(unique_salaries):
        return pd.DataFrame({column_name: [None]})
    nth_salary = unique_salaries.iloc[N - 1]
    return pd.DataFrame({column_name: [nth_salary]})