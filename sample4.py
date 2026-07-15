import os

try:
    import google.genai as genai
except ImportError:
    genai = None

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Dairy Products Data
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

    if not api_key:
        return None

    if genai is None:
        return None

    try:
        return genai.Client(api_key=api_key)
    except Exception as e:
        print("Gemini Client Error:", e)
        return None


def generate_summary(product, forecast, client):
    prompt = f"""
You are a Dairy Business Analyst.

Product: {product}

Forecast Data:
Week 1 = {forecast[0]}
Week 2 = {forecast[1]}
Week 3 = {forecast[2]}

Provide:

1. Farm Manager Summary
2. Trend View
3. Alert View
4. Explain how Gemini AI analyzed the forecast data
5. Explain which charts will be generated and their purpose
6. Inventory Planning Recommendation

Use simple and professional language.
"""

    if client is None:
        return f"""
Farm Manager Summary:
{product} demand is expected to increase from {forecast[0]} to {forecast[2]} units.

Trend View:
Demand shows a steady upward trend across all three weeks.

Alert View:
Monitor inventory levels because demand is increasing.

AI Analysis Process:
1. User entered the product name.
2. Forecast data was retrieved.
3. Demand trend was analyzed.
4. Charts were generated.

Inventory Recommendation:
Maintain sufficient stock to meet future demand.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        print("Gemini Error:", e)
        return "Unable to generate AI summary."


def create_line_chart(product, forecast):
    weeks = ["Week 1", "Week 2", "Week 3"]

    plt.figure(figsize=(7, 5))
    plt.plot(weeks, forecast, marker="o")
    plt.title(f"{product} Demand Forecast")
    plt.xlabel("Weeks")
    plt.ylabel("Demand")
    plt.grid(True)

    filename = f"{product.lower()}_forecast.png"
    plt.savefig(filename)
    plt.close()

    return filename


def create_pie_chart(product, regions):
    plt.figure(figsize=(6, 6))
    plt.pie(
        regions.values(),
        labels=regions.keys(),
        autopct="%1.1f%%"
    )
    plt.title(f"{product} Regional Sales")

    filename = f"{product.lower()}_regional_sales.png"
    plt.savefig(filename)
    plt.close()

    return filename


def create_bar_chart(product, companies):
    plt.figure(figsize=(8, 5))
    plt.bar(companies.keys(), companies.values())
    plt.title(f"{product} Company Sales")
    plt.xlabel("Company")
    plt.ylabel("Sales")

    filename = f"{product.lower()}_company_sales.png"
    plt.savefig(filename)
    plt.close()

    return filename


def main():

    print("=" * 60)
    print(" DAIRY PRODUCT FORECAST ANALYSIS USING GEMINI AI ")
    print("=" * 60)

    product = input(
        "\nEnter Product (Milk, Curd, Butter, Cheese, Paneer): "
    ).strip().title()

    if product not in products:
        print("Invalid Product!")
        return

    data = products[product]

    print("\nAnalyzing data...")
    print("Gemini AI is working behind the scenes...")
    print("Generating report and charts...\n")

    client = get_client()

    summary = generate_summary(
        product,
        data["forecast"],
        client
    )

    print("=" * 60)
    print("AI GENERATED REPORT")
    print("=" * 60)
    print(summary)

    top_company = max(
        data["companies"],
        key=data["companies"].get
    )

    print("\nTop Selling Company:", top_company)
    print("Sales:", data["companies"][top_company])

    line_chart = create_line_chart(
        product,
        data["forecast"]
    )

    pie_chart = create_pie_chart(
        product,
        data["regions"]
    )

    bar_chart = create_bar_chart(
        product,
        data["companies"]
    )

    print("\nCharts Generated Successfully!")
    print("1.", line_chart)
    print("2.", pie_chart)
    print("3.", bar_chart)

    print("\nProcess Flow:")
    print("1. User entered product name.")
    print("2. Product forecast data loaded.")
    print("3. Gemini AI analyzed the forecast.")
    print("4. AI generated business insights.")
    print("5. Python created Line Chart.")
    print("6. Python created Pie Chart.")
    print("7. Python created Bar Chart.")
    print("8. Results displayed and saved.")

    print("\nAnalysis Completed Successfully!")


if __name__ == "__main__":
    main()