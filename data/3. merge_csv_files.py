#
# remove_empty_rows.py
# Script that merges all the CSV files into one single file.
# NOTE: You need to run remove_empty_rows.py before.
#
# @source https://github.com/asc-csa/AlouetteApp
# @author Emiline Filion - Canadian Space Agency
#
# Modification History:
# July 2024: Initial version
#

import pandas as pd

# Constants
ALOUETTE_CSV_FILE = "final_alouette_data.csv"
ISIS_CSV_FILE = "updated_result_master_ISIS_no_empty_values_new.csv"


# Removes rows when either max_depth or fmin are empty.
# @param input_csv_alouette Input CSV file (Alouette).
# @param input_csv_isis Input CSV file (ISIS).
# @return Dataframe that contains data with the appropriate station names.
def merge_csv_files(input_csv_alouette, input_csv_isis):
    
    try:
        # Open data file
        df_data1 = pd.read_csv(input_csv_alouette)
        df_data2 = pd.read_csv(input_csv_isis)
        tmp_frames = [df_data1, df_data2]
        de_result = pd.concat(tmp_frames)
    
    except Exception as e:
        print('Cannot open or process the input CSV file :' + str(e))

    return de_result

#======================================================================================
# Main part

# Debut
print("\nThis script merges all the CSV files into one single file, which is going to be used by the Alouette micro application.")
print("Alouette Input Data file: " + ALOUETTE_CSV_FILE)
print("ISIS Input Data file: " + ISIS_CSV_FILE)

# Merge CSV files
print("Merging CSV files...")
df_new_data = merge_csv_files(ALOUETTE_CSV_FILE, ISIS_CSV_FILE)

# Save the new data file
new_data_filename = ALOUETTE_CSV_FILE.replace(".csv", "_full.csv")
df_new_data.to_csv(new_data_filename, index=False)

# The End
print("\nThe program ended successfully")
print("New data file to use in the Alouette micro application: " + new_data_filename)
print("Have a good day!\n")