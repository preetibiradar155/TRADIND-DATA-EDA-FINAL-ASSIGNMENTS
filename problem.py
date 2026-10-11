import pandas as pd
df = pd.read_csv("trades_orderbook_STUDENT_dirty.csv")
print("Missing values:")
print(df.isnull().sum())
print(f"\nDuplicates: {df.duplicated().sum()}")