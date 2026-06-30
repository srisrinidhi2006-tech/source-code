import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# -----------------------------
# Create the DataFrame
# -----------------------------
daily_sales_data = {
    "Date": [
        "2026-05-01",
        "2026-05-02",
        "2026-05-03",
        "2026-05-08",
        "2026-05-09",
        "2026-05-10"
    ],
    "Branch": [
        "KFC Chennai",
        "KFC Chennai",
        "KFC Chennai",
        "KFC Chennai",
        "KFC Chennai",
        "KFC Chennai"
    ],
    "Sales": [25000, 32000, 28000, 35000, 30000, 40000]
}

df = pd.DataFrame(daily_sales_data)

df["Date"] = pd.to_datetime(df["Date"])
df["Day_of_Week"] = df["Date"].dt.day_name()

# Sort by date
df = df.sort_values("Date")

# Sales by day
sales_by_day = (
    df.groupby("Day_of_Week")["Sales"]
    .sum()
    .reindex([
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ])
    .dropna()
)

# Sales by date
sales_per_date = df.groupby("Date")["Sales"].sum()

# ----------------------------------------------------
# Create Figure
# ----------------------------------------------------
fig, axes = plt.subplots(3, 1, figsize=(10, 16), dpi=150)

# Large spacing between charts
fig.subplots_adjust(
    top=0.98,
    bottom=0.08,
    left=0.08,
    right=0.97,
    hspace=3.5
)

# ====================================================
# Chart 1 - Daily Sales Trend
# ====================================================

axes[0].plot(
    df["Date"],
    df["Sales"],
    marker="8",
    linewidth=10,
    markersize=17,
    color="royalblue"
)

axes[0].set_title(
    "1. Daily Sales Trend for KFC Chennai",
    fontsize=18,
    fontweight="bold",
    pad=35
)

axes[0].set_xlabel("Date", fontsize=10, labelpad=15)
axes[0].set_ylabel("Sales (₹)", fontsize=10)

axes[0].grid(True, linestyle="--", alpha=0.6)

axes[0].xaxis.set_major_formatter(mdates.DateFormatter("%d-%b"))
axes[0].tick_params(axis="x", rotation=30, labelsize=10)

for x, y in zip(df["Date"], df["Sales"]):
    axes[0].text(
        x,
        y + 800,
        f"{y:,}",
        ha="center",
        fontsize=10
    )

# ====================================================
# Chart 2 - Sales by Day
# ====================================================

bars = axes[1].bar(
    sales_by_day.index,
    sales_by_day.values,
    color="skyblue",
    edgecolor="black",
    linewidth=2.5
)

axes[1].set_title(
    "2. Total Sales by Day of the Week",
    fontsize=18,
    fontweight="bold",
    pad=35
)

axes[1].set_xlabel("Day of the Week", fontsize=10, labelpad=15)
axes[1].set_ylabel("Sales (₹)", fontsize=10)

axes[1].grid(axis="y", linestyle="--", alpha=0.6)

axes[1].tick_params(axis="x", rotation=25, labelsize=10)

for bar in bars:
    h = bar.get_height()
    axes[1].text(
        bar.get_x() + bar.get_width()/2,
        h + 900,
        f"{int(h):,}",
        ha="center",
        fontsize=10
    )

# ====================================================
# Chart 3 - Sales by Date
# ====================================================

bars = axes[2].bar(
    sales_per_date.index.strftime("%d-%b"),
    sales_per_date.values,
    color="lightcoral",
    edgecolor="black",
    linewidth=2.5
)

axes[2].set_title(
    "3. Sales for Each Specific Date",
    fontsize=18,
    fontweight="bold",
    pad=35
)

axes[2].set_xlabel("Date", fontsize=10, labelpad=15)
axes[2].set_ylabel("Sales (₹)", fontsize=10)

axes[2].grid(axis="y", linestyle="--", alpha=0.6)

axes[2].tick_params(axis="x", rotation=30, labelsize=10)

for bar in bars:
    h = bar.get_height()
    axes[2].text(
        bar.get_x() + bar.get_width()/2,
        h + 700,
        f"{int(h):,}",
        ha="center",
        fontsize=10
    )

# ----------------------------------------------------
# Save the figure
# ----------------------------------------------------
plt.savefig("KFC_Sales_Report.png", dpi=300, bbox_inches="tight")

plt.show()