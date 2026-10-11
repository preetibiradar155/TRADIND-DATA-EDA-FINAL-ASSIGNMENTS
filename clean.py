import pandas as pd
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("trades_orderbook_STUDENT_dirty.csv")

# timestamp fix - warning hatane ke liye mixed format
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce', format='mixed')

# price fix
df['price'] = df['price'].astype(str).str.replace(r'[^0-9.]', '', regex=True)
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['price'] = df['price'].fillna(df['price'].median())

# side fix
df['side'] = df['side'].astype(str).str.lower().str.strip()
df['side'] = df['side'].replace({'nan': None, 'none': None})
df['side'] = df['side'].ffill()

# quantity fix
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['quantity'] = df['quantity'].fillna(df['quantity'].median())

# ask_price fix
df['ask_price_1'] = df['ask_price_1'].fillna(df['ask_price_1'].median())

print("CLEANING DONE!")
print(f"Shape after cleaning: {df.shape}")
print(df.info())
print("\n--- First 5 rows ---")
print(df.head())

df.to_csv("trades_cleaned.csv", index=False)
print("\nSaved as trades_cleaned.csv")