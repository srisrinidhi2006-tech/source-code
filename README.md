 # Retail Analytics and AI Reporting Projects

## 📌 Overview
This repository contains a collection of Python projects focused on **retail sales analysis**, **data quality validation**, **reporting automation**, and **AI-powered text generation**. These projects demonstrate how to effectively leverage Python for driving business analytics and technical reporting.


## 🚀 Projects Included

### 1. Daily Sales Analysis and Visualization
* **Core Functions:**
  * Analyzes daily sales data from a retail branch.
  * Converts date fields dynamically into standard `datetime` formats.
  * Generates visual trend reports using Matplotlib.
* **Key Visualizations Displayed:**
  * Daily Sales Trend lines
  * Sales distribution by Day of the Week
  * Detailed sales breakdown by Specific Dates
* **🛠️ Technologies Used:** `Python` | `Pandas` | `Matplotlib`

### 2. Weekly Sales Report Generator
* **Core Functions:**
  * Processes raw retail sales data streams.
  * Calculates exact weekly sales aggregates.
  * Groups sales periods accurately by **ISO week numbers**.
  * Automatically exports the final report directly to an Excel spreadsheet.
* **✨ Features:** Automated weekly sales math & clean Excel file production.
* **🛠️ Technologies Used:** `Python` | `Pandas` | `OpenPyXL`

### 3. Menu Data Quality Validation
* **Core Functions:**
  * Performs strict data quality checks on menu and product datasets.
* **Identifies Critical Anomalies:**
  * Missing product descriptions
  * Invalid or corrupt pricing entries
  * Cost structures greater than selling prices (negative margins)
  * Missing product categories
  * Duplicate unique Product IDs
* **🎯 Purpose:** Ensures product master data is 100% accurate before it reaches business reporting dashboards.

### 4. AI API Integration Demo
* **Core Functions:**
  * Demonstrates how to connect standalone Python applications with cloud-hosted AI APIs.
  * Packages and sends prompts to receive structured AI-generated responses.
  * Includes robust structural error-handling mechanisms for unexpected API failures.
* **📚 Topics Covered:** `API Requests` | `JSON Processing` | `Response Handling`

### 5. Dataset Summary and AI Narrative Generation
* **Core Functions:**
  * Analyzes complex product sales data tables.
  * Calculates vital key performance statistics:
    * **Total Sales** & **Total Revenue**
    * **Average Sales** metrics
    * **Best Selling Product** identification
    * **Highest Rated Product** extraction
  * Transforms raw numbers into plain-English business summaries.
* **💼 Use Case:** Converts cold numerical data into management-friendly, readable insights.

### 6. Generic Report Formatter
* **Core Functions:**
  * Creates clean, structured, and aligned text reports out of raw Python dictionaries.
* **Supported Elements:**
  * Nested dictionaries
  * Object lists
  * Boolean value transformations (e.g., True ➔ Yes)
  * Custom centered report titles
* **🎯 Purpose:** Outlines standardized textual reporting layouts for business-terminal applications.

---

## 💻 Requirements

Install the necessary backend dependencies via terminal:

```bash
pip install pandas matplotlib openpyxl

🛠️ How to Run
Clone the repository:

Bash
git clone <your-github-repository-link>
cd <repository-folder>
Run any project file:

Bash
python filename.py

🎓 Learning Outcomes
*Data Analysis using Pandas
*Data Visualization via Matplotlib
*Report Automation frameworks
*Data Quality Validation & sanitization
*Automated Excel Exporting routines
*External API Integration architectures
*AI-Assisted Reporting workflows

### 🚀 Quick-Start Guide: Create, Save, and Run a Program in VS Code

1. **Create & Open a Folder:** Create a folder on your computer (e.g., on your Desktop or D: drive). Open VS Code, go to **File > Open Folder...**, select your folder, and click **Select Folder**.
2. **Create Your Python File:** Click the **New File** icon `+` in the left sidebar. Name your file ending with `.py` (e.g., `main.py`). Avoid using spaces in the filename.
3. **Write & Save Code:** Paste your Python code into the empty editor window and press **Ctrl + S** (or **Cmd + S** on Mac) to save the file.
4. **Install Dependencies (If Needed):** Open the integrated terminal (**Terminal > New Terminal**) and run any required pip commands for your script (e.g., `pip install google-generativeai`).
5. **Run the Program:** Click the **Play button** (triangle icon) in the top-right corner of the editor interface, or type `python main.py` in your terminal and hit Enter.
