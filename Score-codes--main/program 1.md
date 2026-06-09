import pandas as pd
import matplotlib.pyplot as plt

# Recreate the daily sales data for analysis
 daily_sales_data = {
    "Date": [
        "2026-05-01", "2026-05-02", "2026-05-03",
        "2026-05-08", "2026-05-09", "2026-05-10"
    ],
    "Branch": [
        "KFC Chennai", "KFC Chennai", "KFC Chennai",
        "KFC Chennai", "KFC Chennai", "KFC Chennai"
    ],
    "Sales": [25000, 32000, 28000, 35000, 30000, 40000]
}

df_daily = pd.DataFrame(daily_sales_data)

# Convert Date column to datetime
 df_daily["Date"] = pd.to_datetime(df_daily["Date"])

# Extract day of the week for one of the plots
 df_daily['Day_of_Week'] = df_daily['Date'].dt.day_name()

# Create the figure and subplots
 fig, axes = plt.subplots(3, 1, figsize=(12, 18))

# Chart 1: Daily Sales Trend
 df_daily_sorted = df_daily.sort_values(by='Date')
 axes[0].plot(df_daily_sorted['Date'], df_daily_sorted['Sales'], marker='o', linestyle='-', color='blue')
 axes[0].set_title('1. Daily Sales Trend for KFC Chennai')
 axes[0].set_xlabel('Date')
 axes[0].set_ylabel('Sales')
 axes[0].grid(True)
 axes[0].tick_params(axis='x', rotation=45)

# Chart 2: Sales by Day of the Week
 sales_by_day_of_week = df_daily.groupby('Day_of_Week')['Sales'].sum().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
]).dropna()
 axes[1].bar(sales_by_day_of_week.index, sales_by_day_of_week.values, color='skyblue')
 axes[1].set_title('2. Total Sales by Day of the Week')
 axes[1].set_xlabel('Day of the Week')
 axes[1].set_ylabel('Total Sales')
 axes[1].tick_params(axis='x', rotation=45)
 axes[1].grid(axis='y', linestyle='--')

# Chart 3: Sales for Each Specific Date
 sales_per_date = df_daily.groupby('Date')['Sales'].sum().sort_index()
 axes[2].bar(sales_per_date.index, sales_per_date.values, color='lightcoral', width=0.8)
 axes[2].set_title('3. Sales for Each Specific Date')
 axes[2].set_xlabel('Date')
 axes[2].set_ylabel('Sales')
 axes[2].tick_params(axis='x', rotation=45)
 axes[2].grid(axis='y', linestyle='--')

plt.tight_layout()
plt.show()
