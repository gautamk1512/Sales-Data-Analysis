from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Product Descriptions
PRODUCT_DESCRIPTIONS = {
    "Laptop": "A high-performance portable computer suitable for business, education, and entertainment. Known for its versatility and computing power.",
    "Mouse": "An essential input device designed for precision and comfort. Features ergonomic design and responsive tracking.",
    "Keyboard": "A durable and responsive keyboard for efficient typing. Ideal for office work or gaming setups.",
    "Monitor": "High-resolution display screen providing clear and vibrant visuals. essential for desktop computing and dual-screen setups.",
    "Headphones": "Premium audio device offering immersive sound quality. Great for music, calls, and focusing in noisy environments."
}

# Ensure directories exist
for folder in ['static/images', 'static/uploads']:
    if not os.path.exists(folder):
        os.makedirs(folder)

def load_data():
    try:
        df = pd.read_csv('sales_data.csv')
        # Ensure correct data types
        df['Date'] = pd.to_datetime(df['Date'])
        df['Total_Sales'] = df['Quantity_Sold'] * df['Price_per_Unit']
        return df
    except FileNotFoundError:
        return None

@app.route('/')
def index():
    df = load_data()
    if df is None:
        return "Error: sales_data.csv not found."
    
    # Get unique products for the dropdown
    products = df['Product'].unique()
    return render_template('index.html', products=products)

@app.route('/analyze', methods=['POST'])
def analyze():
    product_name = request.form['product']
    
    # Handle Image Upload
    uploaded_image_url = None
    if 'product_image' in request.files:
        file = request.files['product_image']
        if file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            uploaded_image_url = f'static/uploads/{filename}'

    df = load_data()
    
    if df is None:
        return "Error: sales_data.csv not found."

    # Filter data for the selected product
    product_data = df[df['Product'] == product_name]
    
    if product_data.empty:
        return f"No data found for {product_name}"

    # Calculate stats
    total_revenue = product_data['Total_Sales'].sum()
    total_quantity = product_data['Quantity_Sold'].sum()
    average_price = product_data['Price_per_Unit'].mean()
    
    # Get Description
    description = PRODUCT_DESCRIPTIONS.get(product_name, "No description available for this product.")
    
    # Generate Plot
    plt.figure(figsize=(10, 6))
    daily_sales = product_data.groupby('Date')['Total_Sales'].sum()
    daily_sales.plot(kind='line', marker='o', color='purple')
    plt.title(f'Daily Sales Trend for {product_name}')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.tight_layout()
    
    # Save plot
    plot_path = f'static/images/plot_{product_name}.png'
    # Remove old file if exists to ensure update
    if os.path.exists(plot_path):
        os.remove(plot_path)
    plt.savefig(plot_path)
    plt.close()

    return render_template('result.html', 
                           product=product_name, 
                           revenue=total_revenue, 
                           quantity=total_quantity, 
                           avg_price=average_price,
                           description=description,
                           plot_url=plot_path,
                           uploaded_image_url=uploaded_image_url)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
