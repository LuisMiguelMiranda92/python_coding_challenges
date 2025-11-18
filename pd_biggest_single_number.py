"""
+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
Each row of this table contains an integer.
 

A single number is a number that appeared only once in the MyNumbers table.

Find the largest single number. If there is no single number, report null.
"""
import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    single_numbers_df = my_numbers.drop_duplicates(subset=['num'], keep=False)
    result = single_numbers_df['num'].max()
    return pd.DataFrame({'num': [result]})