## Overview
This project analyzes **food delivery order data** to uncover insights into **cost distribution, discounts, delivery fees, and overall profitability.**
By applying **data preprocessing, exploratory data analysis (EDA), and visualization techniques,** it highlights patterns in customer behavior, operational costs, and profit drivers.
The project is designed to help businesses in the food delivery domain **optimize costs, track profitability trends, and make data-driven decisions.**

---

## Key Features
- **Data Cleaning & Preprocessing**:
  - Handles missing and inconsistent discount values.
  - Converts percentages to actual discount amounts.
  - Standardizes datetime columns and creates new features (day of week, hour of day, delivery duration).

- **Exploratory Data Analysis (EDA)**:
  - Visualizes cost distribution, profit patterns, and time-based trends.
  - Correlation heatmap for feature relationships.
  - Boxplots and scatterplots for profit variations.
 
- **Profit & Cost Analysis**:
  - Calculates **delivery costs, processing fees, and discounts.**
  - Derives **net profit per order** and aggregates performance by day and hour.
  - Identifies most profitable and loss-making orders.
 
- **Visualization & Insights**:
  - Cost distribution (pie chart).
  - Commission vs Costs vs Profit (bar chart).
  - Profit distribution (histogram with KDE).
  - Daily profit trends (line chart).
  - Profit distribution by weekday and hour (boxplot & line plot).
  - Delivery duration impact on profitability (scatterplot).

---

## Project Files
1. **food delivery costs.csv**:
   Raw dataset containing order-level details such as:
  - Order Date and Time
  - Delivery Date and Time
  - Order Value
  - Discounts and Offers
  - Delivery Fee
  - Commission Fee
  - Payment Processing Fee

2. **Analysis.py**:
   Python script that:
  - Loads and cleans the dataset
  - Generates new features
  - Performs profit and cost analysis
  - Produces visual insights and advanced summaries

---

## How to Run the Project
**Step 1: Install Dependencies**
```
pip install pandas matplotlib seaborn numpy
```

**Step 2: Run the Script**
```
python Analysis.py
```

**Step 3: View Results**
  - Console output will display **profit summaries, advanced insights, and grouped statistics.**
  - Multiple **visualizations** (pie charts, histograms, bar plots, heatmaps) will be shown
  - A cleaned dataset (cleaned_food_delivery.csv) and summary report (summary.csv) will be exported.

---

## Example Insights
  - **Cost Distribution:** Discounts contribute the highest share of costs.
  - **Profit by Weekday:** Midweek orders show higher average profit than weekends.
  - **Hourly Trends:** Profitability peaks during lunch (12–2 PM) and dinner (7–9 PM).
  - **Delivery Duration Impact:** Longer delivery times often reduce profitability.

---

## Future Enhancements
  - **Automated Report Generation:** Export results as a PDF dashboard.
  - **Predictive Modeling:** Forecast future profits using machine learning.
  - **Anomaly Detection:** Identify unusually high-cost or low-profit orders.
  - **Streamlit Dashboard:** Deploy an interactive analytics dashboard.

---

## Conclusion
This project demonstrates how **data analytics can optimize food delivery business operations** by analyzing costs, discounts, and profits.
The insights generated help decision-makers **improve margins, adjust discount strategies, and streamline operations.**

---

**Stay Data-Driven, Stay Profitable! 📈**
