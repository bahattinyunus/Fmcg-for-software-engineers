import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_fmcg_data(num_days=365, num_products=50, num_stores=10):
    """
    Generates realistic FMCG sales data.
    """
    np.random.seed(42)
    
    # 1. Product Master Data
    categories = ['Beverages', 'Snacks', 'Dairy', 'Personal Care', 'Household']
    products = []
    for i in range(1, num_products + 1):
        cat = np.random.choice(categories)
        base_price = np.random.uniform(5, 50)
        shelf_life = np.random.choice([7, 15, 30, 90, 180, 365]) if cat != 'Household' else 730
        products.append({
            'product_id': f'P{i:03d}',
            'category': cat,
            'base_price': round(base_price, 2),
            'shelf_life_days': shelf_life
        })
    df_products = pd.DataFrame(products)

    # 2. Date Range
    start_date = datetime.now() - timedelta(days=num_days)
    dates = [start_date + timedelta(days=x) for x in range(num_days)]

    # 3. Generate Transactions
    transaction_data = []
    
    for date in dates:
        # Weekly seasonality (higher on weekends)
        is_weekend = date.weekday() >= 5
        daily_traffic = np.random.poisson(200 if is_weekend else 120) * num_stores
        
        for _ in range(daily_traffic):
            store_id = f'S{np.random.randint(1, num_stores+1):02d}'
            product = df_products.sample(1).iloc[0]
            
            # Price fluctuation (simulating promotions)
            is_promo = np.random.random() < 0.15
            price_multiplier = 0.8 if is_promo else 1.0
            price = round(product['base_price'] * price_multiplier, 2)
            
            # Quantity (negative correlation with price usually, but random here mixed with promo)
            qty = np.random.poisson(2 if not is_promo else 4)
            if qty == 0: qty = 1
            
            # Manufacturing date for SKT (Shelf Life) logic
            # Usually produced recently, but some might be old (risk)
            days_since_production = int(np.random.randint(0, int(product['shelf_life_days'] * 0.8)))
            mfg_date = date - timedelta(days=days_since_production)
            expiry_date = mfg_date + timedelta(days=int(product['shelf_life_days']))
            
            transaction_data.append({
                'date': date.strftime('%Y-%m-%d'),
                'store_id': store_id,
                'product_id': product['product_id'],
                'category': product['category'],
                'quantity': qty,
                'unit_price': price,
                'is_promo': is_promo,
                'expiry_date': expiry_date.strftime('%Y-%m-%d')
            })
            
    df_trans = pd.DataFrame(transaction_data)
    
    return df_trans, df_products

if __name__ == "__main__":
    print("Generating synthetic FMCG data...")
    df_sales, df_prods = generate_fmcg_data()
    
    # Save to data folder (ensure it exists)
    import os
    os.makedirs('data', exist_ok=True)
    
    df_sales.to_csv('data/mock_sales_data.csv', index=False)
    df_prods.to_csv('data/product_master.csv', index=False)
    
    print(f"Generated {len(df_sales)} transactions. Saved to data/mock_sales_data.csv")
