import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

#Task 1: Initial Loading
print("Task 1: Initial Loading")
Seoul_Bike_Data = pd.read_csv("seoul_bike_data.csv")
print(Seoul_Bike_Data.head().to_string(index= False ))

#Task 2: Data cleaning
print("Task 2: Data cleaning")

print("Before cleaning data:")
print(Seoul_Bike_Data.isnull().sum())

Seoul_Bike_Data = Seoul_Bike_Data.dropna()

print("After cleaning data:")
print(Seoul_Bike_Data.isnull().sum())
print(Seoul_Bike_Data.describe())


print(Seoul_Bike_Data.dtypes)
print("Columns with mixed value types:")
mixed_type_cols = []
for col in Seoul_Bike_Data.columns:
    unique_types = Seoul_Bike_Data[col].apply(type).value_counts()
    if len(unique_types) > 1:
        mixed_type_cols.append(col)
        print(f" {col} → {dict(unique_types)}")

if not mixed_type_cols:
    print("No columns have mixed types.")
print("\n")


unrealistics_rows = ((Seoul_Bike_Data["Rented Bike Count"] < 0) |
                     (Seoul_Bike_Data["Hour"] < 0) |
                     (Seoul_Bike_Data["Temperature(deg C)"] < -35) | 
                     (Seoul_Bike_Data["Temperature(deg C)"] > 45) |
                     (Seoul_Bike_Data["Humidity(%)"] > 100) | 
                     (Seoul_Bike_Data["Humidity(%)"] < 0) |
                     (Seoul_Bike_Data["Wind speed (m/s)"] < 0) |
                     (Seoul_Bike_Data["Visibility (10m)"] <0) |
                     (Seoul_Bike_Data["Solar Radiation (MJ/m2)"] < 0) |
                     (Seoul_Bike_Data["Rainfall(mm)"] < 0) |
                     (Seoul_Bike_Data["Snowfall (cm)"] < 0))
print("Total number of unrealistics rows:\n",unrealistics_rows.sum())


numeric_col = ["Rented Bike Count","Temperature(deg C)","Humidity(%)",
               "Wind speed (m/s)","Visibility (10m)","Solar Radiation (MJ/m2)",
               "Rainfall(mm)","Snowfall (cm)"]

Seoul_Bike_Data_cleaned = Seoul_Bike_Data.copy()
for num_col in numeric_col:
    Q1 = Seoul_Bike_Data_cleaned[num_col].quantile(0.25)
    Q3 = Seoul_Bike_Data_cleaned[num_col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    Seoul_Bike_Data_cleaned = Seoul_Bike_Data_cleaned[(Seoul_Bike_Data_cleaned[num_col] >= lower) & (Seoul_Bike_Data_cleaned[num_col] <= upper)]
print("Before cleaning:", len(Seoul_Bike_Data))
print("After cleaing: ", len(Seoul_Bike_Data_cleaned))

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

Seoul_Bike_Data[numeric_col].boxplot(ax=axes[0])
axes[0].set_title("Before Cleaning")
axes[0].tick_params(axis='x', rotation=45)

Seoul_Bike_Data_cleaned[numeric_col].boxplot(ax=axes[1])
axes[1].set_title("After Cleaning")
axes[1].tick_params(axis='x', rotation=45)

plt.suptitle("Box Plots of Numeric Columns — Before vs After Cleaning", fontsize=14)

plt.tight_layout() 
plt.show()


print("Duplicated value in Seoul Bike data: ", Seoul_Bike_Data_cleaned.duplicated().any())

# Task 3: Numerical analysis
print("Task 3: Numerical analysis")
numerical_column = ["Rented Bike Count","Temperature(deg C)","Humidity(%)"]
summary_array = np.array([
    [np.mean(Seoul_Bike_Data_cleaned["Rented Bike Count"]), np.median(Seoul_Bike_Data_cleaned["Rented Bike Count"]), np.std(Seoul_Bike_Data_cleaned["Rented Bike Count"])],
    [np.mean(Seoul_Bike_Data_cleaned["Temperature(deg C)"]), np.median(Seoul_Bike_Data_cleaned["Temperature(deg C)"]), np.std(Seoul_Bike_Data_cleaned["Temperature(deg C)"])],
     [np.mean(Seoul_Bike_Data_cleaned["Humidity(%)"]), np.median(Seoul_Bike_Data_cleaned["Humidity(%)"]), np.std(Seoul_Bike_Data_cleaned["Humidity(%)"])]
])
summary_table = pd.DataFrame(summary_array, columns = ["Mean", "Median", "Standard Deviation"],index = numerical_column)
print("\nSummary table:")
print(summary_table)

# Task 4: Simple plot
print("Task 4: Simple plot")


Seoul_Bike_Data_cleaned["Date"] = pd.to_datetime(Seoul_Bike_Data_cleaned["Date"], dayfirst = True)
monthly_rental = Seoul_Bike_Data_cleaned.groupby(Seoul_Bike_Data_cleaned["Date"].dt.to_period("M"))["Rented Bike Count"].sum()
monthly_rental.index = monthly_rental.index.to_timestamp()

plt.figure(figsize= (12,6))
plt.plot(monthly_rental.index, monthly_rental.values, marker= "o", label = "Monthly rentals",   linewidth = 2)
plt.title("Trends of renting bike in Seoul")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Total Rentals", fontsize=12)
plt.xticks(monthly_rental.index, rotation=60)
plt.grid(True, linestyle='--', alpha=0.3)
plt.legend()
plt.show()  

# Task 5: Multi-variable plot
print("Task 5: Multi-variable plot")
daily_rental = Seoul_Bike_Data_cleaned.groupby(Seoul_Bike_Data_cleaned["Date"])["Rented Bike Count"].sum()
average_temperature_daily = Seoul_Bike_Data_cleaned.groupby(Seoul_Bike_Data_cleaned["Date"])["Temperature(deg C)"].mean()
average_humidity_daily = Seoul_Bike_Data_cleaned.groupby(Seoul_Bike_Data_cleaned["Date"])["Humidity(%)"].mean()
average_windspeed_daily = Seoul_Bike_Data_cleaned.groupby(Seoul_Bike_Data_cleaned["Date"])["Wind speed (m/s)"].mean()
plt.figure(figsize = (12,6))
scatter = plt.scatter(average_temperature_daily,average_humidity_daily,
                      c=average_windspeed_daily,s = (daily_rental/150), 
                      cmap = "coolwarm", alpha = 0.7, edgecolors= "k")
plt.colorbar(scatter, label="Average wind speed ")
for size, label in [(50,"≈7,500 rentals"), (150,"≈22,500"), (300,"≈45,000+")]:
    plt.scatter([], [], s=size, c="gray", alpha=0.4, edgecolors="k", label=label)
plt.legend(title="Daily Rentals", frameon=True, loc="upper left")
plt.title("Daily Averages: Temperature, Humidity, Wind Speed, and Bike Rentals")
plt.xlabel("Average Temperature (°C)")
plt.ylabel("Average Humidity (%)")
plt.grid(True, linestyle='--', alpha=0.4)
plt.show()

# Task 6:
import seaborn as sns
sns.set_theme(style="whitegrid")

g = sns.FacetGrid(
    data=Seoul_Bike_Data_cleaned,
    col="Seasons",
    hue="Holiday",
    col_wrap=2,
    height=4.5,
    aspect=1.2
)
g.map_dataframe(sns.scatterplot, x="Temperature(deg C)", y="Rented Bike Count", alpha=0.5, s=25)
g.map_dataframe(sns.regplot, x="Temperature(deg C)", y="Rented Bike Count", scatter=False, ci=None, line_kws={'lw':1.5})
g.set_titles(col_template="{col_name}")
g.add_legend(title="Holiday")
g.set_axis_labels("Temperature (°C)", "Rented Bike Count")
g.fig.suptitle("Bike Rentals vs Temperature by Season and Holiday (with Trend Lines)", y=1.03)
plt.show()


