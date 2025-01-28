import pandas as pd

data = pd.read_csv(r"C:\Users\ASUS\Desktop\vighnesh\dwm\Google.csv")


# Calculate descriptive statistics manually for each numeric column
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns

statistics = {}
for col in numeric_cols:
    col_data = data[col].dropna()  # Exclude missing values
    stats = {
        "Count": col_data.count(),
        "Mean": col_data.mean(),
        "Median": col_data.median(),
        "Mode": col_data.mode().iloc[0] if not col_data.mode().empty else np.nan,
        "Min": col_data.min(),
        "Max": col_data.max(),
        "Range": col_data.max() - col_data.min(),
        "Variance": col_data.var(),
        "Standard Deviation": col_data.std(),
        "25th Percentile": col_data.quantile(0.25),
        "50th Percentile (Median)": col_data.median(),
        "75th Percentile": col_data.quantile(0.75),
        "IQR (Interquartile Range)": col_data.quantile(0.75) - col_data.quantile(0.25)
    }
    statistics[col] = stats

# Convert to DataFrame for better visualization
statistics_df = pd.DataFrame(statistics)

# Display descriptive statistics to the user
import ace_tools as tools; tools.display_dataframe_to_user(name="Manual Descriptive Statistics", dataframe=statistics_df)

statistics_df