import pandas as pd, matplotlib.pyplot as plt
df = pd.read_csv("trades_with_features.csv")
plt.figure(); plt.plot(df['mid_price'][:200]); plt.title("Price Line"); plt.savefig("price_line.png")
plt.figure(); plt.hist(df['spread'], bins=30); plt.title("Spread"); plt.savefig("spread.png")
plt.figure(); df['side'].value_counts().plot(kind='bar'); plt.title("Buy vs Sell"); plt.savefig("buy_sell.png")
print("GRAPHS DONE! 3 images saved")