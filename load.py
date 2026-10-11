import pandas as pd

df = pd.read_csv("trades_orderbook_STUDENT_dirty.csv")

print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\n--- Head ---")
print(df.head())
print("\n--- Info ---")
df.info()