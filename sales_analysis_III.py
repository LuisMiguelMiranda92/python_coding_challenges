"""
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
| unit_price   | int     |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the name and the price of each product.
Table: Sales

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| seller_id   | int     |
| product_id  | int     |
| buyer_id    | int     |
| sale_date   | date    |
| quantity    | int     |
| price       | int     |
+-------------+---------+
This table can have duplicate rows.
product_id is a foreign key (reference column) to the Product table.
Each row of this table contains some information about one sale.
 

Write a solution to report the products that were only sold in the first quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.

Return the result table in any order.
"""
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # Define the date range for Q1 2019 (inclusive)
    Q1_START = pd.to_datetime('2019-01-01')
    Q1_END = pd.to_datetime('2019-03-31')

    # 1. Group by product_id and check for sales outside Q1.
    #    We use .agg(lambda x: ...) to create a boolean Series for each group,
    #    and then check if the maximum value is True (meaning at least one sale was outside Q1).
    product_q1_check = sales.groupby('product_id')['sale_date'].agg(
        was_sold_outside_q1=lambda x: (x.lt(Q1_START) | x.gt(Q1_END)).max()
    ).reset_index()

    # 2. Filter for products where no sale occurred outside Q1 (i.e., False/0)
    products_in_q1_only = product_q1_check[
        product_q1_check['was_sold_outside_q1'] == False
    ]

    # 3. Merge with the Product table to get the product_name
    result_df = product.merge(
        products_in_q1_only[['product_id']],
        on='product_id',
        how='inner'
    )

    # 4. Select and return the required columns
    return result_df[['product_id', 'product_name']]