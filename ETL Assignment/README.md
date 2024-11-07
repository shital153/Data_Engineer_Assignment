#  Marketing Strategy: Age Group Targeting Based on Sales Data

This project aims to analyze sales data for Company XYZ's signature items (x, y, z) and target specific age groups based on total quantities purchased. The analysis is performed using SQL and Python (Pandas), providing insights for a data-driven marketing strategy.

## Overview

This Python script connects to a SQLite database, extracts customer purchase information for a specific age group, and saves the result as a CSV file. The output shows the total quantities purchased for each item by each customer, only including customers aged 18-35.

## Database Schema

The database consists of four tables with the following relationships:

- **Customer**: Stores customer IDs and ages.
- **Sales**: Associates sales transactions with customers.
- **Orders**: Records item quantities for each sales transaction.
- **Items**: Contains item IDs and item names.

The relationships are as follows:
- `Customer` is linked to `Sales` via `customer_id`.
- `Sales` is linked to `Orders` via `sales_id`.
- `Orders` is linked to `Items` via `item_id`.

## Objectives

The script performs the following operations:
1. Filters customers aged between 18 and 35.
2. Joins the tables to get the complete data, including item names, quantities, and customer ages.
3. Aggregates the quantities per customer and item, excluding items with a total quantity of 0.
4. Saves the result to a CSV file with a semicolon (`;`) delimiter.

## Prerequisites

- Python 3
- SQLite3
- Pandas library (`pip install pandas`)

## Usage

1. Make sure `S30 ETL Assignment.db` (the SQLite database file) is in the same directory as the script.
2. Run the script:

   ```bash
   python age_group_sales_analysis.py
   python customer_analysis-sql.py
   
