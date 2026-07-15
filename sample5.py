import os
import matplotlib.pyplot as plt

try:
    from google import genai
except ImportError:
    genai = None

# ------------------ Dataset ------------------

products = {
    "Milk":{"forecast":[1200,1350,1500],"regions":{"North":350,"South":400,"East":250,"West":200},"companies":{"Amul":1500,"Aavin":1200,"Mother Dairy":1800,"Heritage":1000}},
    "Curd":{"forecast":[800,900,1000],"regions":{"North":200,"South":400,"East":150,"West":250},"companies":{"Amul":900,"Aavin":1400,"Mother Dairy":1100,"Heritage":850}},
    "Butter":{"forecast":[600,700,850],"regions":{"North":250,"South":300,"East":150,"West":200},"companies":{"Amul":1700,"Aavin":800,"Mother Dairy":1200,"Heritage":700}},
    "Cheese":{"forecast":[500,650,800],"regions":{"North":200,"South":250,"East":150,"West":300},"companies":{"Amul":1600,"Aavin":900,"Mother Dairy":1400,"Heritage":750}},
    "Paneer":{"forecast":[700,850,950],"regions":{"North":250,"South":350,"East":150,"West":250},"companies":{"Amul":1300,"Aavin":1600,"Mother Dairy":1100,"Heritage":900}},
    "Ghee":{"forecast":[900,1050,1200],"regions":{"North":320,"South":280,"East":180,"West":220},"companies":{"Amul":2000,"Aavin":900,"Mother Dairy":1500,"Heritage":850}},
    "Ice Cream":{"forecast":[1000,1200,1500],"regions":{"North":300,"South":450,"East":200,"West":350},"companies":{"Amul":1900,"Aavin":1300,"Mother Dairy":1700,"Heritage":1000}},
    "Flavoured Milk":{"forecast":[650,800,950],"regions":{"North":180,"South":320,"East":170,"West":280},"companies":{"Amul":1100,"Aavin":1250,"Mother Dairy":1350,"Heritage":700}},
    "Yogurt":{"forecast":[750,900,1050],"regions":{"North":220,"South":330,"East":180,"West":270},"companies":{"Amul":1400,"Aavin":1200,"Mother Dairy":1500,"Heritage":850}},
    "Cream":{"forecast":[550,650,780],"regions":{"North":170,"South":250,"East":130,"West":200},"companies":{"Amul":1350,"Aavin":900,"Mother Dairy":1250,"Heritage":650}}
}

# ------------------ Gemini ------------------

def get_client():
    if genai is None:
        return None
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        return None
    return genai.Client(api_key=key)

def ai_report(product, forecast, client):
    prompt = f"""
Product : {product}

Forecast:
Week1={forecast[0]}
Week2={forecast[1]}
Week3={forecast[2]}

Give:
1. Farm Manager Summary
2. Trend
3. Inventory Recommendation
4. Explain that the dataset comes from Python.
5. Explain that Gemini AI analyzed only the data.
6. Explain that Python Matplotlib created the charts.
"""

    if client is None:
        return f"""
Farm Manager Summary:
Demand for {product} is increasing.

Trend:
{forecast[0]} → {forecast[1]} → {forecast[2]}

Inventory Recommendation:
Increase stock gradually.

Dataset Source:
Python dictionary.

AI Output:
Gemini API not available.

Charts:
Generated using Python Matplotlib.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except:
        return "Gemini AI could not generate the report."

# ------------------ Charts ------------------

def charts(product,data):

    plt.figure(figsize=(5,3))
    plt.plot(["W1","W2","W3"],data["forecast"],marker="o")
    plt.title(product+" Forecast")
    plt.savefig(product+"_forecast.png")
    plt.close()

    plt.figure(figsize=(4,4))
    plt.pie(data["regions"].values(),
            labels=data["regions"].keys(),
            autopct="%1.1f%%")
    plt.title(product+" Regions")
    plt.savefig(product+"_regions.png")
    plt.close()

    plt.figure(figsize=(6,3))
    plt.bar(data["companies"].keys(),
            data["companies"].values())
    plt.title(product+" Companies")
    plt.savefig(product+"_companies.png")
    plt.close()

# ------------------ Main ------------------

print("="*60)
print("DAIRY FORECAST ANALYSIS USING GEMINI AI")
print("="*60)

print("\nAvailable Products\n")

for p in products:
    print("-",p)

product=input("\nEnter Product : ").title()

if product not in products:
    print("Invalid Product")
    exit()

data=products[product]

client=get_client()

print("\nAnalyzing Forecast using Gemini AI...\n")

print(ai_report(product,data["forecast"],client))

top=max(data["companies"],key=data["companies"].get)

print("\nTop Selling Company :",top)
print("Sales :",data["companies"][top])

charts(product,data)

print("\nImages Saved")
print("1.",product+"_forecast.png")
print("2.",product+"_regions.png")
print("3.",product+"_companies.png")

print("\nPROCESS FLOW")
print("1. User selected a dairy product.")
print("2. Python loaded the sample dataset.")
print("3. Forecast values were sent to Gemini AI.")
print("4. Gemini AI analyzed the forecast and generated the report.")
print("5. Python Matplotlib generated the Line, Pie and Bar charts.")
print("6. Images were saved as PNG files.")

print("\nDATA SOURCE")
print("• Dataset : Sample data stored inside Python dictionary.")
print("• AI Report : Generated by Gemini AI.")
print("• Charts : Generated by Python Matplotlib using the same dataset.")
print("• Gemini AI analyzes the data but does not generate the chart images.")