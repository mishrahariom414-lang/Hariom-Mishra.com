# सिंपल डाटा एनालिसिस - किराना दुकान की 6 महीने की बिक्री
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# 1. डाटा बनाना
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [20000, 22000, 25000, 21000, 28000, 30000],  # रुपये में
}
df = pd.DataFrame(data)
print(df)

# 2. सवालों के जवाब निकालना
total = df["Sales"].sum()
average = df["Sales"].mean()
best = df.loc[df["Sales"].idxmax()]
growth = (df["Sales"].iloc[-1] - df["Sales"].iloc[0]) / df["Sales"].iloc[0] * 100

print("\nकुल बिक्री      :", total)
print("औसत बिक्री      :", round(average, 2))
print("सबसे अच्छा महीना :", best["Month"], "-", best["Sales"])
print("Jan से Jun ग्रोथ :", round(growth, 1), "%")

# 3. चार्ट बनाना
plt.figure(figsize=(8, 4.5))
plt.bar(df["Month"], df["Sales"], color="#2E86AB")
plt.axhline(average, color="red", linestyle="--", label=f"Average = {average:.0f}")
for i, v in enumerate(df["Sales"]):
    plt.text(i, v + 400, str(v), ha="center")
plt.title("Monthly Sales of Grocery Shop (Jan-Jun)")
plt.xlabel("Month")
plt.ylabel("Sales (Rs.)")
plt.legend()
plt.tight_layout()
plt.savefig("sales_chart.png", dpi=150)
print("\nचार्ट सेव हो गया: sales_chart.png")
