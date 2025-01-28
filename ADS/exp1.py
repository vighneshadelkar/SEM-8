import pandas as pd

data = pd.read_csv(r"C:\Users\ASUS\Desktop\vighnesh\dwm\Google.csv")

print("First five rows of the dataset:")
print(data.head())

print("\nDescriptive Statistics:")
print(data.describe(include='all'))

print("\nMissing Values in Each Column:")
print(data.isnull().sum())
