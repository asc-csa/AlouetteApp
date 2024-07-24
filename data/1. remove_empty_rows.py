#
# remove_empty_rows.py
# Script that removes empty rows from the CSV file.
#
# @source https://github.com/asc-csa/AlouetteApp
# @author Emiline Filion - Canadian Space Agency
#
# Modification History:
# July 2024: Initial version
#

import pandas as pd

# Constants
INPUT_DATA = "updated_result_master_ISIS2.csv"

# Removes rows when either max_depth or fmin are empty.
# @param input_csv_file Input CSV file.
# @return Dataframe that contains data with the appropriate station names.
def remove_empty_row(input_csv_file):
    
    try:
        # Open data file
        df_data = pd.read_csv(input_csv_file)
        df_data["max_depth"].fillna(-1, inplace = True)
        df_data = df_data[df_data["max_depth"]!=-1]
    
    except Exception as e:
        print('Cannot open or process the input CSV file :' + str(e))

    return df_data

#======================================================================================
# Main part

# Debut
print("\nThis script removes empty rows from the CSV file, which is used by the Alouette micro application.")
print("Input Data file: " + INPUT_DATA)

# Remove rows when either max_depth or fmin are empty
print("Removing rows when either max_depth or fmin are empty...")
df_new_data = remove_empty_row(INPUT_DATA)

# Save the new data file
new_data_filename = INPUT_DATA.replace(".csv", "_no_empty_values.csv")
print(df_new_data)
df_new_data.to_csv(new_data_filename, index=False)

# The End
print("\nThe program ended successfully")
print("New data file to use in the Alouette micro application: " + new_data_filename)
print("Have a good day!\n")