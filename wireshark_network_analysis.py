import pandas as pd

df = pd.read_csv("test.csv", names=["Source", "Destination", "Protocol", "Info"])
print(df.head())