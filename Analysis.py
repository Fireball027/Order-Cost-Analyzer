import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def main():
    # Load Dataset
    print("\nLoading dataset...")
    df = pd.read_csv("food delivery costs.csv")

    # Data Preprocessing
    print("Preprocessing datetime columns...")
    df["Order Date and Time"] = pd.to_datetime(df["Order Date and Time"])
    df["Delivery Date and Time"] = pd.to_datetime(df["Delivery Date and Time"])

    print("Cleaning 'Discounts and Offers' column...")

    # Extract first part of discount value (e.g., "10 % OFF" -> "10")
    def extract(value):
        return str(value).split(" ")[0]

    # Remove % sign and convert to float
    def removep(value):
        if "%" in value:
            return float(value.replace("%", ""))
        else:
            return float(value)

    df["Discounts and Offers"] = df["Discounts and Offers"].apply(extract).apply(removep)

    # If discount <= 15, treat it as percentage of order value
    df.loc[df["Discounts and Offers"] <= 15, "Discounts and Offers"] = \
        (df["Discounts and Offers"] / 100) * df["Order Value"]

    # Fill missing discounts with 0
    df["Discounts and Offers"] = df["Discounts and Offers"].fillna(0)

    # Feature Engineering
    print("Creating new features (Delivery Duration, Costs, Profit, Time-based features)...")
    df["Delivery Duration (mins)"] = (df["Delivery Date and Time"] - df["Order Date and Time"]).dt.total_seconds() / 60
    df["Costs"] = df["Delivery Fee"] + df["Discounts and Offers"] + df["Payment Processing Fee"]
    df["Profit"] = df["Commission Fee"] - df["Costs"]
    df["Day of Week"] = df["Order Date and Time"].dt.day_name()
    df["Hour of Day"] = df["Order Date and Time"].dt.hour

    # Summary Statistics
    print("\nPROFIT SUMMARY")
    print("Total Profit:", df["Profit"].sum())
    print("\nProfit stats:\n", df["Profit"].describe())

    print("\nTop 5 Profitable Orders:\n", df.nlargest(5, "Profit")[["Order Value", "Profit"]])
    print("\nBottom 5 Loss Orders:\n", df.nsmallest(5, "Profit")[["Order Value", "Profit"]])

    # Visualizations
    print("\nGenerating visualizations...")
    sns.set(style="whitegrid")

    # 1. Cost Distribution Pie Chart
    cost_dist = df[["Delivery Fee", "Payment Processing Fee", "Discounts and Offers"]].sum()
    plt.figure(figsize=(6, 6))
    plt.pie(cost_dist, labels=cost_dist.index, autopct="%1.1f%%", startangle=90, colors=sns.color_palette("pastel"))
    plt.title("Cost Distribution")
    plt.show()

    # 2. Commission vs Costs vs Profit (Bar Chart)
    abc = df[["Commission Fee", "Costs", "Profit"]].sum()
    plt.figure(figsize=(6, 5))
    sns.barplot(x=abc.index, y=abc.values, palette="Set2")
    plt.title("Commission vs Costs vs Profit")
    plt.ylabel("Amount")
    plt.show()

    # 3. Profit Distribution (Histogram + KDE)
    plt.figure(figsize=(7, 5))
    sns.histplot(df["Profit"], bins=25, kde=True, color="skyblue")
    plt.title("Profit Distribution")
    plt.xlabel("Profit")
    plt.ylabel("Frequency")
    plt.show()

    # 4. Profit by Day of Week (Boxplot)
    plt.figure(figsize=(7, 5))
    sns.boxplot(x="Day of Week", y="Profit", data=df, palette="muted")
    plt.title("Profit by Day of Week")
    plt.xticks(rotation=45)
    plt.show()

    # 5. Profit by Hour of Day (Line Plot)
    plt.figure(figsize=(7, 5))
    sns.lineplot(x="Hour of Day", y="Profit", data=df, estimator="mean", marker="o")
    plt.title("Average Profit by Hour of Day")
    plt.show()

    # 6. Correlation Heatmap
    plt.figure(figsize=(8, 6))
    corr = df[["Order Value", "Discounts and Offers", "Delivery Fee",
               "Payment Processing Fee", "Commission Fee", "Profit"]].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()

    # 7. Delivery Duration vs Profit (Scatter Plot)
    plt.figure(figsize=(7, 5))
    sns.scatterplot(x="Delivery Duration (mins)", y="Profit", data=df, alpha=0.6, color="purple")
    plt.title("Delivery Duration vs Profit")
    plt.show()

    #  Insights
    print("\nINSIGHTS")

    # Cost contribution ranking
    print("\nCost Contribution (highest to lowest):\n", cost_dist.sort_values(ascending=False))

    # Day with highest average profit
    avg_profit_day = df.groupby("Day of Week")["Profit"].mean().sort_values(ascending=False)
    print("\nAverage Profit by Day of Week:\n", avg_profit_day)

    # Hour with highest average profit
    avg_profit_hour = df.groupby("Hour of Day")["Profit"].mean().sort_values(ascending=False)
    print("\nAverage Profit by Hour of Day:\n", avg_profit_hour)


if __name__ == "__main__":
    main()
