import pandas as pd
import quandl

df = quandl.get('WSE/TBULL')
df = df[['Open','High','Low','Close','Volume']]
df['HL_PCT'] = (df['High'] - df['Close']) / df['Close'] *100
df['PCT_change'] = (df['Close'] - df['Open']) / df['Open'] *100

df = df[['Close','HL_PCT','PCT_change','Volume']]

print(df.head())
