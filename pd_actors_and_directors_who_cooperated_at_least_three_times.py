"""
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| actor_id    | int     |
| director_id | int     |
| timestamp   | int     |
+-------------+---------+
timestamp is the primary key (column with unique values) for this table.
 

Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.

Return the result table in any order.
"""
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    pair_counts = actor_director[['actor_id', 'director_id']].value_counts()
    pairs_with_3_plus_appearances = pair_counts[pair_counts >= 3].reset_index()
    return pairs_with_3_plus_appearances[['actor_id', 'director_id']]