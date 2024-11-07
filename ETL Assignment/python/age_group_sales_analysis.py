import sqlite3
import pandas as pd
from pathlib import Path


def database_connection(current_dir):
    try:
        # Connect to DB and create a cursor

        sqliteConnection = sqlite3.connect(current_dir.parent / 'databases' / "S30 ETL Assignment.db")
        cursor = sqliteConnection.cursor()
        print('DB Init')

        customers_df = pd.read_sql('select * from customers', sqliteConnection)
        sales_df = pd.read_sql('select * from sales', sqliteConnection)
        items_df = pd.read_sql('select * from items', sqliteConnection)
        orders_df = pd.read_sql('select * from orders', sqliteConnection)

        # Close the cursor
        cursor.close()

        return customers_df, sales_df, items_df, orders_df
    # Handle errors
    except sqlite3.Error as error:
        print('Error occurred - ', error)


def extract_total_quantity(customers_df, sale_df, order_df, item_df):
    try:
        filtered_customer = customers_df[(customers_df['age'] >= 18) & (customers_df['age'] <= 35)]
        customer_data = (
            sale_df.merge(filtered_customer, on='customer_id')
            .merge(order_df, on='sales_id')
            .merge(item_df, on='item_id')
        )

        customer_data['quantity'] = customer_data['quantity'].fillna(0)

        final_result_data = (
            customer_data.groupby(['customer_id', 'age', 'item_name'], as_index=False)['quantity']
            .sum())

        final_result_data['quantity'] = final_result_data['quantity'].astype(int)

        final_result_data.rename(columns={'customer_id': 'Customer',
                                          'age': 'Age',
                                          'item_name': 'Item',
                                          'total_quantity': 'Quantity'}, inplace=True)

        return final_result_data

    except KeyError as e:
        print(f"KeyError: Missing column in the data. Details: {e}")
        return None
    except Exception as e:
        print(f"An error occurred during data processing: {e}")
        return None


if __name__ == "__main__":
    current_dir = Path(__file__).parent
    customer_df, sales_df, items_df, orders_df = database_connection(current_dir)
    final_result = extract_total_quantity(customer_df, sales_df, orders_df, items_df)
    if final_result is not None:
        final_result.to_csv(current_dir.parent / 'output_file' / 'output_pandas.csv', sep=';', index=False)
        print("Data saved successfully to 'output_pandas.csv'")
    else:
        print("Data processing failed.")
