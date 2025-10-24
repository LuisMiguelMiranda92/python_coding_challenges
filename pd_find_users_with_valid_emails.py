"""
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
| mail          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains information of the users signed up in a website. Some e-mails are invalid.
 

Write a solution to find the users who have valid emails.

A valid e-mail has a prefix name and a domain where:

The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter.
The domain is '@leetcode.com'.
Return the result table in any order.
"""
import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'
    mask = users['mail'].str.match(pattern)
    
    return users[mask]