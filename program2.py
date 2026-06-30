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

# Create DataFrame and convert Date column safely
sales_df = pd.DataFrame(sales_data)
sales_df["Date"] = pd.to_datetime(sales_df["Date"])

@app.route("/sales", methods=["GET"])
def get_sales():
    """Return all sales records."""
    df_copy = sales_df.copy()
    df_copy["Date"] = df_copy["Date"].dt.strftime("%Y-%m-%d")
    return jsonify(df_copy.to_dict(orient="records"))

@app.route("/sales/summary", methods=["GET"])
def get_sales_summary():
    """Return total sales summary by branch and weekday."""
    total_by_branch = {k: int(v) for k, v in sales_df.groupby("Branch")["Sales"].sum().to_dict().items()}
    
    weekday_df = sales_df.assign(Weekday=sales_df["Date"].dt.day_name())
    total_by_weekday = {k: int(v) for k, v in weekday_df.groupby("Weekday")["Sales"].sum().to_dict().items()}
    
    summary = {
        "total_sales_by_branch": total_by_branch,
        "total_sales_by_weekday": total_by_weekday
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
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400
    filtered = sales_df[sales_df["Date"] == query_date].copy()
    filtered["Date"] = filtered["Date"].dt.strftime("%Y-%m-%d")
    return jsonify(filtered.to_dict(orient="records"))

# Global error handler
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": "An unexpected server error occurred.", "details": str(e)}), 500

if __name__ == "__main__":
    # Changed port to 8081 to avoid the "Address already in use" conflict
    app.run(debug=False, port=8081)