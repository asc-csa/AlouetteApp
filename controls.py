#
# controls.py
# Control and convertion functions for the Alouette/ISIS micro application.
#
# @source https://github.com/asc-csa/AlouetteApp
# @author Emiline Filion - Canadian Space Agency
#
# Modification History:
# June 2024: Addition of ISIS 1&2 data.
#

import pandas as pd
import datetime as dt


# Constants
SATELLITE_1_STR = "Alouette 1"
SATELLITE_2_STR = "Alouette 2"
SATELLITE_3_STR = "ISIS 1"
SATELLITE_4_STR = "ISIS 2"


# Converts the satellite number to its name
# 1: Alouette 1
# 2: Alouette 2
# 3: ISIS 1
# 4: ISIS 2
# @param sat_number Satellite number
# @return Satellite name
def get_satellite_name(sat_number):

    if sat_number == '2':
        return SATELLITE_2_STR
    if sat_number == '3':
        return SATELLITE_3_STR
    if sat_number == '4':
        return SATELLITE_4_STR
    return SATELLITE_1_STR


# Converts an array of satellite names to satellite numbers
# 1: Alouette 1
# 2: Alouette 2
# 3: ISIS 1
# 4: ISIS 2
# @param Array of satellite names
# @return Array of satellite numbers
def convert_array_satellite_names_to_numbers(array_satellite_names):
 
    print('\nDEBUG: entering convert_array_satellite_names_to_numbers() ' + str(array_satellite_names))
    array_satellite_numbers = []
    for tmp_satellite_name in array_satellite_names:
    
        if tmp_satellite_name == SATELLITE_1_STR:
            array_satellite_numbers.append(1)
        elif tmp_satellite_name == SATELLITE_2_STR:
            array_satellite_numbers.append(2)
        elif tmp_satellite_name == SATELLITE_3_STR:
            array_satellite_numbers.append(3)
        elif tmp_satellite_name == SATELLITE_4_STR:
            array_satellite_numbers.append(4)
        else:
            array_satellite_numbers.append(tmp_satellite_name)
    
    print('\nDEBUG: end of convert_array_satellite_names_to_numbers() ' + str(array_satellite_numbers))
    return array_satellite_numbers


# Converts a latitude or longitude coordinate from a string to a float, taking into account N, E, S, W.
# For example, '48.2S' to -48.2
# @param coord The string form of the coordinate.
# @return The coordinate in float form.
def coords_to_float(coord):
    
    if coord != None:
        if str(coord)[-1] == 'N' or str(coord)[-1] == 'E':
            return float(str(coord)[:-1])
        elif str(coord)[-1] == 'S' or str(coord)[-1] == 'W': # removes the letter from '48.2S' and puts a negative
            return float(str(coord)[:-1]) * -1
        else:
            return coord
    else:
        return coord


# Filters the extracted ionogram dataframe on multiple parameters.
# @param df : DataFrame (note: SciPy/NumPy documentation usually refers to this as array_like)
#        The DataFrame with ionogram data to be filtered.
# @param start_date_dt : datetime object
#        Starting date stored as a datetime object
# @param end_date_dt : datetime object
#        Ending date stored as a datetime object
# @param lat_min : double
#        Minimum value of the latitude stored as a double.
# @param lat_max : double
#        Maximum value of the latitude stored as a double.
# @param lon_min : double
#        Minimum value of the longitude stored as a double.
# @param lon_max : double
#        Maximum value of the longitude stored as a double.
# @param ground_stations : list
#        Ground station name strings stored in a list (e.g. ['Resolute Bay, No. W. Territories'])
# @param satellites : list
#        Satellites name strings stored in a list (e.g. ['Alouette 1'])
# @return The filtered DataFrame
def filter_dataframe(df, start_date_dt, end_date_dt, lat_min, lat_max, lon_min, lon_max, ground_stations=None, satellites=None):
    
    #print('\nDEBUG: entering filter_dataframe()')
    print('Satellites selected: ' + str(satellites))
    #start_time = dt.datetime.now()

    #print(f'DEBUG: filter_dataframe(), point #1 - Time spent (s): {(dt.datetime.now()-start_time).total_seconds()}')
    #TODO: the next line takes time (1.5 second)
    dff = df[
        (df["timestamp"].dt.date >= dt.date(start_date_dt.year, start_date_dt.month, start_date_dt.day))
        & (df["timestamp"].dt.date <= dt.date(end_date_dt.year, end_date_dt.month, end_date_dt.day))
            ]
    #print(f'DEBUG: filter_dataframe(), point #2 - Time spent (s): {(dt.datetime.now()-start_time).total_seconds()}')
    if (lat_min != -90) or (lat_max != 90):
        dff = dff[
            (dff["lat"] >= lat_min)
            & (dff["lat"] <= lat_max)
               ]
    if (lon_min != -180) or (lon_max != 180):
        dff = dff[
            (dff["lon"] >= lon_min)
            & (dff["lon"] <= lon_max)
                ]
    if (ground_stations is not None) and (ground_stations != []):
        dff = dff[
            (dff["station_name"].isin(ground_stations))
            ]
    if (satellites is not None) and (satellites != []):
        dff = dff[
            (dff["satellite_number"].isin(convert_array_satellite_names_to_numbers(satellites)))
            ]
    
    #print(f'DEBUG: end of filter_dataframe() - TOTAL Time spent (s): {(dt.datetime.now()-start_time).total_seconds()}')
    return dff
