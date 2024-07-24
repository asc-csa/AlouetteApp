#
# Update_reception_facilities.py
# Script that matches the names of the reception facilities between Alouette & ISIS.
#
# @source https://github.com/asc-csa/AlouetteApp
# @author Emiline Filion - Canadian Space Agency
#
# Modification History:
# June 2024: Initial version
#

import pandas as pd

# Constants
INPUT_RECEPTION_FACILITIES = "reception_facilities.csv"
INPUT_DATA = "updated_result_master_ISIS_no_empty_values.csv"


# Loads matching matrix of reception facilities between Alouette & ISIS
# @return Dataframe that contains the match matrix.
def load_matching_reception_facilities():
    
    # Open the matching file
    matching_matrix = pd.read_csv(INPUT_RECEPTION_FACILITIES)
    return matching_matrix[['Alouette 1 Reception Facility', 'ISIS Reception Facility']]


# Applies the matching matrix, which adjust the names of the reception facilities in the input data file.
# @param input_csv_file Input CSV file
# @return Dataframe that contains data with the appropriate station names.
def apply_matching_matrix(input_csv_file):
    
    try:
        # Open data file
        df_data = pd.read_csv(input_csv_file)
        df_matching_matrix = load_matching_reception_facilities()
        
        # Loop through all reception facilities from the matching matrix
        for matching_case in df_matching_matrix.index:

            # Make sure the reception facility has the appropriate station name for each ionogram
            tmp_reception_facility_alouette = df_matching_matrix['Alouette 1 Reception Facility'][matching_case]
            tmp_reception_facility_isis = df_matching_matrix['ISIS Reception Facility'][matching_case]
            df_data.replace(tmp_reception_facility_isis, tmp_reception_facility_alouette, inplace=True)
    except Exception as e:
        print('Cannot open or process the input CSV file :' + str(e))

    return df_data


# Formats the input data file (timestamp, lattitude, longitude).
# @param Dataframe (output of apply_matching_matrix())
# @return Dataframe that contains data in the appropriate format.
def format_data(df_ddata):

    try:
        # Iterate for all ionogram
        nb_ionograms = len(df_ddata)
        for i in range(0, nb_ionograms, 1):
            
            # Format the timestamp (replace . by -)
            df_ddata.at[i, 'timestamp'] = str(df_ddata.at[i, 'timestamp']).replace('.', '-')
            
            if '-00' in str(df_ddata.at[i, 'timestamp']):
                print('Invalid time found for image L:/DATA/ISIS/ISIS_101300030772/' + str(df_ddata.at[i, 'file_name']) + '.png , timestamp: ' + str(df_ddata.at[i, 'timestamp']))
                        
            # Format the lattitude
            df_ddata.at[i, 'lat'] = str(df_ddata.at[i, 'lat']).replace('N', '')
            if 'S' in df_ddata.at[i, 'lat']:
                df_ddata.at[i, 'lat'] = '-' + str(df_ddata.at[i, 'lat']).replace('S', '')
            
            # Format the longitude
            df_ddata.at[i, 'lon'] = str(df_ddata.at[i, 'lon']).replace('E', '')
            if 'W' in df_ddata.at[i, 'lon']:
                df_ddata.at[i, 'lon'] = '-' + str(df_ddata.at[i, 'lon']).replace('W', '')
        
    except Exception as e:
        print('Cannot open or process the input CSV file :' + str(e))

    return df_ddata

#======================================================================================
# Main part

# Debut
print("\nThis script adjusts the name of the stations if the CSV file, which is used by the Alouette micro application.")
print("Input Data file: " + INPUT_DATA)
print("Matching matrix: " + INPUT_RECEPTION_FACILITIES)

# Rename the names of the reception facilities in the CSV file
print("Matching reception facilities...")
df_new_data = apply_matching_matrix(INPUT_DATA)
print("Formating the new CSV file...")
df_new_data = format_data(df_new_data)

# Save the new data file
new_data_filename = INPUT_DATA.replace(".csv", "_new.csv")
df_new_data.to_csv(new_data_filename, index=False)

# The End
print("\nThe program ended successfully")
print("New data file to use in the Alouette micro application: " + new_data_filename)
print("Have a good day!\n")