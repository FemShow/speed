import pandas as pd

# Read the spreadsheet
file_path = '/Users/femisokoya/Documents/GitHub/Speed/cgn0503.xls'
worksheet_name = 'CGN0503d'
df = pd.read_excel(file_path, sheet_name=worksheet_name)

# Update column headers in row 5
df.iloc[5] = ["Country/Regional Local Authority", "ONS area code", "2019", "2020", "2021", "2022"]

# Delete rows 0 to 4
df = df.iloc[5:]

# Update column headers in new row 0
df.columns = df.iloc[0]

# Truncate values in column 2 (B) after the 9th character
df['ONS area code'] = df['ONS area code'].str[:9]

# Replace 'x' with '0' in columns 2 to 5
df.iloc[:, 2:6] = df.iloc[:, 2:6].replace('x', '0')

# Delete row 0
df = df.drop(df.index[0])

# Remove the string '[Note 9]' from column 0
df.iloc[:, 0] = df.iloc[:, 0].str.replace(r'\[Note 9\]', '', regex=True)

# Melt the dataframe
melted_df = df.melt(
    id_vars=["Country/Regional Local Authority", "ONS area code"],
    value_vars=["2019", "2020", "2021", "2022"],
    var_name="Period",
    value_name="Observation"
)

# Save the melted dataframe to a CSV file
result_path = '/Users/femisokoya/Documents/GitHub/Speed/result.csv'
melted_df.to_csv(result_path, index=False)
