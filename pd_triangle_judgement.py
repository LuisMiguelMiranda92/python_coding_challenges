"""
+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.
 

Report for every three line segments whether they can form a triangle.

Return the result table in any order.
"""
import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = np.where((triangle['x'] + triangle['y'] > triangle['z']) & (triangle['x'] + triangle['z'] > triangle['y']) & (triangle['y'] + triangle['z'] > triangle['x']), 'Yes', 'No')
    return triangle