from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Sample KFC sales data for the API
sales_data = {
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

sales_df = pd.DataFrame(sales_data)
sales_df["Date"] = pd.to_datetime(sales_df["Date"])

@app.route("/sales", methods=["GET"])
def get_sales():
    """Return all sales records."""
    return jsonify(sales_df.to_dict(orient="records"))

@app.route("/sales/summary", methods=["GET"])
def get_sales_summary():
    """Return total sales summary by branch and weekday."""
    summary = {
        "total_sales_by_branch": sales_df.groupby("Branch")["Sales"].sum().to_dict(),
        "total_sales_by_weekday": sales_df.assign(Weekday=sales_df["Date"].dt.day_name())
            .groupby("Weekday")["Sales"].sum().to_dict()
    }
    return jsonify(summary)

@app.route("/sales/date", methods=["GET"])
def get_sales_by_date():
    """Return sales for a specific date passed as a query parameter."""
    date_str = request.args.get("date")
    if not date_str:
        return jsonify({"error": "Please provide a date query parameter in YYYY-MM-DD format."}), 400

    try:
        query_date = pd.to_datetime(date_str)
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    filtered = sales_df[sales_df["Date"] == query_date]
    return jsonify(filtered.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
