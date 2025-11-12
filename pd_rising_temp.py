"""
Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.
 

Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

The result format is in the following example.


"""
import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])

    # 3. Sort by date (important to make sure .shift() is correct)
    weather = weather.sort_values(by='recordDate')

    # 4. Create new columns for the previous day's temperature and date
    weather['prev_temp'] = weather['temperature'].shift(1)
    weather['prev_date'] = weather['recordDate'].shift(1)

    # 5. Create a mask to find the rows that meet both conditions
    mask = (
        (weather['temperature'] > weather['prev_temp']) &
        (weather['recordDate'] - weather['prev_date'] == pd.Timedelta(days=1))
    )

    # 6. Apply the mask to get the final 'id's
    return weather[mask][['id']]