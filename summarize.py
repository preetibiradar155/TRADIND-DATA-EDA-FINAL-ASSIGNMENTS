import pandas as pd
df = pd.read_csv("trades_orderbook_STUDENT_dirty.csv")
print(df.describe())
print(df['side'].value_counts())