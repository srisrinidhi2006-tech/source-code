import pandas as pd

# Sample KFC menu database for a data quality report
 data = {
    "Product_ID": ["K101", "K102", "K103", "K104", "K102"],
    "Menu_Item": [
        "Zinger Burger",
        "Chicken Bucket",
        "French Fries",
        "Pepsi",
        "Chicken Bucket"
    ],
    "Description": [
        "Spicy chicken burger",
        "Hot and crispy chicken",
        "Crispy potato fries",
        None,
        "Hot and crispy chicken"
    ],
    "Selling_Price": [199, 0, 99, 79, 599],
    "Cost_Price": [120, 250, 110, 40, 450],
    "Category": [
        "Burger",
        "Bucket Meals",
        "Sides",
        "Beverage",
        "Bucket Meals"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

print("KFC MENU DATA QUALITY REPORT")
print("=" * 45)

# 1. Missing Descriptions
missing_desc = df[
    df["Description"].isnull() |
    (df["Description"].astype(str).str.strip() == "")
]

# 2. Invalid Prices
invalid_price = df[df["Selling_Price"] <= 0]

# 3. Cost Greater Than Selling Price
cost_issue = df[df["Cost_Price"] > df["Selling_Price"]]

# 4. Missing Categories
missing_category = df[
    df["Category"].isnull() |
    (df["Category"].astype(str).str.strip() == "")
]

# 5. Duplicate Product IDs
duplicate_products = df[df.duplicated(subset=["Product_ID"], keep=False)]

# Summary Report
print(f"Missing Descriptions          : {len(missing_desc)}")
print(f"Zero/Negative Prices          : {len(invalid_price)}")
print(f"Cost > Selling Price Issues   : {len(cost_issue)}")
print(f"Missing Categories            : {len(missing_category)}")
print(f"Duplicate Product IDs         : {duplicate_products['Product_ID'].nunique()}")

print("\nDETAILED ISSUES")
print("=" * 45)

if not missing_desc.empty:
    print("\n1. Products with Missing Descriptions")
    print(missing_desc[["Product_ID", "Menu_Item"]])

if not invalid_price.empty:
    print("\n2. Products with Invalid Prices")
    print(invalid_price[["Product_ID", "Menu_Item", "Selling_Price"]])

if not cost_issue.empty:
    print("\n3. Products where Cost exceeds Selling Price")
    print(cost_issue[["Product_ID", "Menu_Item", "Cost_Price", "Selling_Price"]])

if not missing_category.empty:
    print("\n4. Products with Missing Categories")
    print(missing_category[["Product_ID", "Menu_Item"]])

if not duplicate_products.empty:
    print("\n5. Duplicate Product IDs")
    print(duplicate_products[["Product_ID", "Menu_Item"]])
