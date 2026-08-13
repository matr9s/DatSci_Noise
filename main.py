
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("creditcard.csv")
df = df.drop("Time", axis=1)
df['OutNum'] = 0
print(df.shape)

for col in df.columns[:-1]:
    Q1 = np.percentile(df[col], 25)
    Q3 = np.percentile(df[col], 75)
    IQR = Q3 - Q1
    lower_bound_iqr = Q1 - 1.5 * IQR
    upper_bound_iqr = Q3 + 1.5 * IQR
    print(lower_bound_iqr)
    print(upper_bound_iqr)
    outliers = (df[col] < lower_bound_iqr) | (df[col] > upper_bound_iqr)
    df.loc[outliers, "OutNum"] += 1
    df[col] = df[col].clip(lower=lower_bound_iqr, upper=upper_bound_iqr)

df = df[df["OutNum"] <= 0.10 * (len(df.columns) - 2)].reset_index(drop=True).columns[:-1]
print(df)

##############
"""
1. loop through every column
1.1 run IQR
1.2 store in list upper and lower lower_bound_iqr (dictionary)
2 check amount of missing values in row 
3 then based on amount of missing values determine whether to cap or remove
"""


# print(outliers_iqr)

# print(lower_bound_iqr)


"""
# Print identified outliers using IQR
print("Outliers (IQR):", outliers_iqr)
plt.boxplot(df)
plt.scatter([], [], color='blue', label='Normal Distribution with Outliers')
plt.scatter(outliers_iqr, [0] * len(outliers_iqr), color='red', label='outliers (IQR)')
plt.title('Boxplot with Outliers Detected by IQR')
plt.xlabel('Distribution')
plt.ylabel('Values')
plt.legend()
plt.tight_layout()
plt.show()
"""

"""
import numpy as np
import matplotlib.pyplot as plt
# Create a normal distribution of 5@ values
np.random.seed(42)
data_normal = np.random.normal(loc=0, scale=1, size=50)
# Add outliers (80 and 90)
data_with_outliers = np.concatenate([data_normal, [80, 90]])
# IQR method
# Sort the data
sorted_data = np.sort(data_with_outliers)
# Calculate quartiles
Q1 = np.percentile(sorted_data, 25)
Q3 = np.percentile(sorted_data, 75)
# Calculate IQR
IQR = Q3 - Q1
# Define Lower and upper bounds for outliers using IQR
lower_bound_iqr = max(min(sorted_data),Q1 - 1.5 * IQR)
upper_bound_iqr = min(max(sorted_data),Q3 + 1.5 * IQR)
# Identify outliers using IQR
outliers_iqr = [point for point in data_with_outliers if point < lower_bound_iqr or point > upper_bound_iqr]
# Print identified outliers using IQR
print("Outliers (IQR):", outliers_iqr)
plt.boxplot(data_with_outliers)
plt.scatter([], [], color='blue', label='Normal Distribution with Outliers')
plt.scatter(outliers_iqr, [0] * len(outliers_iqr), color='red', label='outliers (IQR)')
plt.title('Boxplot with Outliers Detected by IQR')
plt.xlabel('Distribution')
plt.ylabel('Values')
plt.legend()
plt.tight_layout()
plt.show()
"""
