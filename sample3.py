import os

try:
    import google.genai as genai
except ImportError:
    genai = None

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


products = {
    "Milk": {
        "forecast": [1200, 1350, 1500],
        "regions": {"North": 350, "South": 400, "East": 250, "West": 200},
        "companies": {"Amul": 1500, "Aavin": 1200, "Mother Dairy": 1800, "Heritage": 100},
    },
    "Curd": {
        "forecast": [800, 900, 1000],
        "regions": {"North": 200, "South": 400, "East": 150, "West": 250},
        "companies": {"Amul": 900, "Aavin": 1400, "Mother Dairy": 1100, "Heritage": 850},
    },
    "Butter": {
        "forecast": [600, 750, 850],
        "regions": {"North": 250, "South": 300, "East": 150, "West": 200},
        "companies": {"Amul": 1700, "Aavin": 800, "Mother Dairy": 1200, "Heritage": 700},
    },
    "Cheese": {
        "forecast": [500, 650, 800],
        "regions": {"North": 200, "South": 250, "East": 150, "West": 300},
        "companies": {"Amul": 1600, "Aavin": 900, "Mother Dairy": 1400, "Heritage": 750},
    },
    "Paneer": {
        "forecast": [700, 850, 950],
        "regions": {"North": 250, "South": 350, "East": 150, "West": 250},
        "companies": {"Amul": 1300, "Aavin": 1600, "Mother Dairy": 1100, "Heritage": 900},
    },
}


def get_client():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key or api_key == "YOUR_GEMINI_API_KEY":
        return None
    if genai is None:
        return None

    try:
        return genai.Client(api_key=api_key)
    except Exception as error:
        print(f"Gemini client initialization failed: {error}")
        return None


def generate_summary(product, forecast, client):
    if client is None:
        return (
            f"{product} demand is expected to increase from {forecast[0]} to {forecast[-1]} over the next 3 weeks. "
            "Farm managers should monitor supply closely and plan inventory accordingly."
        )

    prompt = f"""
    Product: {product}
    Weekly Forecast:
    Week 1 = {forecast[0]}
    Week 2 = {forecast[1]}
    Week 3 = {forecast[2]}
    Give:
    1. Farm Manager Summary
    2. Trend View
    3. Alert View
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
    except Exception as error:
        print(f"Gemini request failed: {error}")
        return (
            f"{product} demand is expected to increase from {forecast[0]} to {forecast[-1]} over the next 3 weeks. "
            "Farm managers should monitor supply closely and plan inventory accordingly."
        )


def save_plot(filename, plot_func):
    fig = plot_func()
    fig.savefig(filename, dpi=150)
    plt.close(fig)


def main():
    product = input("Enter Dairy Product: ").strip().title() or "Milk"

    if product not in products:
        print(
            f"Product '{product}' not found! Please try again with a valid product like Milk, Curd, Butter, Cheese, or Paneer."
        )
        return

    data = products[product]
    client = get_client()
    summary = generate_summary(product, data["forecast"], client)

    print("\n" + "=" * 50)
    print("PRODUCT:", product)
    print("=" * 50)
    print(summary)

    top_company = max(data["companies"], key=data["companies"].get)
    print("\nTop Selling Company:", top_company)
    print("Sales:", data["companies"][top_company])

    weeks = ["Week 1", "Week 2", "Week 3"]

    line_fig = plt.figure(figsize=(7, 5))
    plt.plot(weeks, data["forecast"], marker="o")
    plt.title(f"{product} Demand Forecast")
    plt.xlabel("Weeks")
    plt.ylabel("Demand")
    plt.grid(True)
    line_fig.savefig(f"{product.lower()}_forecast.png", dpi=150)
    plt.close(line_fig)

    pie_fig = plt.figure(figsize=(6, 6))
    plt.pie(
        data["regions"].values(),
        labels=data["regions"].keys(),
        autopct="%1.1f%%",
    )
    plt.title(f"{product} Regional Sales")
    pie_fig.savefig(f"{product.lower()}_regional_sales.png", dpi=150)
    plt.close(pie_fig)

    bar_fig = plt.figure(figsize=(7, 5))
    plt.bar(data["companies"].keys(), data["companies"].values())
    plt.title(f"{product} Company Sales")
    plt.xlabel("Company")
    plt.ylabel("Sales")
    bar_fig.savefig(f"{product.lower()}_company_sales.png", dpi=150)
    plt.close(bar_fig)

    print("\nCharts saved as image files in the current folder.")


if __name__ == "__main__":
    main()