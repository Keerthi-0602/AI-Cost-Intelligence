import pandas as pd

df = pd.read_csv("data.csv")

duplicates = df[df.duplicated(subset=["vendor", "amount", "date"], keep=False)]

print("Duplicate Invoices Found:")
print(duplicates)

total_loss = duplicates["amount"].sum()
print("Total Potential Loss:", total_loss)

print("Suggested Action: Cancel duplicate invoice")