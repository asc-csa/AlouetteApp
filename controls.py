# This file is depreciated. Controls had to be hard coded into app.py in the translate_static function. Babel could not translate from this file.

from flask_babel import Babel, _

# Controls for webapp
station_name_options = [
    {'label': _('Resolute Bay, No. W. Territories'), 'value': 'Resolute Bay, No. W. Territories'},
    {'label': _('Blossom Point, Maryland'), 'value': 'Blossom Point, Maryland'},
    {'label': _('South Atlantic, Falkland Islands'), 'value': 'South Atlantic, Falkland Islands'},
    {'label': _("St. John's, Newfoundland"), 'value': "St. John's, Newfoundland"},
    {'label': _('Orroral Valley, Australia'), 'value': 'Orroral Valley, Australia'},
    {'label': _('Prince Albert, Canada'), 'value': 'Prince Albert, Canada'},
    {'label': _('Ottawa, Canada'), 'value': 'Ottawa, Canada'},
    {'label': _('Byrd Station, Antartica'), 'value': 'Byrd Station, Antartica'},
    {'label': _('Las Palmas, Canary Island'), 'value': 'Las Palmas, Canary Island'},
    {'label': _('Winkfield, England'), 'value': 'Winkfield, England'},
    {'label': _('Fort Myers, Florida'), 'value': 'Fort Myers, Florida'},
    {'label': _('Antofagasta, Chile'), 'value': 'Antofagasta, Chile'},
    {'label': _('East Grand Forks, Minnesota'), 'value': 'East Grand Forks, Minnesota'},
    {'label': _('Rosman, No. Carolina'), 'value': 'Rosman, No. Carolina'},
    {'label': _('College, Fairbanks, Alaska'), 'value': 'College, Fairbanks, Alaska'},
    {'label': _('Woomera, Australia'), 'value': 'Woomera, Australia'},
    {'label': _('Gilmore Creek, Fairbanks, Alaska'), 'value': 'Gilmore Creek, Fairbanks, Alaska'},
    {'label': _('Tromso, Norway'), 'value': 'Tromso, Norway'},
    {'label': _('University of Alaska, Fairbanks, Alaska'), 'value': 'University of Alaska, Fairbanks, Alaska'},
    {'label': _('Darwin, Australia'), 'value': 'Darwin, Australia'},
    {'label': _('Quito, Ecuador'), 'value': 'Quito, Ecuador'},
    {'label': _('South Point, Hawaiian Islands'), 'value': 'South Point, Hawaiian Islands'},
    {'label': _('Lima, Peru'), 'value': 'Lima, Peru'},
    {'label': _('Johannesburg, South Africa'), 'value': 'Johannesburg, South Africa'},
    {'label': _('Kano, Nigeria'), 'value': 'Kano, Nigeria'},
    {'label': _('Tananarive, Madagascar'), 'value': 'Tananarive, Madagascar'},
    {'label': _('Bretigny, France'), 'value': 'Bretigny, France'},
    {'label': _('Singapore, Malaysia'), 'value': 'Singapore, Malaysia'},
    {'label': _('Boulder, Colorado'), 'value': 'Boulder, Colorado'},
    {'label': _('Mojave, California'), 'value': 'Mojave, California'},
    {'label': _('Kauai, Hawaii'), 'value': 'Kauai, Hawaii'},
    {'label': _('Kashima, Japan'), 'value': 'Kashima, Japan'}]

# Getting only the values of the station names
station_values = []
for station in station_name_options:
    station_values.append(station['value'])

x_axis_options = [
    {'label': _('Date'), 'value': ('timestamp')},
    {'label': _('Latitude'), 'value': ('lat')},
    {'label': _('Longitude'), 'value': ('lon')}]

y_axis_options = [
    {'label': _('Minimum Frequency'), 'value': ('fmin')},
    {'label': _('Maximum Depth'), 'value': ('max_depth')}]

year_dict = {}
for year in range(1962,1974):
    year_dict[year] = str(year)

lat_dict = {}
for lat in range(-90, 90+1, 15):
    lat_dict[lat] = str(lat)

lon_dict = {}
for lon in range(-180, 180+1, 30):
    lon_dict[lon] = str(lon)
