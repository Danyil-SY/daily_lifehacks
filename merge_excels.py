# Merge different excel files into one

import pandas as pd
import os

# set the directory where the Excel files are located
directory = "C:\\Users\\Default\\Documents\\123" # change this path name if needed
# initialize an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx") or filename.endswith(".xls"):
        # read the Excel file into a DataFrame
        file_path = os.path.join(directory, filename)
        df = pd.read_excel(file_path)
        
        # merge the columns apart from the first column with the existing merged data
        merged_data = pd.concat([merged_data, df.iloc[:, 0:]], axis=1)

# write the merged data to a new Excel file
merged_file_path = "C:\\Users\\Default\\Documents\\123\\merged_data.xlsx" # change this path name if needed
merged_data.to_excel(merged_file_path, index=False)

print("Merge complete. Merged data saved to", merged_file_path)