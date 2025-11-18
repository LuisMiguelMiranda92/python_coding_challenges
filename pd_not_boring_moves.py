"""
+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| id             | int      |
| movie          | varchar  |
| description    | varchar  |
| rating         | float    |
+----------------+----------+
id is the primary key (column with unique values) for this table.
Each row contains information about the name of a movie, its genre, and its rating.
rating is a 2 decimal places float in the range [0, 10]
 

Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".

Return the result table ordered by rating in descending order.
"""
import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    odd_id_mask = cinema['id'] % 2 != 0
    not_boring_mask = cinema['description'] != 'boring'
    combined_mask = (odd_id_mask) & (not_boring_mask)
    return cinema[combined_mask].sort_values(by='rating', ascending=False)