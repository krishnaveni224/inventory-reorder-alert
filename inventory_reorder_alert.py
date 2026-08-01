import csv

# List to store items that need restocking
restock_items = []

# Read the stock CSV file
try:
    with open("stock.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                item = row["Item"]
                quantity = int(row["Quantity"])
                threshold = int(row["Threshold"])

                # Check stock level
                if quantity <= threshold:
                    print(f"{item} - REORDER")

                    restock_items.append({
                        "Item": item,
                        "Quantity": quantity,
                        "Threshold": threshold
                    })
                else:
                    print(f"{item} - IN STOCK")

            except (ValueError, KeyError):
                print("Skipping invalid row")

except FileNotFoundError:
    print("Error: stock.csv file not found.")

# Create restock report CSV
with open("restock_report.csv", "w", newline="") as file:
    fieldnames = ["Item", "Quantity", "Threshold"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for item in restock_items:
        writer.writerow(item)

print("\nRestock report created successfully!")

# Print Restock Report
print("\n------ RESTOCK NEEDED REPORT ------")

if restock_items:
    for item in restock_items:
        print(f"Item: {item['Item']}")
        print(f"Current Quantity: {item['Quantity']}")
        print(f"Reorder Threshold: {item['Threshold']}")
        print("----------------------------")
else:
    print("All items are sufficiently stocked.")

# Bonus: Simulated Email Alert
print("\n========== EMAIL ALERT ==========")
print("Subject: Inventory Reorder Alert\n")

if restock_items:
    print("Dear Warehouse Manager,\n")
    print("The following items need to be reordered:\n")

    for item in restock_items:
        print(f"- {item['Item']} (Current: {item['Quantity']}, Threshold: {item['Threshold']})")

    print("\nPlease restock these items as soon as possible.")
else:
    print("All items are sufficiently stocked.")
    
