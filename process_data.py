import pandas as pd
import glob
import os

DATA_DIR = './data'
OUTPUT_FILE = 'formatted_data.csv'

def format_sales_data():
    """
    Reads daily sales CSV files, filters for Pink Morsels, 
    calculates total sales, and outputs a single formatted CSV.
    """
    print("Locating CSV files...")
    csv_files = glob.glob(os.path.join(DATA_DIR, "*.csv"))
    
    if not csv_files:
        print(f"Error: No CSV files found in the '{DATA_DIR}' directory. Please ensure you are in the correct folder.")
        return

    dataframes = []
    for file in csv_files:
        df = pd.read_csv(file)
        dataframes.append(df)
        
    combined_df = pd.concat(dataframes, ignore_index=True)
    print(f"Combined {len(csv_files)} files successfully.")

    pink_morsel_df = combined_df[combined_df['product'].str.lower() == 'pink morsel'].copy()
    
    if pink_morsel_df['price'].dtype == 'O':
        pink_morsel_df['price'] = pink_morsel_df['price'].str.replace('$', '', regex=False).astype(float)
        
    pink_morsel_df['sales'] = pink_morsel_df['quantity'] * pink_morsel_df['price']
    
    final_df = pink_morsel_df[['sales', 'date', 'region']]
    final_df = final_df.rename(columns={
        'sales': 'Sales',
        'date': 'Date',
        'region': 'Region'
    })

    final_df.to_csv(OUTPUT_FILE, index=False)
    print(f"Success! The formatted data has been saved to '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    format_sales_data()