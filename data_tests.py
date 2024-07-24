#
# data_tests.py
# Script that tests the format and data of the input CSV file (final_alouette_data.csv).
#
# @source https://github.com/asc-csa/AlouetteApp
# @author Emiline Filion - Canadian Space Agency
#
# Modification History:
# June 2024: Initial version
#

import pandas as pd
import numpy as np

# Constants
INPUT_DATA = "data/updated_result_master_ISIS1_no_empty_values_new.csv"
NB_EXPECTED_COLUMNS = 11
NB_TESTS = (2 * NB_EXPECTED_COLUMNS) + 1
FALSE_ARRAY_EXPECTED = [False]
TRUE_ARRAY_EXPECTED = [True]


# Asserts the CSV files contains a particular column.
# @param df Dataframe.
# @param column_name Name of the column to validate.
# @param error_msg Error message (optional).
# @return True if the column is there. Otherwise, false.
def assert_column_exists(df, column_name, error_msg = ""):
    
    try:
        if df[column_name] is not None:
            return True
    except:
        print("ERROR: " + column_name + " is not present.")
    print(error_msg)
    return False

# Asserts the column does not have any empty cell.
# @param df Dataframe.
# @param column_name Name of the column to validate.
# @param error_msg Error message (optional).
# @return True if there are no empty cells. Otherwise, false.
def assert_no_empty_cells(df, column_name, error_msg = ""):
    
    try:
        boolean_column = pd.isna(df[column_name])
        if boolean_column.isin(TRUE_ARRAY_EXPECTED).any() : 
            print("ERROR: " + column_name + " has an empty values, which should not happen.")
            print(error_msg)
            return False
        return True

    except:
        print("ERROR: " + column_name + " has an empty values, which should not happen.")
    print(error_msg)
    return False


#======================================================================================
# Main part

# Debut
print("\nThis script tests the format and data of the input CSV file")
print("Input Data file: " + INPUT_DATA)
print("Running tests...\n")

# Make sure all required columns are present
nb_successful_tests = 0
df_data = pd.read_csv(INPUT_DATA)
if assert_column_exists(df_data, "file_name") : nb_successful_tests += 1
if assert_column_exists(df_data, "fmin") : nb_successful_tests += 1
if assert_column_exists(df_data, "max_depth") : nb_successful_tests += 1
if assert_column_exists(df_data, "subdir_name") : nb_successful_tests += 1
if assert_column_exists(df_data, "satellite_number") : nb_successful_tests += 1
if assert_column_exists(df_data, "station_number") : nb_successful_tests += 1
if assert_column_exists(df_data, "timestamp") : nb_successful_tests += 1
if assert_column_exists(df_data, "station_name") : nb_successful_tests += 1
if assert_column_exists(df_data, "3_letter_code") : nb_successful_tests += 1
if assert_column_exists(df_data, "lat") : nb_successful_tests += 1
if assert_column_exists(df_data, "lon") : nb_successful_tests += 1

# Make sure the satellite number is valid
valid_satellite_numbers = [1, 3, 4]
df_valid_sattelite_numbers = df_data['satellite_number'].isin(valid_satellite_numbers)
if df_valid_sattelite_numbers.isin(FALSE_ARRAY_EXPECTED).any() : print("ERROR: The CSV file contains invalid satellite numbers")
else : nb_successful_tests += 1

# Make sure there are no empty cells
if assert_no_empty_cells(df_data, "file_name") : nb_successful_tests += 1
if assert_no_empty_cells(df_data, "fmin") : nb_successful_tests += 1
if assert_no_empty_cells(df_data, "max_depth") : nb_successful_tests += 1
if assert_no_empty_cells(df_data, "subdir_name") : nb_successful_tests += 1
if assert_no_empty_cells(df_data, "satellite_number") : nb_successful_tests += 1
if assert_no_empty_cells(df_data, "station_number") : nb_successful_tests += 1
if assert_no_empty_cells(df_data, "timestamp") : nb_successful_tests += 1
if assert_no_empty_cells(df_data, "station_name") : nb_successful_tests += 1
if assert_no_empty_cells(df_data, "3_letter_code") : nb_successful_tests += 1
if assert_no_empty_cells(df_data, "lat") : nb_successful_tests += 1
if assert_no_empty_cells(df_data, "lon") : nb_successful_tests += 1

# The End
print("\nEnd of tests")
print("Number of tests: " + str(NB_TESTS))
print("Number of successful tests: " + str(nb_successful_tests))
if nb_successful_tests == NB_TESTS :
    print("All tests passed")
else:
    print("ERROR: Your CSV file does not have the right format.")
print("Have a good day!\n")