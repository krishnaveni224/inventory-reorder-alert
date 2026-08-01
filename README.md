# Inventory Reorder Alert System

## Description
This project is a Python-based inventory reorder alert system. It reads stock data from a CSV file, compares the current quantity with the reorder threshold, identifies items that need restocking, and generates a `restock_report.csv` file.

## Features
- Read inventory data from a CSV file
- Compare stock quantity with reorder threshold
- Display REORDER or IN STOCK status
- Generate a restock report in CSV format
- Basic error handling

## Technologies Used
- Python
- CSV Module

## Files
- inventory_reorder_alert.py
- stock.csv
- restock_report.csv

## How to Run
1. Place `stock.csv` in the project folder.
2. Run:
   ```bash
   python inventory_reorder_alert.py
   ```
3. The program will display the inventory status and generate `restock_report.csv`.
