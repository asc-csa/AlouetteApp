# -*- coding: utf-8 -*-
import dash
import pathlib
import copy
import dash_core_components as dcc
import dash_html_components as html
import dash_dangerously_set_inner_html
import plotly.graph_objs as go
import pandas as pd
import datetime as dt
from scipy.stats import sem, t
from scipy import mean
from dateutil.relativedelta import relativedelta
from dash.dependencies import Input, Output
import locale
import urllib.parse

from zipfile import ZipFile
import os
import flask
from io import StringIO
from flask_babel import _ ,Babel
from flask import session, redirect, url_for, request



external_stylesheets = ['https://wet-boew.github.io/themes-dist/GCWeb/assets/favicon.ico',
                        'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
                        'https://wet-boew.github.io/themes-dist/GCWeb/css/theme.min.css',
                        'https://wet-boew.github.io/themes-dist/GCWeb/wet-boew/css/noscript.min.css']  # Link to external CSS

external_scripts = [
    'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.js',
    'https://wet-boew.github.io/themes-dist/GCWeb/wet-boew/js/wet-boew.min.js',
    'https://wet-boew.github.io/themes-dist/GCWeb/js/theme.min.js',
    'https://cdn.plot.ly/plotly-locale-de-latest.js'
]


if __name__ == '__main__':
     prefixe=""
#     app.run_server(debug=True)  # For development/testing
     from header_footer import gc_header_en, gc_footer_en, gc_header_fr, gc_footer_fr


    
     df = pd.read_csv(r'data/final_alouette_data.csv')  # edit for compatibility with CKAN portal (e.g. API to dataframe)
  
     app = dash.Dash(__name__,meta_tags=[{"name": "viewport", "content": "width=device-width"}],external_stylesheets=external_stylesheets,external_scripts=external_scripts,)
     app.title="Alouette: application d’exploration des données d’ionogrammes historiques | data exploration application for historic ionograms"
     server = app.server
     server.config['SECRET_KEY'] = '78b81502f7e89045fe634e85d02f42c5'  # Setting up secret key to access flask session
     babel = Babel(server)  # Hook flask-babel to the app

  
    

else :
    prefixe="/alouette"
    from applications.alouette.header_footer import gc_header_en, gc_footer_en, gc_header_fr, gc_footer_fr
    df = pd.read_csv(r'applications/alouette/data/final_alouette_data.csv')  # edit for compatibility with CKAN portal (e.g. API to dataframe)
    
    app = dash.Dash(
    __name__,
    requests_pathname_prefix='/alouette/',
    meta_tags=[{"name": "viewport", "content": "width=device-width"}],
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
)
    app.title="Alouette: application d’exploration des données d’ionogrammes historiques | data exploration application for historic ionograms"
    server = app.server
    server.config['SECRET_KEY'] = '78b81502f7e89045fe634e85d02f42c5'  # Setting up secret key to access flask session
    babel = Babel(server)  # Hook flask-babel to the app







# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()  # path to "data" folder

IONOGRAM_PATH = 'U:/Downloads'  # Directory to Ionogram images for testing
# IONOGRAM_PATH = '/storage_slow/ftp_root/users/OpenData_DonneesOuvertes/pub/AlouetteData/Alouette Data'  # Directory to Ionogram images on server

# load data and transform as needed
#dtypes = {'': 'int', 'file_name': 'str', 'max_depth': 'float', 'decimal_value': 'str'}


# Dropdown options
#======================================================================================
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

#======================================================================================

def coords_to_float(coord):
    """Convert a latitude or longitude coordinate from a string to a float, taking into account N, E, S, W.

    For example, '48.2S' to -48.2

    Parameters
    ----------
    coord : str
        The string form of the coordinate

    Returns
    -------
    float
        The coordinate in float form
    """
    if coord != None:
        if str(coord)[-1] == 'N' or str(coord)[-1] == 'E':
            return float(str(coord)[:-1])
        elif str(coord)[-1] == 'S' or str(coord)[-1] == 'W': # removes the letter from '48.2S' and puts a negative
            return float(str(coord)[:-1]) * -1
        else:
            return coord
    else:
        return coord



df['timestamp'] = pd.to_datetime(df['timestamp'])  # converts the timestamp to date_time objects
 
df['lat'] = df.apply(lambda x: coords_to_float(x['lat']), axis=1)
df['lon'] = df.apply(lambda x: coords_to_float(x['lon']), axis=1)

# Create global chart template
mapbox_access_token = "pk.eyJ1IjoiamFja2x1byIsImEiOiJjajNlcnh3MzEwMHZtMzNueGw3NWw5ZXF5In0.fk8k06T96Ml9CLGgKmk81w"

layout = dict(
    autosize=True,
    automargin=True,
    margin=dict(l=30, r=30, b=20, t=40),
    hovermode="closest",
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#F9F9F9",
    # legend=dict(font=dict(size=10), orientation="h"),
    title="Ground Station Overview",
    mapbox=dict(
        accesstoken=mapbox_access_token,
        style="light",
        # center=dict(lon=-78.05, lat=42.54),
        zoom=2,
    ),
    transition={'duration': 500},
)


# Builds the layout for the header
def build_header():
    return html.Div(
            [
                html.Div([], className="one column"),
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url("csa-logo.png"),
                            id="csa-image",
                            style={
                                "height": "60px",
                                "width": "auto",
                                "margin": "25px",
                            },
                            alt="CSA Logo"
                        )
                    ],
                    className="one column",
                ),
                html.Div(
                    [
                        html.H3(
                            "",
                            style={"margin-bottom": "10px", "margin-left": "15%"},
                            id="page-title"),
                    ],
                    className="six columns",
                    id="title",
                ),
                html.Div(
                    [
                        html.A(
                            html.Button("", id="learn-more-button", className="dash_button"),
                            href="http://www.asc-csa.gc.ca/eng/satellites/alouette.asp"
                        ),
                        html.A(
                            html.Button('FR', id='language-button', className="dash_button"),
                            href='/alouette/language/fr', id='language-link'
                        ),
                    ],
                    className="four columns",
                    id="button-div",
                    style={"text-align": "center"}
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        )


# Builds the layout and components for the inputs to filter the data, as well as the ionograms/month graph and the ground stations map
def build_filtering():
    return html.Div([
        html.Div(
            [
                html.Div(
                    [
                        html.H3(id="ionograms_text"),
                        html.P(id="ionograms-ratio")
                    ],
                    id="info-container",
                    className="mini_container three columns",
                    style={"text-align": "center"},
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                 html.H6(id="description"),
                                 html.P(id="description-1"),
                                 html.P(id="description-2"),
                            ],
                            id="description_div",
                        ),
                    ],
                    id="description-container",
                    className="container-display mini_container nine columns",
                ),
            ],
            className="row flex-display twelve columns"
        ),

        html.Div(
            [
                html.H3(
                   id="select-data"
                ),
            ],
            style={"margin-top": "10px", "margin-left": "auto", "margin-right": "auto", "text-align": "center"},
            className="twelve columns"
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [dcc.Graph(id="selector_map")],
                        ),
                        html.Div(
                            [
                                html.P(
                                    id="groundstations-text",
                                    className="control_label",
                                ),
                                html.Label(
                                    dcc.Dropdown(
                                        id="ground_station_list",
                                        options=[],
                                        multi=True,
                                        value=station_values,
                                        className="dcc_control",
                                    ),
                                ),
                                html.Div(
                                    [
                                        html.P(
                                            id="latitude-text",
                                            className="control_label",
                                        ),
                                        # dcc.RangeSlider(
                                        #     id="lat_slider",
                                        #     min=-90.0,
                                        #     max=90.0,
                                        #     value=[-90.0, 90.0],
                                        #     className="dcc_control",
                                        #     marks=lat_dict,
                                        # ),
                                        dcc.Input(
                                            id="lat_min",
                                            type='number',
                                            value=-90.0,
                                            placeholder="Min Latitude",
                                            min=-90.0,
                                            max=90.0,
                                            step=5,
                                            style={"margin-left": "5px"}
                                        ),
                                        dcc.Input(
                                            id="lat_max",
                                            type='number',
                                            value=90.0,
                                            placeholder="Max Latitude",
                                            min=-90.0,
                                            max=90.0,
                                            step=5,
                                            style={"margin-left": "5px"}
                                        ),
                                        html.H5(
                                            "", style={"margin-top": "30px"}
                                        ),
                                    ],
                                    className="one-half column"
                                ),
                                html.Div(
                                    [
                                        html.P(
                                            id="longitude-text",
                                            className="control_label",
                                        ),
                                        # dcc.RangeSlider(
                                        #     id="lon_slider",
                                        #     min=-180.0,
                                        #     max=180.0,
                                        #     value=[-180.0, 180.0],
                                        #     className="dcc_control",
                                        #     marks=lon_dict,
                                        # ),
                                        dcc.Input(
                                            id="lon_min",
                                            type='number',
                                            value=-90.0,
                                            placeholder="Min Longitude",
                                            min=-90.0,
                                            max=90.0,
                                            step=5,
                                            style={"margin-left": "5px"}
                                        ),
                                        dcc.Input(
                                            id="lon_max",
                                            type='number',
                                            value=90.0,
                                            placeholder="Max Longitude",
                                            min=-90.0,
                                            max=90.0,
                                            step=5,
                                            style={"margin-left": "5px"}
                                        ),
                                    ],
                                    className="one-half column"
                                ),
                                html.H5(
                                    "", style={"margin-top": "10px"}
                                ),
                            ],
                            id="map-options",
                        ),
                    html.P(id="Map_description-1"),
                    ],

                    id="left-column-1",
                    style={"flex-grow": 1},
                    className="six columns",
                ),
                html.Div(
                    [
                        html.Div(
                            [dcc.Graph(id="count_graph")],
                            id="countGraphContainer",
                        ),
                        html.Div(
                            [
                                html.P(
                                    id="yearslider-text",
                                    className="control_label",
                                ),
                                # dcc.RangeSlider(
                                #     id="year_slider",
                                #     min=1962,
                                #     max=1973,
                                #     value=[1962, 1973],
                                #     className="dcc_control",
                                #     marks=year_dict
                                # ),
                                html.Div([
                                    html.Label(
                                        dcc.DatePickerRange(
                                            id='date_picker_range',
                                            min_date_allowed=dt.datetime(1962, 9, 29),
                                            max_date_allowed=dt.datetime(1972, 12, 31),
                                            #initial_visible_month=dt.datetime(1962, 9, 29),
                                            start_date=dt.datetime(1962, 9, 29),
                                            end_date=dt.datetime(1972, 12, 31),
                                            start_date_placeholder_text='Select start date',
                                            end_date_placeholder_text='Select end date',
                                            style={"margin-top": "5px"}
                                        ),
                                    ),
                                    html.Div(id='output-container-date-picker-range')
                                ]),
                                html.H5(
                                    "", style={"margin-top": "30px", "margin-bottom": "25px"}
                                ),
                                html.Div(
                                    [
                                        html.A(
                                            html.Button(id='download-button-1', n_clicks=0, className="dash_button", style={'padding': '0px 10px'}),
                                            id='download-link-1',
                                            # download='rawdata.csv',
                                            href="",
                                            target="_blank",
                                        ),
                                        html.A(
                                            html.Button(id='download-button-2',  n_clicks=0, className="dash_button", style={'padding': '0px 10px'}),
                                            id='download-link-2',
                                            style={"margin-left": "5px"},
                                        )
                                    ],
                                ),
                            ],
                            id="cross-filter-options",
                        ),
                    html.Div ([html.P(id="Graph_description-1")]),
                    ],
                    id="right-column-1",
                    style={"flex-grow": 1},
                    className="six columns",
                ),
            ],
            className="row flex-display pretty_container twelve columns",
            style={"justify-content": "space-evenly"}
        ),

    ])


# Builds the layout for the map displaying statistics as well as the confidence interval graph
def build_stats():
    return html.Div([
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [dcc.Graph(id="viz_chart")],
                            id="vizChartContainer",
                            #className="pretty_container",
                        ),
                    ],
                    id="left-column-3",
                    className="nine columns",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.P(
                                    id="x-axis-selection-text",
                                    className="control_label",
                                ),
                                html.Label(
                                    dcc.Dropdown(
                                        id="x_axis_selection_1",
                                        options=x_axis_options,
                                        multi=False,
                                        value='timestamp',
                                        className="dcc_control",
                                    ),
                                ),
                                html.P(
                                    id="y-axis-selection-text",
                                    className="control_label",
                                ),
                                html.Label(
                                    dcc.Dropdown(
                                        id="y_axis_selection_1",
                                        options=y_axis_options,
                                        multi=False,
                                        value='max_depth',
                                        className="dcc_control",
                                    ),
                                ),
                            ],
                            #className="pretty_container",
                            id="viz-chart-options",
                        ),
                        html.Div ([html.P(id="Map_description-2")]),
                    ],
                    id="right-column-3",
                    className="three columns",
                ),
            ],
            className="row flex-display pretty_container",
            #style={"height": "500px"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [dcc.Graph(id="viz_map")],
                            id="vizGraphContainer",
                        ),
                    ],
                    id="left-column-4",
                    className="nine columns",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.P(
                                    id="stat-selection-text",
                                    className="control_label",
                                ),
                                html.Label(
                                    dcc.Dropdown(
                                        id="stat_selection",
                                        options=[
                                            {'label': 'Mean', 'value': 'mean'},
                                            {'label': 'Median', 'value': 'median'}
                                        ],
                                        multi=False,
                                        value='mean',
                                        className="dcc_control",
                                    ),
                                ),
                                html.P(
                                    id="stat-y-axis-text",
                                    className="control_label",
                                ),
                                html.Label(
                                    dcc.Dropdown(
                                        id="y_axis_selection_2",
                                        options=y_axis_options,
                                        multi=False,
                                        value='max_depth',
                                        className="dcc_control",
                                    ),
                                ),
                            ],
                            #className="pretty_container",
                            id="map-viz-options",
                        ),
                        html.Div ([html.P(id="Graph_description-2")]),
                    ],
                    id="right-column-4",
                    className="three columns",
                ),
            ],
            className="row flex-display pretty_container",
            #style={"height": "500px"},
        ),
        html.Div(id='none', children=[], style={'display': 'none'}), # Placeholder element to trigger translations upon page load
    ])


# Create app layout
app.layout = html.Div(
    [
        html.Div([""], id='gc-header'),
        html.Div(
            [
                dcc.Store(id="aggregate_data"),
                html.Div(id="output-clientside"),  # empty Div to trigger javascript file for graph resizing

                build_header(),
                build_filtering(),
                build_stats(),
            ],
            id="mainContainer",
            style={"display": "flex", "flex-direction": "column", "margin": "auto", "width":"75%"},
        ),
        html.Div([""], id='gc-footer'),
        html.Div(id='none2', children=[], style={'display': 'none'}), # Placeholder element to trigger translations upon page load
    ],
)



# Helper functions
def filter_dataframe(df, start_date_dt, end_date_dt, lat_min, lat_max, lon_min, lon_max, ground_stations=None):
    """Filter the extracted ionogram dataframe on multiple parameters.

    Called for every component.

    Parameters
    ----------
    df : DataFrame (note: SciPy/NumPy documentation usually refers to this as array_like)
        The DataFrame with ionogram data to be filtered.

    start_date_dt : datetime object
        Starting date stored as a datetime object

    end_date_dt : datetime object
        Ending date stored as a datetime object

    lat_min : double
        Minimum value of the latitude stored as a double.
        
    lat_max : double
        Maximum value of the latitude stored as a double.
        
    lon_min : double
        Minimum value of the longitude stored as a double.
        
    lon_max : double
        Maximum value of the longitude stored as a double.

    ground_stations : list
        Ground station name strings stored in a list (e.g. ['Resolute Bay, No. W. Territories'])

    Returns
    -------
    DataFrame
        The filtered DataFrame
    """

    dff = df[
        (df["timestamp"].dt.date >= dt.date(start_date_dt.year, start_date_dt.month, start_date_dt.day))
        & (df["timestamp"].dt.date <= dt.date(end_date_dt.year, end_date_dt.month, end_date_dt.day))
            ]
    if (lat_min != -90) or (lat_max != 90):
        dff = dff[
            (dff["lat"] >= lat_min)
            & (dff["lat"] <= lat_max)
               ]
    if (lon_min != -90) or (lon_max != 90):
        dff = dff[
            (dff["lon"] >= lon_min)
            & (dff["lon"] <= lon_max)
                ]
    if (ground_stations is not None) and (ground_stations != []):
        dff = dff[
            (dff["station_name"].isin(ground_stations))
            ]

    return dff


# Selectors -> ionogram count
@app.callback(
    Output("ionograms_text", "children"),
    [
        Input("date_picker_range", "start_date"),
        Input("date_picker_range", "end_date"),
        Input("lat_min", "value"),
        Input("lat_max", "value"),
        Input("lon_min", "value"),
        Input("lon_max", "value"),
        Input("ground_station_list", "value"),
    ],
)
def update_ionograms_text(start_date, end_date, lat_min, lat_max, lon_min, lon_max, ground_stations=None):
    """Update the component that counts the number of ionograms selected.

    Parameters
    ----------
    start_date : str
        Starting date stored as a str

    end_date : str
        Ending date stored as a str

    lat_min : double
        Minimum value of the latitude stored as a double.
        
    lat_max : double
        Maximum value of the latitude stored as a double.
        
    lon_min : double
        Minimum value of the longitude stored as a double.
        
    lon_max : double
        Maximum value of the longitude stored as a double.

    ground_stations : list
        Ground station name strings stored in a list (e.g. ['Resolute Bay, No. W. Territories'])

    Returns
    -------
    int
        The number of ionograms present in the dataframe after filtering
    """
    start_time = dt.datetime.now()

    start_date = dt.datetime.strptime(start_date.split('T')[0], '%Y-%m-%d')  # Convert strings to datetime objects
    end_date = dt.datetime.strptime(end_date.split('T')[0], '%Y-%m-%d')

    dff = filter_dataframe(df, start_date, end_date, lat_min, lat_max, lon_min, lon_max, ground_stations)

    print(f'update_ionograms_text: {(dt.datetime.now()-start_time).total_seconds()}')

    return "{:n}".format(dff.shape[0]) + " / " + "{:n}".format(406566)


# Selectors -> ground stations
@app.callback(
    Output("ground_station_list", "value"),
    [
        Input("lat_min", "value"),
        Input("lat_max", "value"),
        Input("lon_min", "value"),
        Input("lon_max", "value"),
    ],
)
def update_ground_station_list(lat_min, lat_max, lon_min, lon_max):
    """Update the list of ground stations selected based on the other user-selected parameters.

    Parameters
    ----------
    lat_min : double
        Minimum value of the latitude stored as a double.
        
    lat_max : double
        Maximum value of the latitude stored as a double.
        
    lon_min : double
        Minimum value of the longitude stored as a double.
        
    lon_max : double
        Maximum value of the longitude stored as a double.

    Returns
    -------
    list
        The number of ground stations present in the current selection
    """
    # Manually set the value for dates so that changing the date does not update the ground station list
    start_date = dt.datetime(year=1962, month=9, day=29)
    end_date = dt.datetime(year=1972, month=12, day=31)


    dff = filter_dataframe(df, start_date, end_date, lat_min, lat_max, lon_min, lon_max)
    if len(dff['station_name'].unique()) < 32: # if we have selected a subset of ground stations, return the selected list
        return list(dff['station_name'].unique())
    else:
        return [] # if we have not selected any stations, keep the selection box empty


# Selectors -> Image download link
@app.callback(
    Output("download-link-2", "href"),
    [
        Input("date_picker_range", "start_date"),
        Input("date_picker_range", "end_date"),
        Input("lat_min", "value"),
        Input("lat_max", "value"),
        Input("lon_min", "value"),
        Input("lon_max", "value"),
        Input("ground_station_list", "value"),
    ],
)
def update_images_link(start_date, end_date, lat_min, lat_max, lon_min, lon_max, ground_stations=None):
    """Updates the link to the Ionogram images download

    Returns
    -------
    link : str
        Link that redirects to the Flask route to download the CSV based on selected filters
    """

    link = '/dash/downloadImages?start_date={}&end_date={}&lat_min={}&lat_max={}&lon_min={}&lon_max={}&ground_stations={}'\
        .format(start_date, end_date, lat_min, lat_max, lon_min, lon_max, ground_stations)

    return link


from io import BytesIO



@app.server.route('/dash/downloadImages')
def download_images():

    start_date = dt.datetime.strptime(flask.request.args.get('start_date').split('T')[0], '%Y-%m-%d')  # Convert strings to datetime objects
    end_date = dt.datetime.strptime(flask.request.args.get('end_date').split('T')[0], '%Y-%m-%d')

    lat_min = flask.request.args.get('lat_min')
    lat_max = flask.request.args.get('lat_max')
    lon_min = flask.request.args.get('lon_min')
    lon_max = flask.request.args.get('lon_max')

    ground_stations = flask.request.args.get('ground_stations') # parses a string representation of ground_stations
    ground_stations = literal_eval(ground_stations) # converts into a list representation

    dff = filter_dataframe(df, start_date, end_date, int(lat_min), int(lat_max), int(lon_min), int(lon_max), ground_stations)

    dff['file_path'] = dff['file_name'].map(lambda x: os.path.join(IONOGRAM_PATH, x) + '.png')

    # Store the zip in memory
    memory_file = BytesIO()
    max_download = 100  # Temporary limit on number of ionograms that can be downloaded
    with ZipFile(memory_file, 'w') as zf:
        for index, row in dff.iterrows():
            if os.path.exists(row['file_path']) and max_download > 0:
                max_download -= 1
                zf.write(row['file_path'], arcname=row['file_name']+'.png')  # Write each image into the zip

        # Making the output csv from the filtered df
        csv_buffer = StringIO()
        dff.to_csv(csv_buffer, index=False)
        zf.writestr('Metadata_of_selected_ionograms.csv', csv_buffer.getvalue())

    memory_file.seek(0)

    return flask.send_file(memory_file, attachment_filename='Ionograms.zip', as_attachment=True)



# Selectors -> CSV Link
@app.callback(
    Output("download-link-1", "href"),
    [
        Input("date_picker_range", "start_date"),
        Input("date_picker_range", "end_date"),
        Input("lat_min", "value"),
        Input("lat_max", "value"),
        Input("lon_min", "value"),
        Input("lon_max", "value"),
        Input("ground_station_list", "value"),
    ],
)
def update_csv_link(start_date, end_date, lat_min, lat_max, lon_min, lon_max, ground_stations=None):
    """Updates the link to the CSV download

    Returns
    -------
    link : str
        Link that redirects to the Flask route to download the CSV based on selected filters
    """

    link = '/dash/downloadCSV?start_date={}&end_date={}&lat_min={}&lat_max={}&lon_min={}&lon_max={}&ground_stations={}' \
            .format(start_date, end_date, lat_min, lat_max, lon_min, lon_max, ground_stations)

    return link

from flask import make_response
from ast import literal_eval


# Flask route that handles the CSV downloads. This allows for larger files to be passed,
# as well as avoiding generating the CSV until the download is desired
@app.server.route('/dash/downloadCSV')
def download_csv():
    """Generates the CSV and sends it to the user

    args
    ----------
    start_date : str
        Starting date stored as a str

    end_date : str
        Ending date stored as a str

    lat_min : double
        Minimum value of the latitude stored as a double.
        
    lat_max : double
        Maximum value of the latitude stored as a double.
        
    lon_min : double
        Minimum value of the longitude stored as a double.
        
    lon_max : double
        Maximum value of the longitude stored as a double.

    ground_stations : list
        Ground station name strings stored in a list (e.g. ['Resolute Bay, No. W. Territories'])

    Returns
    -------
    output : CSV
        CSV file based on the applied filters
    """

    start_date = dt.datetime.strptime(flask.request.args.get('start_date').split('T')[0], '%Y-%m-%d')  # Convert strings to datetime objects
    end_date = dt.datetime.strptime(flask.request.args.get('end_date').split('T')[0], '%Y-%m-%d')

    lat_min = flask.request.args.get('lat_min')
    lat_max = flask.request.args.get('lat_max')
    lon_min = flask.request.args.get('lon_min')
    lon_max = flask.request.args.get('lon_max')

    ground_stations = flask.request.args.get('ground_stations') # parses a string representation of ground_stations
    ground_stations = literal_eval(ground_stations) # converts into a list representation

    dff = filter_dataframe(df, start_date, end_date, int(lat_min), int(lat_max), int(lon_min), int(lon_max), ground_stations)

    # Making the output csv from the filtered df
    csv_buffer = StringIO()
    dff.to_csv(csv_buffer, index=False)
    output = make_response(csv_buffer.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=summary_data.csv"
    output.headers["Content-type"] = "text/csv"

    return output


# Selectors -> count graph
@app.callback(
    Output("count_graph", "figure"),
    # [Input("visualize-button", "n_clicks")],
    [
        Input("date_picker_range", "start_date"),
        Input("date_picker_range", "end_date"),
        Input("lat_min", "value"),
        Input("lat_max", "value"),
        Input("lon_min", "value"),
        Input("lon_max", "value"),
        Input("ground_station_list", "value"),
    ],
)
def make_count_figure(start_date, end_date, lat_min, lat_max, lon_min, lon_max, ground_stations=None):
    """Create and update the histogram of selected iongograms over the given time range.

    Parameters
    ----------
    start_date : str
        Starting date stored as a str

    end_date : str
        Ending date stored as a str

    lat_min : double
        Minimum value of the latitude stored as a double.
        
    lat_max : double
        Maximum value of the latitude stored as a double.
        
    lon_min : double
        Minimum value of the longitude stored as a double.
        
    lon_max : double
        Maximum value of the longitude stored as a double.

    ground_stations : list
        Ground station name strings stored in a list (e.g. ['Resolute Bay, No. W. Territories'])

    Returns
    -------
    dict
        A dictionary containing 2 key-value pairs: the selected data as an array of dictionaries and the histogram's
        layout as as a Plotly layout graph object.
    """
    start_time = dt.datetime.now()

    start_date = dt.datetime.strptime(start_date.split('T')[0], '%Y-%m-%d')  # Convert strings to datetime objects
    end_date = dt.datetime.strptime(end_date.split('T')[0], '%Y-%m-%d')

    layout_count = copy.deepcopy(layout)

    dff = filter_dataframe(df, start_date, end_date, lat_min, lat_max, lon_min, lon_max, ground_stations)
    g = dff[["file_name", "timestamp"]]
    g.index = g["timestamp"]
    g = g.resample("M").count()

    data = [
        dict(
            type="scatter",
            mode="markers",
            x=g.index,
            y=g['file_name'] / 2,
            name="All Ionograms",
            opacity=0,
            hoverinfo="skip",
        ),
        dict(
            type="bar",
            x=g.index,
            y=g['file_name'],
            name="All Ionograms",
            marker=dict(color="rgb(18, 99, 168)"),
        ),
    ]

    layout_count["title"] = _("Ionograms Per Month")
    layout_count["xaxis"] = {"title": "Date", "automargin": True}
    layout_count["yaxis"] = {"title": _("Number of Ionograms"), "automargin": True}
    layout_count["dragmode"] = "select"
    layout_count["showlegend"] = False
    layout_count["autosize"] = True
    layout_count["transition"] = {'duration': 500}

    figure = dict(data=data, layout=layout_count)

    print(f'make_count_figure: {(dt.datetime.now()-start_time).total_seconds()}')

    return figure


@app.callback(
    Output("selector_map", "figure"),
    # [Input("visualize-button", "n_clicks")],
    [
        Input("date_picker_range", "start_date"),
        Input("date_picker_range", "end_date"),
        Input("lat_min", "value"),
        Input("lat_max", "value"),
        Input("lon_min", "value"),
        Input("lon_max", "value"),
        Input("ground_station_list", "value"),
    ],
)
def generate_geo_map(start_date, end_date, lat_min, lat_max, lon_min, lon_max, ground_stations=None):
    """Create and update the map of ground stations for selected iongograms.

    The size of the ground station marker indicates the number of ionograms from that ground station.

    Parameters
    ----------
    start_date : str
        Starting date stored as a str

    end_date : str
        Ending date stored as a str

    lat_min : double
        Minimum value of the latitude stored as a double.
        
    lat_max : double
        Maximum value of the latitude stored as a double.
        
    lon_min : double
        Minimum value of the longitude stored as a double.
        
    lon_max : double
        Maximum value of the longitude stored as a double.

    ground_stations : list
        Ground station name strings stored in a list (e.g. ['Resolute Bay, No. W. Territories'])

    Returns
    -------
    dict
        A dictionary containing 2 key-value pairs: the selected data as an array of Plotly scattermapbox graph objects
        and the map's layout as a Plotly layout graph object.
    """
    start_time = dt.datetime.now()

    start_date = dt.datetime.strptime(start_date.split('T')[0], '%Y-%m-%d')  # Convert strings to datetime objects
    end_date = dt.datetime.strptime(end_date.split('T')[0], '%Y-%m-%d')

    filtered_data = filter_dataframe(df, start_date, end_date, lat_min, lat_max, lon_min, lon_max, ground_stations)

    traces = []

    for station_details, dfff in filtered_data.groupby(["station_name", "lat", "lon"]):
        trace = dict(
            station_name=station_details[0],
            lat=station_details[1],
            lon=station_details[2],
            count=len(dfff),
        )
        traces.append(trace)
    df_stations = pd.DataFrame(traces)

    stations = []
    if traces != []:

        lat = df_stations["lat"].tolist()
        lon = df_stations["lon"].tolist()
        counts = df_stations["count"].tolist()
        station_names = df_stations["station_name"].tolist()

        # Count mapping from aggregated data
        count_metric_data = {}
        count_metric_data["min"] = df_stations["count"].min()
        count_metric_data["max"] = df_stations["count"].max()
        count_metric_data["mid"] = (count_metric_data["min"] + count_metric_data["max"]) / 2
        count_metric_data["low_mid"] = (
                                               count_metric_data["min"] + count_metric_data["mid"]
                                       ) / 2
        count_metric_data["high_mid"] = (
                                                count_metric_data["mid"] + count_metric_data["max"]
                                        ) / 2

        for i in range(len(df_stations)):
            val = counts[i]
            station_name = station_names[i]

            station = go.Scattermapbox(
                lat=[lat[i]],
                lon=[lon[i]],
                mode="markers",
                marker=dict(
                    color='#1263A8',
                    showscale=False,
                    cmin=count_metric_data["min"],
                    cmax=count_metric_data["max"],
                    size=10
                         * (1 + 2 * (val + count_metric_data["min"]) / count_metric_data["mid"]),
                    colorbar=dict(
                        x=0.9,
                        len=0.7,
                        title=dict(
                            text="Ground Station Overview",
                            font={"color": "#737a8d", "family": "Open Sans"},
                        ),
                        titleside="top",
                        tickmode="array",
                        tickvals=[count_metric_data["min"], count_metric_data["max"]],
                        ticktext=[
                            count_metric_data["min"],
                            count_metric_data["max"],
                        ],
                        ticks="outside",
                        thickness=15,
                        tickfont={"family": "Open Sans", "color": "#737a8d"},
                    ),
                ),
                opacity=0.8,
                #selectedpoints=selected_index,
                selected=dict(marker={"color": "#ffff00"}),
                customdata=[(station_name)],
                hoverinfo="text",
                text=station_name
                     + "<br>No. of Ionograms: "
                     + str(val)
                     + "<br>lat: " + str(lat[i])
                     + "<br>lon: " + str(lon[i])
            )
            stations.append(station)

    else:
        station = go.Scattermapbox(
            lat=[],
            lon=[],
            mode="markers",
            marker=dict(
                color='#1263A8',
                showscale=False,
                size=10,
                colorbar=dict(
                    x=0.9,
                    len=0.7,
                    title=dict(
                        text="No Ground Stations Selected",
                        font={"color": "#737a8d", "family": "Open Sans"},
                    ),
                    titleside="top",
                    tickmode="array",
                    ticks="outside",
                    thickness=15,
                    tickfont={"family": "Open Sans", "color": "#737a8d"},
                ),
            ),
            opacity=0.8,
            selected=dict(marker={"color": "#ffff00"}),
            customdata=[],
            hoverinfo="text",
        )
        stations.append(station)

    layout = go.Layout(
        margin=dict(l=10, r=10, t=20, b=10, pad=5),
        plot_bgcolor="#171b26",
        paper_bgcolor="#171b26",
        clickmode="event+select",
        hovermode="closest",
        showlegend=False,
        legend=go.layout.Legend(
            x=1,
            y=1,
            traceorder="normal",
        ),
        mapbox=go.layout.Mapbox(
            accesstoken=mapbox_access_token,
            #bearing=10,
            #center=go.layout.mapbox.Center(
            #    lat=df_stations.lat.mean(), lon=df_stations.lon.mean()
            #),
            #pitch=5,
            zoom=1,
            style="mapbox://styles/plotlymapbox/cjvppq1jl1ips1co3j12b9hex",
        ),
        transition={'duration': 500},
    )

    print(f'generate_geo_map: {(dt.datetime.now()-start_time).total_seconds()}')

    return {"data": stations, "layout": layout}


# Selectors -> viz chart (95% CI)
@app.callback(
    Output("viz_chart", "figure"),
    # [Input("visualize-button", "n_clicks")],
    [
        Input("date_picker_range", "start_date"),
        Input("date_picker_range", "end_date"),
        Input("x_axis_selection_1", "value"),
        Input("y_axis_selection_1", "value"),
        Input("lat_min", "value"),
        Input("lat_max", "value"),
        Input("lon_min", "value"),
        Input("lon_max", "value"),
        Input("ground_station_list", "value"),
    ],
)
def make_viz_chart(start_date, end_date, x_axis_selection, y_axis_selection, lat_min, lat_max, lon_min, lon_max, ground_stations=None):
    """Create and update the chart for visualizing selected iongograms based on varying x and y-axis selection.

    Displays the mean value from the selected x-axis with a calculated 95% confidence interval, displaying the
    boundaries with a lighter coloured ribbon.

    Parameters
    ----------
    start_date : str
        Starting date stored as a str

    end_date : str
        Ending date stored as a str

    x_axis_selection : string
        The chart's x-axis parameter selected by the dropdown stored as a string (e.g 'timestamp')

    y_axis_selection : string
        The chart's y-axis parameter selected by the dropdown stored as a string (e.g 'max_depth')

    lat_min : double
        Minimum value of the latitude stored as a double.

    lat_max : double
        Maximum value of the latitude stored as a double.

    lon_min : double
        Minimum value of the longitude stored as a double.

    lon_max : double
        Maximum value of the longitude stored as a double.

    ground_stations : list
        Ground station name strings stored in a list (e.g. ['Resolute Bay, No. W. Territories'])

    Returns
    -------
    dict
        A dictionary containing 2 key-value pairs: the selected data as an array of dictionaries and the chart's layout
        as a Plotly layout graph object.
    """
    start_time = dt.datetime.now()

    start_date = dt.datetime.strptime(start_date.split('T')[0], '%Y-%m-%d')  # Convert strings to datetime objects
    end_date = dt.datetime.strptime(end_date.split('T')[0], '%Y-%m-%d')

    dff = filter_dataframe(df, start_date, end_date, lat_min, lat_max, lon_min, lon_max, ground_stations)

    confidence = 0.95

    estimated_means = []
    ci_upper_limits = []
    ci_lower_limits = []
    bins = []

    # bucketing the data
    if x_axis_selection == 'timestamp':
        dff.index = dff["timestamp"]

        index_month = dt.date(dff.index.min().year, dff.index.min().month, 1)
        end_month = dt.date(dff.index.max().year, dff.index.max().month, 1)

        while index_month <= end_month:
            index_month_data = dff[(dff['timestamp'] > pd.Timestamp(index_month))
                                & (dff['timestamp'] < pd.Timestamp(index_month + relativedelta(months=1)))]
                # dff[index_month: index_month + relativedelta(months=1)]

            n = len(index_month_data[y_axis_selection])
            if n == 0:
                estimated_means.append(None)
                ci_upper_limits.append(None)
                ci_lower_limits.append(None)
            else:
                bin_mean = mean(index_month_data[y_axis_selection])
                std_err = sem(index_month_data[y_axis_selection])
                error_range = std_err * t.ppf((1 + confidence) / 2, n - 1)  # t.ppf should be 1.96 given big enough n value

                estimated_means.append(bin_mean)
                ci_upper_limits.append(bin_mean + error_range)
                ci_lower_limits.append(bin_mean - error_range if bin_mean - error_range >= 0 else 0)
                bins.append(index_month)

            index_month += relativedelta(months=1)

    elif x_axis_selection == 'lat' or x_axis_selection == 'lon':
        if x_axis_selection == 'lat':
            step = 5
            index_range = range(-90,90,step)
        if x_axis_selection == 'lon':
            step = 5
            index_range = range(-180, 180, step)


        for i in index_range:
            bin_data = dff[(dff[x_axis_selection] >= i)
                                & (dff[x_axis_selection] < i + step)]
                # dff[index_month: index_month + relativedelta(months=1)]

            n = len(bin_data[y_axis_selection])
            if n == 0:
                estimated_means.append(None)
                ci_upper_limits.append(None)
                ci_lower_limits.append(None)
            else:
                bin_mean = mean(bin_data[y_axis_selection])
                std_err = sem(bin_data[y_axis_selection])
                error_range = std_err * t.ppf((1 + confidence) / 2, n - 1)  # t.ppf should be 1.96 given big enough n value

                estimated_means.append(bin_mean)
                ci_upper_limits.append(bin_mean + error_range)
                ci_lower_limits.append(bin_mean - error_range if bin_mean - error_range >= 0 else 0)
                bins.append(i)

    data = [
        dict(
            #mode="lines",
            name="",
            type="scatter",
            x=bins,
            y=ci_upper_limits,
            #line_color="rgba(255,255,255,0)",
            fillcolor="rgba(255,255,255,0)",
            line={'color': 'rgba(18,99,168,0)'},
            connectgaps=True,
            showlegend=False,
        ),
        dict(
            fill="tonexty",
            mode="none",
            name="95% Confidence Interval",
            type="scatter",
            x=bins,
            y=ci_lower_limits,
            fillcolor="rgba(18,99,168,0.25)",
            #line_color="rgba(255,255,255,0)",
            line={'width': '0px'},
            connectgaps=True,
            showlegend=True,
        ),
        dict(
            type="scatter",
            mode="lines+markers",
            x=bins,
            y=estimated_means,
            name="Estimated Mean",
            line={'color': 'rgb(18,99,168)'},
            marker={'size': 2.5},
            connectgaps=False,
            showlegend=True,
        ),
    ]

    layout = dict(
        autosize=True,
        automargin=True,
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        # legend=dict(font=dict(size=10), orientation="h"),
        title=_("Data Visualization (95% Confidence Interval)"),
        xaxis={"title": x_axis_selection, "automargin": True},
        yaxis={"title": y_axis_selection, "automargin": True},
        height=500,
        transition={'duration': 500},
    )

    figure = dict(data=data, layout=layout)

    print(f'make_viz_chart: {(dt.datetime.now()-start_time).total_seconds()}')

    return figure

# Selectors -> viz map
@app.callback(
    Output("viz_map", "figure"),
    # [Input("visualize-button", "n_clicks")],
    [
        Input("date_picker_range", "start_date"),
        Input("date_picker_range", "end_date"),
        Input("stat_selection", "value"),
        Input("y_axis_selection_2", "value"),
        Input("lat_min", "value"),
        Input("lat_max", "value"),
        Input("lon_min", "value"),
        Input("lon_max", "value"),
        Input("ground_station_list", "value"),
    ],
)
def make_viz_map(start_date, end_date, stat_selection, var_selection, lat_min, lat_max, lon_min, lon_max, ground_stations=None):
    """Create and update a map visualizing the selected ionograms' values for the selected variable by ground station.

    The size of the ground station marker indicates the number of ionograms from that ground station.

    Parameters
    ----------
    start_date : str
        Starting date stored as a str

    end_date : str
        Ending date stored as a str

    stat_selection : string
        The type of average used for the size of the ground station markers stored as a string (e.g 'Mean')

    var_selection : string
        The variable corresponding to the size of the ground station markers on the maps elected by the dropdown stored
        as a string (e.g 'max_depth')

    lat_min : double
        Minimum value of the latitude stored as a double.

    lat_max : double
        Maximum value of the latitude stored as a double.

    lon_min : double
        Minimum value of the longitude stored as a double.

    lon_max : double
        Maximum value of the longitude stored as a double.

    ground_stations : list
        Ground station name strings stored in a list (e.g. ['Resolute Bay, No. W. Territories'])

    Returns
    -------
    dict
        A dictionary containing 2 key-value pairs: the selected data as an array of Plotly scattermapbox graph objects
        and the map's layout as a Plotly layout graph object.
    """
    start_time = dt.datetime.now()

    start_date = dt.datetime.strptime(start_date.split('T')[0], '%Y-%m-%d')  # Convert strings to datetime objects
    end_date = dt.datetime.strptime(end_date.split('T')[0], '%Y-%m-%d')

    filtered_data = filter_dataframe(df, start_date, end_date, lat_min, lat_max, lon_min, lon_max, ground_stations)

    traces = []
    for station_details, dfff in filtered_data.groupby(["station_name", "lat", "lon"]):
        trace = dict(
            station_name=station_details[0],
            lat=station_details[1],
            lon=station_details[2],
            count=len(dfff),
            mean=filtered_data.groupby(["station_name", "lat", "lon"])[var_selection].mean()[station_details[0]][0],
            median=filtered_data.groupby(["station_name", "lat", "lon"])[var_selection].median()[station_details[0]][0]
        )
        traces.append(trace)

    df_stations = pd.DataFrame(traces)

    stations = []
    if traces != []:

        lat = df_stations["lat"].tolist()
        lon = df_stations["lon"].tolist()
        station_names = df_stations["station_name"].tolist()
        if stat_selection == 'mean':
            stat_values = df_stations["mean"].tolist()
        elif stat_selection == 'median':
            stat_values = df_stations["median"].tolist()

        # Count mapping from aggregated data
        stat_metric_data = {}
        stat_metric_data["min"] = df_stations[stat_selection].min()
        stat_metric_data["max"] = df_stations[stat_selection].max()
        stat_metric_data["mid"] = (stat_metric_data["min"] + stat_metric_data["max"]) / 2
        stat_metric_data["low_mid"] = (stat_metric_data["min"] + stat_metric_data["mid"]) / 2
        stat_metric_data["high_mid"] = (stat_metric_data["mid"] + stat_metric_data["max"]) / 2

        for i in range(len(df_stations)):
            val = stat_values[i]
            station_name = station_names[i]

            station = go.Scattermapbox(
                lat=[lat[i]],
                lon=[lon[i]],
                mode="markers",
                marker=dict(
                    color='white',
                    showscale=False,
                    cmin=stat_metric_data["min"],
                    cmax=stat_metric_data["max"],
                    #size=1 + (val - stat_metric_data["min"] / 10),
                    size= 1 + 25 * ((val - stat_metric_data["min"]) + stat_metric_data["min"]) / stat_metric_data["mid"],
                            # 10 + (val - stat_metric_data["min"]) / 15,
                    colorbar=dict(
                        x=0.9,
                        len=0.7,
                        title=dict(
                            text="Ground Station Overview",
                            font={"color": "#737a8d", "family": "Open Sans"},
                        ),
                        titleside="top",
                        tickmode="array",
                        tickvals=[stat_metric_data["min"], stat_metric_data["max"]],
                        ticktext=[
                            stat_metric_data["min"],
                            stat_metric_data["max"],
                        ],
                        ticks="outside",
                        thickness=15,
                        tickfont={"family": "Open Sans", "color": "#737a8d"},
                    ),
                ),
                opacity=0.6,
                #selectedpoints=selected_index,
                selected=dict(marker={"color": "#ffff00"}),
                customdata=[(station_name)],
                hoverinfo="text",
                text=station_name
                + "<br>" + stat_selection + " " + var_selection + ":"
                + str(round(val, 2))
                + "<br>lat: " + str(lat[i])
                + "<br>lon: " + str(lon[i])
            )
            stations.append(station)

    else:
        station = go.Scattermapbox(
            lat=[],
            lon=[],
            mode="markers",
            marker=dict(
                color='#1263A8',
                showscale=False,
                size=0,
                colorbar=dict(
                    x=0.9,
                    len=0.7,
                    title=dict(
                        text="No Ground Stations Selected",
                        font={"color": "#737a8d", "family": "Open Sans"},
                    ),
                    titleside="top",
                    tickmode="array",
                    ticks="outside",
                    thickness=15,
                    tickfont={"family": "Open Sans", "color": "#737a8d"},
                ),
            ),
            opacity=0.8,
            selected=dict(marker={"color": "#ffff00"}),
            customdata=[],
            hoverinfo="text",
        )
        stations.append(station)

    layout = go.Layout(
        margin=dict(l=10, r=10, t=20, b=10, pad=5),
        plot_bgcolor="#171b26",
        paper_bgcolor="#171b26",
        clickmode="event+select",
        hovermode="closest",
        showlegend=False,
        mapbox=go.layout.Mapbox(
            accesstoken=mapbox_access_token,
            #bearing=10,
            #center=go.layout.mapbox.Center(
            #    lat=df_stations.lat.mean(), lon=df_stations.lon.mean()
            #),
            #pitch=5,
            zoom=1,
            style="mapbox://styles/plotlymapbox/cjvppq1jl1ips1co3j12b9hex",
        ),
        height=500,
        transition={'duration': 500},
    )

    print(f'make_viz_map: {(dt.datetime.now()-start_time).total_seconds()}')

    return {"data": stations, "layout": layout}


# Inject the static text here after translating
# The variables in controls.py are placed here; babel does not work for translation unless it is hard coded here, not sure why. Likely has to with the way Dash builds the web app.
@app.callback(
    [
        Output("page-title", "children"),
        Output("learn-more-button", "children"),
        Output("ionograms-ratio", "children"),
        Output("description-1", "children"),
        Output("description-2", "children"),
        Output("select-data", "children"),
        Output("latitude-text", "children"),
        Output("longitude-text", "children"),
        Output("Map_description-1", "children"),
        Output("yearslider-text", "children"),
        Output("groundstations-text", "children"),
        Output("download-button-1", "children"),
        Output("download-button-2", "children"),
        Output("Graph_description-1", "children"),
        Output("x-axis-selection-text", "children"),
        Output("y-axis-selection-text", "children"),
        Output("Graph_description-2", "children"),
        Output("stat-selection-text", "children"),
        Output("stat-y-axis-text", "children"),
        Output("ground_station_list", "options"),
        Output("x_axis_selection_1", "options"),
        Output("y_axis_selection_1", "options"),
        Output("y_axis_selection_2", "options"),
        Output("Map_description-2", "children"),
        Output("stat_selection", "options"),
    ],
        [Input('none', 'children')], # A placeholder to call the translations upon startup
)
def translate_static(x):
    print('Translating...')
    return [
                _("Alouette I Ionogram Data"),
                _("Learn More About Alouette"),
                _("ionograms selected") + " / " + _("total of ionograms"),
                _("Launched in 1962, Alouette I sent signals with different frequencies into the topmost layer of the atmosphere, known as the ionosphere, and collected data on the depth these frequencies travelled. The results of this were sent to ground stations around the world and stored in films as ionogram images, which have now been digitized. The ionograms Alouette I provided were used to fuel hundreds of scientific papers at the time. Although ionosphere data from more recent years is readily available, the data from Alouette I’s ionograms are the only ones available for this time period. Barriers for accessing, interpreting and analyzing the data at a larger scale have prevented this data's usage. "),
                _("This application provides users the ability to select, download and visualize Alouette I's data. Please note that the extracted ionogram parameters, such as max depth and min frequency, are provided primarily for demonstration purposes. These values are subject to error, and should not be directly used in a scientific context."),
                _("Select Data"),
                _("Filter by ground station latitude:"),
                _("Filter by ground station longitude:"),
                _("Map of the world showing ground stations. Each station is represented by a circle, the size of which depends on the number of ionograms at each station."),
                _("Filter by date:"),
                _("Select ground stations:"),
                _('Download Summary Data as CSV'),
                _('Download Selected Ionogram Images'),
                _("Graph showing the number of ionograms captured during each month. The X-axis presents the date and the Y-axis presents the number of ionograms."),
                _("Select x-axis:"),
                _("Select y-axis:"),
                _("Graph visualizing the mean maximum depth over time. The variables can be changed using the dropdown. By default the X-axis represents time while the Y-axis represents mean maximum depth (Km)."),
                _("Select statistic:"),
                _("Select plotted value:"),
                [  # Ground_station_options
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
                    {'label': _('Kashima, Japan'), 'value': 'Kashima, Japan'}
                ],
                [  # x_axis_options
                    {'label': _('Date'), 'value': 'timestamp'},
                    {'label': _('Latitude'), 'value': 'lat'}, {'label': _('Longitude'), 'value': 'lon'}
                ],
                [  # y_axis_options
                    {'label': _('Minimum Frequency'), 'value': 'fmin'},
                    {'label': _('Maximum Depth'), 'value': 'max_depth'}
                ],
                [  # y_axis_selection_2
                    {'label': _('Minimum Frequency'), 'value': 'fmin'},
                    {'label': _('Maximum Depth'), 'value': 'max_depth'}
                ],
                _("Map showing mean maximum depth at each ground station. Each station is represented by a circle, the size of which depends on the mean maximum depth."),
                [  # stat_selection
                    {'label': _('Mean'), 'value': 'mean'},
                    {'label': _('Median'), 'value': 'median'}
                ],

    ]

# Translate the header and the footer by injecting raw HTML
@app.callback(
    [
        Output('gc-header', 'children'),
        Output('gc-footer', 'children')
    ],
    [Input('none2', 'children')]
)
def translate_header_footer(x):
    """ Translates the government header and footer
    """
    try: # On the first load of the webpage, there is a bug where the header won't load due to the session not being established yet. This try/except defaults the header/footer to english
        if session['language'] == 'fr':
            return [dash_dangerously_set_inner_html.DangerouslySetInnerHTML(gc_header_fr), dash_dangerously_set_inner_html.DangerouslySetInnerHTML(gc_footer_fr)]
        else:
            return [dash_dangerously_set_inner_html.DangerouslySetInnerHTML(gc_header_en), dash_dangerously_set_inner_html.DangerouslySetInnerHTML(gc_footer_en)]
    except:
        return [dash_dangerously_set_inner_html.DangerouslySetInnerHTML(gc_header_en), dash_dangerously_set_inner_html.DangerouslySetInnerHTML(gc_footer_en)]


@app.callback(
    [
        Output('language-button', 'children'),
        Output('language-link', 'href'),
    ],
    [Input('none2', 'children')]
)
def update_language_button(x):
    """Updates the button to switch languages
    """

    language = session['language']
    if language == 'fr':
        return 'EN', prefixe+'/language/en'
    else:
        return 'FR', prefixe+'/language/fr'



@babel.localeselector
def get_locale():
    # if the user has set up the language manually it will be stored in the session,
    # so we use the locale from the user settings
    try:
        language = session['language']
    except KeyError:
        language = None
    if language is not None:
        return language
    return 'en'


@app.server.route('/language/<language>')
def set_language(language=None):
    """Sets the session language, then refreshes the page
    """

    session['language'] = language

    return redirect(url_for('/'))


if __name__ == '__main__':
       app.run_server(debug=True, host='0.0.0.0', port=8888)  # For the server
       

