"""
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| query_name  | varchar |
| result      | varchar |
| position    | int     |
| rating      | int     |
+-------------+---------+
This table may have duplicate rows.
This table contains information collected from some queries on a database.
The position column has a value from 1 to 500.
The rating column has a value from 1 to 5. Query with rating less than 3 is a poor query.
 

We define query quality as:

The average of the ratio between query rating and its position.

We also define poor query percentage as:

The percentage of all queries with rating less than 3.

Write a solution to find each query_name, the quality and poor_query_percentage.

Both quality and poor_query_percentage should be rounded to 2 decimal places.

Return the result table in any order.

The result format is in the following example.
"""
import pandas as pd
from decimal import Decimal, ROUND_HALF_UP



def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['poor_query']=queries['rating']<3
    queries['positionxrating']=queries.rating/queries.position+1e-6
    queries=queries.groupby('query_name', as_index=False).agg(quality=('positionxrating', 'mean'), poor_query_percentage=('poor_query', 'mean'))
    queries['poor_query_percentage']=queries['poor_query_percentage']*100
    return queries.round(2)