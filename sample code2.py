import os
import json
import csv
import argparse
from pathlib import Path
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def load_forecast_csv(filepath):
    """Load dairy forecast data: columns = product, week_1, week_2, week_3..."""
    data = {}
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = row.pop('product')
            data[product] = {k: int(v) for k, v in row.items()}
    return data

def build_prompt(product, values):
    return f"""
    You are a dairy supply chain analyst.
    Analyze this forecasted demand data for dairy products and return JSON with 3 keys.

    Product: {product}
    Weekly Forecast in litres/kg: {values}

    Return ONLY valid JSON in this exact format:
    {{
      "farm_manager_summary": "2-3 lines for production/stock decisions. Mention if supply should increase or hold.",
      "trend_view": "State if demand is Rising, Falling, or Stable. Include % change from week_1 to week_3.",
      "alert_view": "Flag if week-to-week change > 20%"
    }}
    """