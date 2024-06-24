import pandas as pd
import matplotlib.pyplot as plt

# Define the file path
file_path = 'API_SP.POP.TOTL_DS2_en_csv_v2_429032.csv'  # Replace with your actual file path

# Step 1: Try to load the dataset without skipping rows to inspect its structure
try:
    df_full = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
    print(df_full.head(10))  # Display the first 10 rows to inspect
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")
except Exception as e:
    print(f"An error occurred while loading the dataset: {e}")

# Step 2: Based on the inspection, adjust the number of rows to skip if needed
# If the structure requires skipping rows, use skiprows parameter accordingly
try:
    df = pd.read_csv(file_path, skiprows=4)  # Adjust skiprows as needed based on the file structure
    print("Dataset loaded successfully with skipping rows!")
except Exception as e:
    print(f"An error occurred while loading the dataset with skipping rows: {e}")

# Display the first few rows to understand the structure of the data


# Step 3: Extract population data for the year 2021
try:
    df_2021 = df[['Country Name', '2021']].dropna()
    print("Data for the year 2021 extracted successfully!")
except KeyError as e:
    print(f"KeyError: {e} - Please ensure the column '2021' exists in the dataset.")
except Exception as e:
    print(f"An error occurred while extracting the data: {e}")

# Display the first few rows of the extracted data

# Step 4: Sort the data by population in descending order and select top 10 countries for better visualization
df_2021 = df_2021.sort_values(by='2021', ascending=False).head(10)

# Display the sorted data
print(df_2021)

# Step 5: Plotting the bar chart
try:
    plt.figure(figsize=(10, 6))
    plt.bar(df_2021['Country Name'], df_2021['2021'], color='skyblue')
    plt.xlabel('Country')
    plt.ylabel('Total Population in 2021')
    plt.title('Population Distribution by Country in 2021')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    print("Bar chart plotted successfully!")
except Exception as e:
    print(f"An error occurred while plotting the bar chart: {e}")
