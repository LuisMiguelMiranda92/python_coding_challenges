"""
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| sell_date   | date    |
| product     | varchar |
+-------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each row of this table contains the product name and the date it was sold in a market.
 
Write a solution to find for each date the number of different products sold and their names.

The sold products names for each date should be sorted lexicographically.
Return the result table ordered by sell_date.

The result format is in the following example.
Output: 
+------------+----------+------------------------------+
| sell_date  | num_sold | products                     |
+------------+----------+------------------------------+
| 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
| 2020-06-01 | 2        | Bible,Pencil                 |
| 2020-06-02 | 1        | Mask                         |
+------------+----------+------------------------------+
"""
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities.drop_duplicates(['sell_date','product'],inplace= True)
    df = activities.groupby('sell_date')['product'].agg(num_sold = 'count',products = lambda x: ','.join(sorted(x))).reset_index()
    return df.sort_values(by='sell_date')
