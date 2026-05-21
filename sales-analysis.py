import pandas as pd
import matplotlib.pyplot as plt

# Load the sales data from a CSV file
sales_data = pd.read_csv("sales-data.csv")

# Calculate the percentage growth in sales
sales_data["Growth"]= sales_data["Sales"].pct_change() * 100

plt.figure(figsize=(10, 10))
# Plot the total sales
plt.subplot(2,1,1)
plt.plot(sales_data["Month"], sales_data["Sales"])
plt.title("Total sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=90)

# Plot the growth in sales
plt.subplot(2,1,2)
plt.plot(sales_data["Month"], sales_data["Growth"])
plt.title("Growth in sales")
plt.xlabel("Month")
plt.ylabel("Growth (%)")
plt.xticks(rotation=90)
plt.savefig("sales_analysis.png")