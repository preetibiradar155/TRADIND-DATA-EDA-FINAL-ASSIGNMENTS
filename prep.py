import pandas as pd
df = pd.read_csv("trades_with_features.csv")
df['target'] = (df['mid_price'].shift(-5) > df['mid_price']).astype(int)
split = int(len(df)*0.7)
train, test = df.iloc[:split], df.iloc[split:]
train.to_csv("train.csv", index=False)
test.to_csv("test.csv", index=False)
print(f"MODEL PREP DONE! Train:{len(train)} Test:{len(test)}")