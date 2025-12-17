# Sales Data Analysis Project (DS7E-741: PROJECT-I)

This project analyzes sales data using Python to extract meaningful insights and visualize trends. It demonstrates data handling with `pandas` and visualization with `matplotlib`.

## Prerequisites

- Python installed on your system.

## Installation

1.  **Open your terminal/command prompt.**
2.  **Install the required libraries** using the following command:

    ```bash
    pip install pandas matplotlib
    ```

## How to Run the Project

### Option 1: Command Line Analysis
1.  Ensure `sales_data.csv` is in the same folder as the script.
2.  Run the script using the command:

    ```bash
    python sales_analysis.py
    ```

### Option 2: Web Application (Flask)
1.  Run the Flask app:
    ```bash
    python app.py
    ```
2.  Open your browser and go to `http://127.0.0.1:5000`.
3.  Select a product from the dropdown and click **Analyze Product**.
4.  View the detailed statistics and sales trend chart for that product.

### Option 3: Running in Google Colab (Step-by-Step Guide)
If you want to run this project in the cloud (Google Colab), follow these steps carefully:

**Step 1: Open Google Colab**
1.  Go to [colab.research.google.com](https://colab.research.google.com/).
2.  Click on **"New Notebook"** in the bottom right corner of the pop-up.

**Step 2: Upload the Data File**
1.  On the left side of the screen, you will see a **Folder icon** (Files). Click it.
2.  Click the **Upload icon** (an arrow pointing up) at the top of the Files pane.
3.  Select the `sales_data.csv` file from your computer and upload it.
    *   *Note: Google Colab might warn you that files are recycled when the runtime disconnects. Just click OK.*

**Step 3: Write and Run the Code**
1.  Click on the first code cell (the box where you can type).
2.  Copy the code below and paste it into the cell:

    ```python
    import pandas as pd
    import matplotlib.pyplot as plt

    # 1. Read the data
    try:
        df = pd.read_csv('sales_data.csv')
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("Error: Please upload sales_data.csv first!")

    # 2. Calculate Total Sales
    df['Total_Sales'] = df['Quantity_Sold'] * df['Price_per_Unit']

    # 3. Print Analysis
    total_sales = df['Total_Sales'].sum()
    best_selling_product = df.groupby('Product')['Total_Sales'].sum().idxmax()
    average_daily_sales = df.groupby('Date')['Total_Sales'].sum().mean()

    print("-" * 30)
    print("ANALYSIS RESULTS")
    print("-" * 30)
    print(f"Total Revenue: {total_sales}")
    print(f"Best Selling Product: {best_selling_product}")
    print(f"Average Daily Sales: {average_daily_sales:.2f}")

    # 4. Show Charts
    # Product Sales
    plt.figure(figsize=(10, 6))
    df.groupby('Product')['Total_Sales'].sum().plot(kind='bar', color='skyblue')
    plt.title('Product-wise Total Sales')
    plt.show()

    # Daily Trend
    plt.figure(figsize=(10, 6))
    df.groupby('Date')['Total_Sales'].sum().plot(kind='line', marker='o', color='green')
    plt.title('Daily Sales Trend')
    plt.show()
    ```

3.  Click the **Play button** (triangle icon) on the left side of the cell to run the code.

**Step 4: View Results**
- You will see the **Analysis Results** (Total Revenue, etc.) printed below the cell.
- You will see the **Charts** displayed directly on the page.

**Files you need:**
- `sales_data.csv` (You must upload this)

## Project Structure

- `sales_data.csv`: The dataset containing sales records.
- `sales_analysis.py`: Command-line analysis script.
- `app.py`: Flask web application.
- `templates/`: HTML files for the web app (`index.html`, `result.html`).
- `static/`: Stores generated images/plots for the web app.
- `plots/`: Directory where charts from the CLI script are saved.

## Code Breakdown

Here is an explanation of what the `sales_analysis.py` code does:

### 1. Importing Libraries
```python
import pandas as pd
import matplotlib.pyplot as plt
import os
```
- `pandas`: Used for reading the CSV file and manipulating the data (tables).
- `matplotlib.pyplot`: Used for creating charts and graphs.
- `os`: Used to check and create directories (folders).

### 2. Reading the Data
```python
df = pd.read_csv('sales_data.csv')
```
- Reads the data from `sales_data.csv` into a pandas DataFrame (`df`), which is like a programmable Excel sheet.

### 3. Calculating Total Sales
```python
df['Total_Sales'] = df['Quantity_Sold'] * df['Price_per_Unit']
```
- Creates a new column `Total_Sales` by multiplying the quantity sold by the price per unit for each row.

### 4. Data Analysis
```python
total_sales = df['Total_Sales'].sum()
best_selling_product = df.groupby('Product')['Total_Sales'].sum().idxmax()
average_daily_sales = df.groupby('Date')['Total_Sales'].sum().mean()
```
- **Total Sales**: Sums up the entire `Total_Sales` column.
- **Best Selling Product**: Groups data by 'Product', sums their sales, and finds the product with the maximum value.
- **Average Daily Sales**: Groups data by 'Date', sums daily sales, and then calculates the average.

### 5. Visualization (Charts)

**Product-wise Sales (Bar Chart):**
```python
product_sales.plot(kind='bar', color='skyblue')
plt.savefig('plots/product_sales.png')
```
- Creates a bar chart showing how much revenue each product generated and saves it as an image.

**Daily Sales Trend (Line Chart):**
```python
daily_sales.plot(kind='line', marker='o', color='green')
plt.savefig('plots/daily_sales_trend.png')
```
- Creates a line chart showing how sales changed day by day and saves it as an image.
