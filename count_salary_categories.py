"""
+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
account_id is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.
 

Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a category, return 0.

Return the result table in any order.

The result format is in the following example.
"""
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # 1. Calculate the counts directly using boolean summing
    # This is faster and safer than groupby because it handles 0-counts automatically.
    low_count = (accounts['income'] < 20000).sum()
    high_count = (accounts['income'] > 50000).sum()
    
    # Average is whatever is left (Total Rows - Low - High)
    avg_count = len(accounts) - low_count - high_count

    # 2. Build the result DataFrame manually
    result = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low_count, avg_count, high_count]
    })

    return result