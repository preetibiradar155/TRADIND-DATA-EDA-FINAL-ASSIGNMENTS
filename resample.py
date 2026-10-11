import pandas as pd
df = pd.read_csv("trades_with_features.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'], format='mixed')
df.set_index('timestamp', inplace=True)

ohlcv = df['price'].resample('1min').ohlc()
ohlcv['volume'] = df['quantity'].resample('1min').sum()
ohlcv = ohlcv.dropna()

ohlcv.to_csv("ohlcv_1min.csv")
print("OHLCV DONE! - ohlcv_1min.csv saved")
print(ohlcv.head())