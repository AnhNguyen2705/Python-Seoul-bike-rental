# Python-Seoul-bike-rental

### Project Context
This project analyses public bike rental data in Seoul to identify the key drivers of daily demand and translate insights into actionable business recommendations.

The objective was not only to perform statistical analysis, but to apply a structured, fact-based approach to understand how environmental factors influence customer behaviour and how those insights could support operational and strategic decision-making.

### Problem Statement
Urban bike-sharing systems operate in highly variable environments. Demand fluctuates due to weather, seasonality, and behavioural factors.

The key questions addressed were: What factors most strongly influence daily rental demand? How does demand fluctuate across seasons? What operational or strategic decisions could improve performance based on these patterns?

### Analytical Approach
#### 1. Data Validation & Cleaning

Before drawing conclusions, the dataset was rigorously examined to ensure reliability.

The process included:

Identifying and removing missing values (NaN)

Eliminating unrealistic entries (e.g., negative bike counts, invalid temperature ranges)

Removing duplicates

Applying logical validation filters (e.g., temperature bounds between -35°C and 45°C)

This step ensured that conclusions were based on credible, validated data, reducing bias and analytical risk.

#### 2. Quantitative Assessment
Key observations:

Rental demand is right-skewed (mean > median), indicating peak-demand days significantly impact overall averages.

High standard deviation (597) suggests strong volatility in demand.

Weather conditions vary substantially throughout the year.

This indicated that external factors likely drive rental variability, warranting deeper exploration.

### Key Insights
Temperature is the strongest driver of demand, especially between 20°C–30°C.

Moderate humidity supports higher rentals, while extreme humidity reduces demand.

Seasonal regression analysis shows stronger demand sensitivity in spring and autumn.

Holidays have minimal impact compared to environmental factors.

Overall, rental demand is primarily environmentally driven rather than calendar-driven.

### Business Implications
Increase capacity and staffing during spring and autumn.

Incorporate weather forecasts into demand planning models.

Align marketing campaigns with optimal weather conditions.

Plan cost-control strategies during low-demand winter periods.

### Demonstrated Skills
Structured, fact-based problem solving

Quantitative reasoning and insight generation

Translating analysis into strategic recommendations

Clear and concise communication
