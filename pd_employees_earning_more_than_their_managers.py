"""
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
 

Write a solution to find the employees who earn more than their managers.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
Output: 
+----------+
| Employee |
+----------+
| Joe      |
+----------+
Explanation: Joe is the only employee who earns more than his manager.
"""
import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # Merge the DataFrame with itself to get manager details on the same row.
    # An inner merge automatically handles employees without a managerId.
    merged_df = employee.merge(
        employee,
        left_on='managerId',
        right_on='id',
        suffixes=('_employee', '_manager')
    )
    
    # Filter for rows where the employee's salary is greater than the manager's.
    earns_more_df = merged_df[merged_df['salary_employee'] > merged_df['salary_manager']]
    
    # Select the employee's name and rename the column to 'Employee'.
    result_df = earns_more_df[['name_employee']].rename(columns={'name_employee': 'Employee'})
    
    return result_df
