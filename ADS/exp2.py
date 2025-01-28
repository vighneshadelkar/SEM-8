import pandas as pd
import seaborn as sns
import missingno as msno
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

# Load the dataset
file_path = '/mnt/data/diabetes_prediction_dataset.csv'
df = pd.read_csv(file_path)

# Display initial information
print("Initial Dataset Info:")
print(df.info())
print("\nMissing Values Count:\n", df.isnull().sum())

# Visualize missing data
msno.bar(df, figsize=(10, 5))
plt.show()

msno.heatmap(df, figsize=(10, 5))
plt.show()

# 1. Deletion of rows with missing data
df_dropped = df.dropna()
print(f"\nShape after dropping rows with missing data: {df_dropped.shape}")

# 2. Mean/Median Imputation
df_mean_imputed = df.fillna(df.mean())
df_median_imputed = df.fillna(df.median())

# 3. Mode Imputation
df_mode_imputed = df.copy()
for col in df.columns:
    df_mode_imputed[col].fillna(df_mode_imputed[col].mode()[0], inplace=True)

# 4. Arbitrary Value Imputation
arbitrary_value = -1
df_arbitrary_imputed = df.fillna(arbitrary_value)

# 5. End of Tail Imputation
df_end_of_tail = df.copy()
for col in df.select_dtypes(include=[np.number]).columns:
    end_of_tail_value = df[col].mean() + 3 * df[col].std()
    df_end_of_tail[col].fillna(end_of_tail_value, inplace=True)

# 6. Random Sample Imputation
df_random_sample = df.copy()
for col in df.columns:
    if df[col].isnull().sum() > 0:
        df_random_sample[col] = df[col].apply(
            lambda x: np.random.choice(df[col].dropna()) if pd.isnull(x) else x
        )

# 7. Frequent Category Imputation
df_frequent_category = df.copy()
for col in df.select_dtypes(include=['object']).columns:
    most_frequent = df[col].mode()[0]
    df_frequent_category[col].fillna(most_frequent, inplace=True)

# 8. Adding a new category as “missing” (for categorical columns)
df_new_category = df.copy()
for col in df.select_dtypes(include=['object']).columns:
    df_new_category[col] = df_new_category[col].fillna('missing')

# 9. Regression Imputation (for numerical columns)
df_regression = df.copy()
for col in df.select_dtypes(include=[np.number]).columns:
    if df[col].isnull().sum() > 0:
        # Split into train and test sets
        not_null = df[df[col].notnull()]
        null = df[df[col].isnull()]
        
        X_train = not_null.drop(columns=[col])
        y_train = not_null[col]
        X_test = null.drop(columns=[col])
        
        # Linear Regression Model
        reg = LinearRegression()
        reg.fit(X_train, y_train)
        
        # Predict and fill missing values
        df_regression.loc[df[col].isnull(), col] = reg.predict(X_test)

# Summary of all methods
print("\nMean Imputation Sample:\n", df_mean_imputed.head())
print("\nMedian Imputation Sample:\n", df_median_imputed.head())
print("\nMode Imputation Sample:\n", df_mode_imputed.head())
print("\nArbitrary Value Imputation Sample:\n", df_arbitrary_imputed.head())
print("\nEnd of Tail Imputation Sample:\n", df_end_of_tail.head())
print("\nRandom Sample Imputation Sample:\n", df_random_sample.head())
print("\nFrequent Category Imputation Sample:\n", df_frequent_category.head())
print("\nNew Category ('missing') Imputation Sample:\n", df_new_category.head())
print("\nRegression Imputation Sample:\n", df_regression.head())

# Correlation heatmap after regression imputation
plt.figure(figsize=(12, 8))
sns.heatmap(df_regression.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap after Regression Imputation")
plt.show()