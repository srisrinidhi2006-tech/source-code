import os
import json
import csv
import argparse
from pathlib import Path
import google.generativeai as genai

# Ensure the API key is configured
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Error: GEMINI_API_KEY environment variable not set.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def load_forecast_csv(filepath):
    """Load dairy forecast data: columns = product, week_1, week_2, week_3..."""
    data = {}
    if not Path(filepath).exists():
        raise FileNotFoundError(f"The file {filepath} does not exist.")
        
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = row.pop('product')
            # Safely convert values to integers, skipping any empty columns
            data[product] = {k: int(v) for k, v in row.items() if v.strip()}
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

def main():
    # Set up command-line arguments so you can run it via VS Code terminal
    parser = argparse.ArgumentParser(description="Analyze dairy forecast using Gemini API.")
    parser.add_argument("csv_file", type=str, help="Path to the dairy forecast CSV file")
    args = parser.parse_args()

    try:
        # 1. Load data
        print(f"Loading data from {args.csv_file}...")
        forecast_data = load_forecast_csv(args.csv_file)
        
        # 2. Process each product through Gemini
        for product, values in forecast_data.items():
            print(f"\nAnalyzing {product}...")
            prompt = build_prompt(product, values)
            
            # Enforce structured JSON generation using generation_config
            response = model.generate_content(
                prompt,
                generation_config={"response_mime_type": "application/json"}
            )
            
            # 3. Print the formatted result
            try:
                result_json = json.loads(response.text)
                print(json.dumps(result_json, indent=2))
            except json.JSONDecodeError:
                print("Failed to parse response as JSON. Raw response:")
                print(response.text)
                
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
