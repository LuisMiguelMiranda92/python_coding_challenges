"""
Table: Orders

+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
order_number is the primary key (column with unique values) for this table.
This table contains information about the order ID and the customer ID.
 

Write a solution to find the customer_number for the customer who has placed the largest number of orders.

The test cases are generated so that exactly one customer will have placed more orders than any other customer.

The result format is in the following example.


"""
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders_count = orders['customer_number'].value_counts()
    largest_customer = orders_count[orders_count == orders['customer_number'].value_counts().max()]
    return largest_customer.reset_index()[['customer_number']]