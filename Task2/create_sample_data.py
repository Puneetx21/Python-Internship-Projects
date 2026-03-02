import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate sample sales data
np.random.seed(42)
dates = pd.date_range(start='2026-01-01', end='2026-02-27', freq='D')
products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones']
regions = ['North', 'South', 'East', 'West']

data = []
for date in dates:
    for _ in range(np.random.randint(5, 15)):
        data.append({
            'Date': date.strftime('%Y-%m-%d'),
            'Product': np.random.choice(products),
            'Region': np.random.choice(regions),
            'Quantity': np.random.randint(1, 20),
            'Price': np.random.choice([29.99, 49.99, 79.99, 299.99, 59.99]),
            'Customer_Satisfaction': np.random.randint(1, 6)
        })

df = pd.DataFrame(data)
df['Revenue'] = df['Quantity'] * df['Price']
df.to_csv('sales_data.csv', index=False)

print(" Sample data created: sales_data.csv")
print(f"Total records: {len(df)}")
print("\nPreview:")
print(df.head())
