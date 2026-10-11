import pandas as pd
df = pd.read_csv("trades_cleaned.csv")
df['spread'] = df['ask_price_1'] - df['bid_price_1']
df['mid_price'] = (df['ask_price_1'] + df['bid_price_1'])/2
print("Features added")
print(df[['spread','mid_price']].head())
df.to_csv("trades_with_features.csv", index=False)