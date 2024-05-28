# -*- coding: utf-8 -*-
import dash
import pathlib
import copy
import configparser
import dash_core_components as dcc
#import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import datetime as dt
from scipy.stats import sem, t
from scipy import mean
from dateutil.relativedelta import relativedelta
from dash.dependencies import Input, Output, State
import dash_table as dst
#from dash_table.Format import Format, Scheme
#import locale
import urllib.parse

from zipfile import ZipFile
import os
from os import path
import flask
from io import StringIO
from flask_babel import _ ,Babel
from flask import session, redirect, url_for


class CustomDash(dash.Dash):

    analytics_code = ''
    lang = ''
    header = ''
    footer = ''
    meta_html = ''
    app_header = ''
    app_footer = ''
    analytics_footer = ''

    def set_analytics(self, code):
        self.analytics_code = code

    def set_analytics_footer(self, code):
        self.analytics_footer = code

    def set_lang(self, lang):
        self.lang = lang

    def set_header(self, header):
        self.header = header

    def set_footer(self, footer):
        self.footer = footer

    def set_meta_tags(self, meta_html):
        self.meta_html = meta_html

    def set_app_header(self, header):
        self.app_header = header

    def set_app_footer(self, footer):
        self.app_footer = footer

    def interpolate_index(self, **kwargs):
        # Inspect the arguments by printing them
        return '''
        <!DOCTYPE html>
        <html lang='{lang}'>
            <head>
                <meta charset="UTF-8" />
                {analytics}
                {metas}
                {favicon}
                <title>
                {title}
                </title>
                <style id='dash_components_css'></style>
                {css}
                {meta}
            </head>
            <body id="wb-cont">
                {header}
                <main property="mainContentOfPage" typeof="WebPageElement" class="container">
                    {app_header}
                    {app_entry}
                    {app_footer}
                </main>
                <div class="global-footer">
                    <footer id="wb-info">
                    {footer}
                    {config}
                    {scripts}
                    {renderer}
                    {analytics_footer}
                    </footer>
                </div>
            </body>
        </html>
        '''.format(
            app_entry=kwargs['app_entry'],
            config=kwargs['config'],
            scripts=kwargs['scripts'],
            renderer=kwargs['renderer'],
            metas = kwargs['metas'],
            favicon = kwargs['favicon'],
            css = kwargs['css'],
            title = kwargs['title'],
            analytics = self.analytics_code,
            analytics_footer = self.analytics_footer,
            meta = self.meta_html,
            lang = self.lang,
            header = self.header,
            footer = self.footer,
            app_header = self.app_header,
            app_footer = self.app_footer
            )

# get relative data folder
PTH = '/home/ckanportal/App-Launcher/'
PATH = pathlib.Path(__file__).parent.absolute()
DATA_PATH = PATH.joinpath("data").resolve()  # path to "data" folder
ASSET_PATH = PATH.joinpath("public").resolve()  # path to "assets" folder

scripts = ASSET_PATH.joinpath("scripts.js").resolve()

external_stylesheets = [
    'https://canada.ca/etc/designs/canada/wet-boew/css/wet-boew.min.css',
    'https://canada.ca/etc/designs/canada/wet-boew/css/theme.min.css',
    'https://use.fontawesome.com/releases/v5.8.1/css/all.css'
    # 'assets/gc_theme_cdn/assets/favicon.ico',
    # 'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
    # 'assets/gc_theme_cdn/css/theme.min.css',
    # 'https://wet-boew.github.io/themes-dist/GCWeb/wet-boew/css/noscript.min.css'
]  # Link to external CSS

external_scripts = [
    # 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.js',
    # 'https://wet-boew.github.io/themes-dist/GCWeb/wet-boew/js/wet-boew.min.js',
    # 'assets/gc_theme_cdn/js/theme.min.js',
    # 'https://cdn.plot.ly/plotly-locale-de-latest.js',
    '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js',
    'https://canada.ca/etc/designs/canada/wet-boew/js/wet-boew.min.js',
    'https://canada.ca/etc/designs/canada/wet-boew/js/theme.min.js',
    'assets/scripts.js'
]

def get_config_dict():
    config = configparser.RawConfigParser()
    config.read(PTH+'config.cfg')
    if not hasattr(get_config_dict, 'config_dict'):
        get_config_dict.config_dict = dict(config.items('TOKENS'))
    return get_config_dict.config_dict

def generate_meta_tag(name, content):
    return "<meta name=\"" + name + "\" content=\"" + content + "\">"

def generate_meta_tag_with_title(name, content, title):
    return "<meta name=\"" + name + "\" title=\"" + title + "\" content=\"" + content + "\">"

if __name__ == '__main__':
    print ('DEBUG: Alouette Main Block used')
    prefixe=""
#   app.run_server(debug=True)  # For development/testing
    from header_footer import gc_header_en, gc_footer_en, gc_header_fr, gc_footer_fr, app_title_en, app_title_fr, app_footer_en, app_footer_fr
    if(path.exists(os.path.dirname(os.path.abspath(__file__)) + r"/analytics.py")):
        from analytics import analytics_code, analytics_footer
    else:
        analytics_code = ''
        analytics_footer = ''
    from .config import Config
    app_config = Config()
    tokens = get_config_dict()

    path_data=app_config.DATA_PATH
    prefixe=app_config.APP_PREFIX

    df = pd.read_csv(PTH+r'applications/alouette/data/final_alouette_data.csv')  # edit for compatibility with CKAN portal (e.g. API to dataframe)

    app = CustomDash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width"}],
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
    )

else :
    prefixe="/alouette"
    print ('Alouette Alternate Block used')
    from .header_footer import gc_header_en, gc_footer_en, gc_header_fr, gc_footer_fr, app_title_en, app_title_fr, app_footer_en, app_footer_fr
    if(path.exists(os.path.dirname(os.path.abspath(__file__)) + r"/analytics.py")):
        from .analytics import analytics_code, analytics_footer
    else:
        analytics_code = ''
        analytics_footer = ''
    from .config import Config
    app_config = Config()

    path_data=app_config.DATA_PATH
    prefixe=app_config.APP_PREFIX

    df = pd.read_csv(PTH+r'applications/alouette/data/final_alouette_data.csv')  # edit for compatibility with CKAN portal (e.g. API to dataframe)
    tokens = get_config_dict()
    app = CustomDash(
        __name__,
        requests_pathname_prefix=prefixe,
        meta_tags=[{"name": "viewport", "content": "width=device-width"}],
        external_stylesheets=external_stylesheets,
        external_scripts=external_scripts,
    )

meta_html = ''
if app_config.DEFAULT_LANGUAGE == 'en':
    app.set_header(gc_header_en)
    app.set_footer(gc_footer_en)
    meta_html += generate_meta_tag(
        'description',
        'Explore ionosphere data from Alouette I, Canada’s first satellite! Launched in 1962, ionograms have shaped the way that we understand the Earth’s upper atmosphere.'
        )
    meta_html += generate_meta_tag('keywords', '')

    meta_html += generate_meta_tag('dcterms.title', 'Alouette: data exploration application for historic ionograms')
    meta_html += generate_meta_tag_with_title('dcterms.language', 'eng', 'ISO639-2')
    meta_html += generate_meta_tag('dcterms.creator', 'Canadian Space Agency')
    meta_html += generate_meta_tag('dcterms.accessRights', '2')
    meta_html += generate_meta_tag('dcterms.service', 'CSA-ASC')

    app.title="Alouette: data exploration application for historic ionograms"
    app.set_app_header(app_title_en)
    app.set_app_footer(app_footer_en)
else:
    app.set_header(gc_header_fr)
    app.set_footer(gc_footer_fr)
    meta_html += generate_meta_tag(
        'description',
        "Explorer les données ionosphériques d’Alouette I, le premier satellite Canadien! Lancé en 1962, les ionogrammes ont grandement influencé notre compréhension de la haute atmosphère terrestre."
        )
    meta_html += generate_meta_tag('keywords', '')

    meta_html += generate_meta_tag('dcterms.title', 'Alouette: application d’exploration des données d’ionogrammes historiques ')
    meta_html += generate_meta_tag_with_title('dcterms.language', 'fra', 'ISO639-2')
    meta_html += generate_meta_tag('dcterms.creator', 'Agence spatiale canadienne')
    meta_html += generate_meta_tag('dcterms.accessRights', '2')
    meta_html += generate_meta_tag('dcterms.service', 'CSA-ASC')

    app.title="Alouette: application d’exploration des données d’ionogrammes historiques "
    app.set_app_header(app_title_fr)
    app.set_app_footer(app_footer_fr)

app.set_meta_tags(meta_html)
app.set_analytics(analytics_code)
app.set_analytics_footer(analytics_footer)
app.set_lang(app_config.DEFAULT_LANGUAGE)
app.title="Alouette: application d’exploration des données d’ionogrammes historiques | data exploration application for historic ionograms"
server = app.server
server.config['SECRET_KEY'] = tokens['secret_key']  # Setting up secret key to access flask session
babel = Babel(server)  # Hook flask-babel to the app

# try:
#     language = session['language']
# except KeyError:
#     language = 'en'



#IONOGRAM_PATH = 'U:/Storage'  # Directory to Ionogram images for testing
IONOGRAM_PATH = '/storage/ftp_root/users/OpenData_DonneesOuvertes/pub/AlouetteData/Alouette Data'  # Directory to Ionogram images for testing
MAX_IONOGRAM = 100
# IONOGRAM_PATH = '/storage_slow/ftp_root/users/OpenData_DonneesOuvertes/pub/AlouetteData/Alouette Data'  # Directory to Ionogram images on server

# load data and transform as needed
#dtypes = {'': 'int', 'file_name': 'str', 'max_depth': 'float', 'decimal_value': 'str'}

# print(session['language'])

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
    {'label': _('Minimum frequency'), 'value': ('fmin')},
    {'label': _('Maximum depth'), 'value': ('max_depth')}]

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


# converts the timestamp to date_time objects
df['timestamp'] = pd.to_datetime(df['timestamp'])

df['lat'] = df.apply(lambda x: coords_to_float(x['lat']), axis=1)
df['lon'] = df.apply(lambda x: coords_to_float(x['lon']), axis=1)

# Create global chart template
mapbox_access_token = tokens['alouette_mapbox_token']

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


# Builds the layout and components for the inputs to filter the data, as well as the ionograms/month graph and the ground stations map
def build_filtering():
    return html.Div([
        html.Div(
            [
                html.Div(
                    [
                        html.H2(id="ionograms_text",style = {"margin-top": "3.5em"}),
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
                                dcc.Markdown(id="description-1"),
                                dcc.Markdown(id="description-2"),
                                dcc.Markdown(id="github-link")
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
                        html.Section(
                            [
                                html.H2(
                                    id='error_header'
                                ),
                                html.Ul(
                                    id='form_errors'
                                )
                            ],
                            id='filter_errors',
                            hidden=True,
                            className='alert alert-danger'
                        ),
                        html.Div(
                            [
                            html.Div(
                                [
                                    html.P(
                                        id="latitude-text",
                                        className="control_label",
                                    ),
                                    html.Div([
                                        html.Label(
                                            id="lat_min-text",
                                            htmlFor = "lat_min",
                                            hidden = True
                                        ),
                                        html.Div([
                                            html.Div(
                                                id="lat_alert",
                                                hidden=True,
                                                className='label label-danger'
                                            ),
                                        ]),
                                        dcc.Input(
                                            id="lat_min",
                                            type='number',
                                            value=-90.0,
                                            placeholder="Min Latitude",
                                            min=-90.0,
                                            max=90.0,
                                            step=5,
                                        ),
                                        html.Label(
                                            id="lat_max-text",
                                            htmlFor = "lat_max",
                                            hidden = True
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
                                        )
                                    ]
                                ),
                                html.Div(children=html.P(id="lat_selection"),className="wb-inv")
                                ],
                                className="col-md-6"
                            ),
                            html.Div(
                                [
                                    html.P(
                                        id="longitude-text",
                                        className="control_label",
                                    ),
                                    html.Div([
                                        html.Label(
                                            id = "lon_min-text",
                                            htmlFor = "lon_min",
                                            hidden = True
                                        ),
                                        html.Div([
                                            html.Div(
                                                id="lon_alert",
                                                hidden=True,
                                                className='label label-danger'
                                            ),
                                        ]),
                                        dcc.Input(
                                            id="lon_min",
                                            type='number',
                                            value=-180.0,
                                            placeholder="Min Longitude",
                                            min=-180.0,
                                            max=180.0,
                                            step=5,
                                            style={"margin-left": "5px"}
                                        ),
                                        html.Label(
                                            id = "lon_max-text",
                                            htmlFor = "lon_max",
                                            hidden = True
                                        ),
                                        dcc.Input(
                                            id="lon_max",
                                            type='number',
                                            value=180.0,
                                            placeholder="Max Longitude",
                                            min=-180.0,
                                            max=180.0,
                                            step=5,
                                            style={"margin-left": "5px"}
                                        )
                                    ]),
                                html.Div(children=html.P(id="lon_selection"),className="wb-inv")],
                                className="col-md-6"
                            ),
                            ],
                            className='row'
                        ),
                        html.Div(
                            [
                                html.Div([
                                    html.Div( id="date_alert", className='label label-danger' ),
                                ]),
                                html.P(
                                    id="yearslider-text",
                                    className="control_label",
                                ),
                                html.Div([
                                    dcc.DatePickerRange(
                                        id='date_picker_range',
                                        min_date_allowed=dt.datetime(1962, 9, 29),
                                        max_date_allowed=dt.datetime(1972, 12, 31),
                                        #initial_visible_month=dt.datetime(1962, 9, 29),
                                        start_date=dt.datetime(1962, 9, 29),
                                        end_date=dt.datetime(1972, 12, 31),
                                        start_date_placeholder_text='Select start date',
                                        end_date_placeholder_text='Select end date',
                                        display_format="Y-MM-DD",
                                        style={"margin-top": "5px"}
                                    ),
                                    html.Div(id='output-container-date-picker-range'),
                                html.Div(children=html.P(id="date_selection"),className="wb-inv")]),
                            ],
                            id="cross-filter-options",
                            className="",
                        ),
                        html.Div(
                            [
                                html.Div([
                                    html.P(
                                        id="groundstations-text",
                                        className="control_label",
                                    ),
                                    html.Div(
                                        [
                                            html.Label(
                                                id="groundstations-label-text",
                                                htmlFor="ground_station_list_dropdown",
                                                className="control_label",
                                                hidden = True
                                            ),
                                            dcc.Dropdown(
                                                id="ground_station_list",
                                                options=[],
                                                placeholder=_("Sélectionner | Select"),
                                                multi=True,
                                                value=station_values,
                                                className="dcc_control",
                                                label = 'Label test'
                                            ),
                                        ],
                                        className="drop_down col-md-6",
                                        role="listbox",
                                        **{'aria-label': 'Select plotted value'}
                                    ),
                                    html.Div(children=html.P(id="ground_station_selection"),className="wb-inv")]),

                            ],
                            id="map-options",
                            className="",
                        ),
                        
                        html.Div(
                            [
                                html.Div ([html.P("[Alouette/ISIS - Label]")]),
                                html.P("[Alouette/ISIS] - Dropdownlist")
                            ],                       
                        ),                        
                        
                        html.Div(
                            [
                            html.Div(
                                [
                                    html.A(
                                        html.Span(id='download-button-1', n_clicks=0, style={'padding': '0px 10px'}),
                                        id='download-link-1',
                                        # download='rawdata.csv',
                                        href="",
                                        target="_blank",
                                        className="btn btn-primary"
                                    ),
                                ],
                                className="col-md-6"
                            ),
                            html.Div(
                                [
                                    html.A(
                                        html.Span(id='download-button-2',  n_clicks=0, style={'padding': '0px 10px'}),
                                        id='download-link-2',
                                        style={"margin-left": "5px"},
                                        className="btn btn-primary"
                                    ),
                                ],
                                className="col-md-6"
                            ),
                            ],
                            className='row'
                        ),
                        html.Div(children=html.P(id="download_selection"),className="wb-inv"),
                        html.Div ([html.P(id="Download_limit")]),
                    ],
                    className="map-filters"
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [dcc.Graph(
                                        id="selector_map",
                                        className="csa-graph",
                                        config={
                                            "displaylogo": False,
                                            "displayModeBar" : False
                                        },
                                    ),
                                    detail_table("geo_table","geo_table_text")],
                                ),
                            html.P(id="Map_description-1"),
                            ],

                            id="left-column-1",
                            style={"flex-grow": 1},
                            className="col-md-6",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        dcc.Graph(
                                            id="count_graph",
                                            className="csa-graph",
                                            config={
                                                "displaylogo": False,
                                                "displayModeBar": False
                                            }
                                        ),
                                        detail_table("count_table","count_table_text")
                                    ],
                                    id="countGraphContainer",
                                ),
                            html.Div ([html.P(id="Graph_description-1")]),
                            ],
                            id="right-column-1",
                            style={"flex-grow": 1},
                            className="col-md-6",
                        ),
                    ],
                ),
            ],
            className="pretty_container twelve columns",
            style={"justify-content": "space-evenly"}
        ),

    ])

def detail_table(id, id2):
    #next button pagnation, for some reason the pages are 0 indexed but the dispalyed page isn't
    @app.callback(
        [
            Output( id, 'page_current'),
            Output( id+'-btn-1-a', 'data-value'),
            Output( id+'-btn-2-a', 'data-value'),
            Output( id+'-btn-3-a', 'data-value'),
            Output( id+'-btn-1-a', "children"),
            Output( id+'-btn-2-a', "children"),
            Output( id+'-btn-3-a', "children"),
            Output( id+'-btn-1-a', "aria-label"),
            Output( id+'-btn-2-a', "aria-label"),
            Output( id+'-btn-3-a', "aria-label"),
            Output( id+'-btn-1-a', "aria-current"),
            Output( id+'-btn-2-a', "aria-current"),
            Output( id+'-btn-3-a', "aria-current"),
            Output( id+'-btn-1', "className"),
            Output( id+'-btn-2', "className"),
            Output( id+'-btn-prev-a', 'children'),
            Output( id+'-btn-next-a', 'children'),
            Output( id+'-btn-prev-a', "aria-label"),
            Output( id+'-btn-next-a', "aria-label"),
            Output( id+'-navigation', "aria-label"),
        ],
        [
            Input( id+'-btn-prev', 'n_clicks'),
            Input( id+'-btn-1', 'n_clicks'),
            Input( id+'-btn-2', 'n_clicks'),
            Input( id+'-btn-3', 'n_clicks'),
            Input( id+'-btn-next', 'n_clicks')
        ],
        [
            State( id, 'page_current'),
            State( id+'-btn-1-a', 'data-value'),
            State( id+'-btn-2-a', 'data-value'),
            State( id+'-btn-3-a', 'data-value'),
        ]
    )
    
    def update_table_next(btn_prev, btn_1, btn_2, btn_3, btn_next, curr_page, btn1_value, btn2_value, btn3_value):
        
        session['language'] = app_config.DEFAULT_LANGUAGE
        ctx = dash.callback_context
        btn1_current = 'false'
        btn2_current = 'false'
        btn3_current = 'false'

        btn1_class = ''
        btn2_class = ''

        btn1_aria = ''
        btn2_aria = ''
        btn3_aria = ''

        if ctx.triggered:
            # curr_page = curr_page + 1
            #print(ctx.triggered)
            if ctx.triggered[0]['prop_id'] == id+'-btn-next.n_clicks':
                curr_page += 1
            if ctx.triggered[0]['prop_id'] == id+'-btn-1.n_clicks':
                curr_page = btn1_value
            if ctx.triggered[0]['prop_id'] == id+'-btn-2.n_clicks':
                curr_page = btn2_value
            if ctx.triggered[0]['prop_id'] == id+'-btn-3.n_clicks':
                curr_page = btn3_value
            if ctx.triggered[0]['prop_id'] == id+'-btn-prev.n_clicks':
                curr_page -= 1

            if curr_page < 0:
                curr_page = 0

        aria_prefix = _('Goto page ')

        if curr_page < 1:
            btn1_value = curr_page
            btn2_value = curr_page+1
            btn3_value = curr_page+2
            btn1_current = 'true'
            btn1_class = 'active'
            btn1_aria = aria_prefix + str(btn1_value+1) + ', ' + _('Current Page')
            btn2_aria = aria_prefix + str(btn2_value+1)
            btn3_aria = aria_prefix + str(btn3_value+1)
        else:
            btn1_value = curr_page -1
            btn2_value = curr_page
            btn3_value = curr_page + 1
            btn2_current = 'true'
            btn2_class = 'active'
            btn1_aria = aria_prefix + str(btn1_value+1)
            btn2_aria = aria_prefix + str(btn2_value+1) + ', ' + _('Current Page')
            btn3_aria = aria_prefix + str(btn3_value+1)

        return [
            curr_page,
            btn1_value,
            btn2_value,
            btn3_value,
            btn1_value+1,
            btn2_value+1,
            btn3_value+1,
            btn1_aria,
            btn2_aria,
            btn3_aria,
            btn1_current,
            btn2_current,
            btn3_current,
            btn1_class,
            btn2_class,
            _('Previous'),
            _('Next'),
            _('Goto Previous Page'),
            _('Goto Next Page'),
            _('Pagination Navigation')
        ]

    return html.Div([
        html.Details(
            [
                html.Summary(id=id2),
                html.Div(
                    dst.DataTable(
                        id=id,
                        page_size= 10,
                        page_current = 0
                    ),
                    style={"margin":"4rem"}
                ),
                html.Nav(
                    html.Ul(
                        [
                            html.Li(
                                html.A(
                                    _('Previous'),
                                    id=id+'-btn-prev-a',
                                    className='page-prev',
                                    **{'aria-label': _('Goto Previous Page'), 'data-value': -1}
                                ),
                                id=id+'-btn-prev',
                                n_clicks=0,
                                tabIndex=0
                            ),
                            html.Li(
                                html.A(
                                    '1',
                                    id=id+'-btn-1-a',
                                    **{'aria-label': _("Goto page 1, Current Page"), 'aria-current': _('true'), 'data-value': 0}
                                ),
                                id=id+'-btn-1',
                                n_clicks=0,
                                tabIndex=0
                            ),
                            html.Li(
                                html.A(
                                    '2',
                                    id=id+'-btn-2-a',
                                    **{'aria-label': _('Goto page 2'), 'data-value': 1}
                                ),
                                className='active',
                                id=id+'-btn-2',
                                n_clicks=0,
                                tabIndex=0
                            ),
                            html.Li(
                                html.A(
                                    '3',
                                    id=id+'-btn-3-a',
                                    **{'aria-label': _('Goto page 3'), 'data-value': 2}
                                ),
                                id=id+'-btn-3',
                                n_clicks=0,
                                tabIndex=0
                            ),
                            html.Li(
                                html.A(
                                    'Next',
                                    id=id+'-btn-next-a',
                                    className='page-next',
                                    **{'aria-label': _('Goto Next Page'), 'data-value': -2}
                                ),
                                id=id+'-btn-next',
                                n_clicks=0,
                                tabIndex=0
                            )
                        ],
                        className = 'pagination'
                    ),
                    **{'aria-label': _('Pagination Navigation')},
                    role = _('navigation'),
                    className = 'table_pagination',
                    id = id+'-navigation'
                )
            ]
        )
    ])

# Builds the layout for the map displaying statistics as well as the confidence interval graph
def build_stats():
    return html.Div([
        html.Div(
            [
                html.Div(
                    [
                        html.Div ([html.P(id="Map_description-2")]),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Label(
                                            htmlFor='x_axis_selection_1_dropdown',
                                            id="x-axis-selection-text",
                                            className="control_label",
                                        ),
                                        dcc.Dropdown(
                                            id="x_axis_selection_1",
                                            options=x_axis_options,
                                            multi=False,
                                            value='timestamp',
                                            className="dcc_control",
                                            label = 'Label test'
                                        ),
                                    ],
                                    className="drop_down col-md-6",
                                    role="listbox",
                                    style={'max-width': '400px'},
                                    **{'aria-label': 'Select x-axis'}
                                ),
                                html.Div(
                                    [
                                    html.Label(
                                        htmlFor='y_axis_selection_1_dropdown',
                                        id="y-axis-selection-text",
                                        className="control_label",
                                    ),
                                    dcc.Dropdown(
                                        id="y_axis_selection_1",
                                        options=y_axis_options,
                                        multi=False,
                                        value='max_depth',
                                        className="dcc_control",
                                        label = 'Label test'
                                    ),
                                    ],
                                    className="drop_down col-md-6",
                                    role="listbox",
                                    style={'max-width': '400px'},
                                    **{'aria-label': 'Select y-axis'}
                                ),
                            ],
                            className="row",
                            id="viz-chart-options",
                        ),
                    ],
                    id="right-column-3",
                    className="row",
                    style={"margin-bottom": "20px"}
                ),
                html.Div(
                    [
                        html.Div(
                            [dcc.Graph(id="viz_chart",
                                       config={
                                           "displaylogo": False,
                                           "displayModeBar": False
                                       }
                                       ),
                             detail_table("viz_table","viz_table_text")],
                            id="vizChartContainer",
                            #className="pretty_container",
                        ),
                    ],
                    id="left-column-3",
                    className="row",
                ),
            ],
            className="row pretty_container",
            #style={"height": "500px"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div ([html.P(id="Graph_description-2")]),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Label(
                                            htmlFor="stat_selection_dropdown",
                                            id="stat-selection-text",
                                            className="control_label",
                                        ),
                                        dcc.Dropdown(
                                            id="stat_selection",
                                            options=[
                                                {'label': 'Mean', 'value': 'mean'},
                                                {'label': 'Median', 'value': 'median'}
                                            ],
                                            multi=False,
                                            value='mean',
                                            className="dcc_control",
                                            label = 'Label test'
                                        ),
                                    ],
                                    className="drop_down col-md-6",
                                    role="listbox",
                                    style={'max-width': '400px'},
                                    **{'aria-label': 'Select Statistic'}
                                ),
                                html.Div(
                                    [
                                        html.Label(
                                            htmlFor="y_axis_selection_2_dropdown",
                                            id="stat-y-axis-text",
                                            className="control_label",
                                        ),
                                        dcc.Dropdown(
                                            id="y_axis_selection_2",
                                            options=y_axis_options,
                                            multi=False,
                                            value='max_depth',
                                            className="dcc_control",
                                            label = 'Label test'
                                        ),
                                    ],
                                    className="drop_down col-md-6",
                                    role="listbox",
                                    style={'max-width': '400px'},
                                    **{'aria-label': 'Select plotted value'}
                                ),
                            ],
                            className="row",
                            id="map-viz-options",
                        ),
                    ],
                    id="right-column-4",
                    className="row",
                    style={"margin-bottom": "20px"}
                ),
                html.Div(
                    [
                        html.Div(
                            [dcc.Graph(id="viz_map",
                                       config={
                                           "displaylogo": False,
                                           "displayModeBar": False
                                       }
                                       ),
                             detail_table("viz_map_table","viz_map_table_text")],
                            id="vizGraphContainer",
                        ),
                    ],
                    id="left-column-4",
                    className="row",
                ),
            ],
            className="row pretty_container",
            #style={"height": "500px"},
        ),
        html.Div(id='none', children=[], style={'display': 'none'}), # Placeholder element to trigger translations upon page load
    ])

#     '''
# Create app layout
app.layout = html.Div(
    [
        html.Div([""], id='gc-header'),
        html.Div(
            [
                dcc.Store(id="aggregate_data"),
                html.Div(id="output-clientside"),  # empty Div to trigger javascript file for graph resizing

                # build_header(),
                build_filtering(),
                build_stats(),
            ],
            id="mainContainer",
            style={"display": "flex", "flex-direction": "column", "margin": "auto", "width":"95%"},
            role='main',
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
    
    #print('\nDEBUG: entering filter_dataframe()')
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
    
    #print(f'DEBUG: end of filter_dataframe() - TOTAL Time spent (s): {(dt.datetime.now()-start_time).total_seconds()}')
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
    
    start_date = dt.datetime.strptime(start_date.split('T')[0], '%Y-%m-%d')  # Convert strings to datetime objects
    end_date = dt.datetime.strptime(end_date.split('T')[0], '%Y-%m-%d')

    dff = filter_dataframe(df, start_date, end_date, lat_min, lat_max, lon_min, lon_max, ground_stations)
    return "{:n}".format(dff.shape[0]) + " / " + "{:n}".format(699360)


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

@app.callback(
    Output("lat_alert", "hidden"),[
        Input("lat_min", "value"),
        Input("lat_max", "value"),
    ]
)

def form_lat_validation(lat_min,lat_max):
    return lat_validation(lat_min,lat_max)

def lat_validation(lat_min,lat_max):
    try:
        s = ((lat_min < lat_max) and (lat_min >= -90) and (lat_max <= 90))
    except TypeError:
        s = False
    return s

@app.callback(
    Output("lon_alert", "hidden"),[
        Input("lon_min", "value"),
        Input("lon_max", "value"),
    ]
)
def form_lon_validation(lon_min,lon_max):
    return lon_validation(lon_min,lon_max)

def lon_validation(lon_min,lon_max):
    try:
        s = ((lon_min < lon_max) and (lon_min >= -180) and (lon_max <= 180))
    except TypeError:
        s = False
    return s

@app.callback(
    [
        Output("filter_errors", "hidden"),
        Output("form_errors", 'children'),
        Output("error_header", 'children')
    ],
    [
        Input('lat_min','value'),
        Input('lat_max','value'),
        Input('lon_min','value'),
        Input('lon_max','value'),
        Input("date_picker_range", "start_date"),
        Input("date_picker_range", "end_date")
    ],
)
def update_error_list(lat_min,lat_max,lon_min,lon_max, start_date, end_date):
    
    s = False
    errors = []
    if not lon_validation(lon_min, lon_max) or not lat_validation(lat_min, lat_max):
        if not lat_validation(lat_min, lat_max):
            errors.append(
                html.Li(
                    html.A(
                        _("Invalid values provided. Latitude values must be between -90 and 90. Minimum values must be smaller than maximum values. All values must be round numbers that are multiples of 5."),
                        href="#lat_alert"
                    )
                )
            )
        if not lon_validation(lon_min, lon_max):
            errors.append(
                html.Li(
                    html.A(
                        _("Invalid values provided. Longitude values must be between -180 and 180. Minimum values must be smaller than maximum values. All values must be round numbers that are multiples of 5."),
                        href="#lon_alert"
                    )
                )
            )
        if not date_validation(start_date,end_date):
            errors.append(
                html.Li(
                    html.A(
                        _("Invalid dates provided. Dates must be between 29/09/1962 (Sep. 29th 1962) and 31/12/1972 (Dec. 31st 1972)."),
                        href="#date_alert"
                    )
                )
            )
    else:
        s = True
    
    return [
        s,
        errors,
        _('The form could not be submitted because errors were found.')
    ]

# @app.callback(
#     Output("pos_alert", "is_open"),
#     [   Input("lat_min", "value"),
#         Input("lat_max", "value"),
#         Input("lon_min", "value"),
#         Input("lon_max", "value"),
#     ],
#     [
#         State("pos_alert", "is_open")
#     ],
# )
def pos_validation(lat_min,lat_max,lon_min,lon_max, is_open):
    try:
        s = not ((lat_min < lat_max) and (lat_min >= -90) and (lat_max <= 90) and (lon_min < lon_max) and (lon_min >= -180) and (lon_max <= 180))
    except TypeError:
        s = True
    return s

@app.callback(
    Output("date_alert", "hidden"),
    [   Input("date_picker_range", "start_date"),
        Input("date_picker_range", "end_date")
    ]
)
def form_date_validation(start_date, end_date):
    return date_validation(start_date, end_date)

def date_validation(start_date, end_date):
    try:
        start = dt.datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S')
        end = dt.datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        start = dt.datetime.strptime(start_date, '%Y-%m-%d')
        end = dt.datetime.strptime(end_date, '%Y-%m-%d')
    MIN_DATE=dt.datetime(1962, 9, 29)
    MAX_DATE=dt.datetime(1972, 12, 31)
    return ((start>=MIN_DATE) and (start <= end) and (start <= MAX_DATE) and (end >= MIN_DATE) and (end <= MAX_DATE))

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

    # link = prefixe+'/dash/downloadImages?start_date={}&end_date={}&lat_min={}&lat_max={}&lon_min={}&lon_max={}&ground_stations={}'\
    #     .format(start_date, end_date, lat_min, lat_max, lon_min, lon_max, ground_stations)
    values = {
        'start_date': start_date,
        'end_date': end_date,
        'lat_min': lat_min,
        'lat_max': lat_max,
        'lon_min': lon_min,
        'lon_max': lon_max,
        'ground_stations': ground_stations
    }

    link = prefixe + '/dash/downloadImages?' + urllib.parse.urlencode(values)
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
    max_download = MAX_IONOGRAM  # Temporary limit on number of ionograms that can be downloaded
    with ZipFile(memory_file, 'w') as zf:
        for index, row in dff.iterrows():
            if os.path.exists(row['file_path']) and max_download > 0:
                max_download -= 1
                zf.write(row['file_path'], arcname=row['file_name']+'.png')  # Write each image into the zip

        # Making the output csv from the filtered df
        csv_buffer = StringIO()
        dff.to_csv(csv_buffer, index=False)
        language = app_config.DEFAULT_LANGUAGE
        if language == 'fr':
            fn = "Metadata_des_ionogrammes_séléctionnés.csv"
        else:
            fn = 'Metadata_of_selected_ionograms.csv'
        zf.writestr(fn, csv_buffer.getvalue())

    memory_file.seek(0)
    language = app_config.DEFAULT_LANGUAGE
    if language == 'fr':
        fn = "Ionogrammes.zip"
    else:
        fn = "Ionograms.zip"
    return flask.send_file(memory_file, attachment_filename=fn, as_attachment=True)


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

    # link = '/dash/downloadCSV?start_date={}&end_date={}&lat_min={}&lat_max={}&lon_min={}&lon_max={}&ground_stations={}' \
    #         .format(start_date, end_date, lat_min, lat_max, lon_min, lon_max, ground_stations)
    values = {
        'start_date': start_date,
        'end_date': end_date,
        'lat_min': lat_min,
        'lat_max': lat_max,
        'lon_min': lon_min,
        'lon_max': lon_max,
        'ground_stations': ground_stations
    }

    link = prefixe + '/dash/downloadCSV?' + urllib.parse.urlencode(values)
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
    
    language = app_config.DEFAULT_LANGUAGE

    start_date = dt.datetime.strptime(flask.request.args.get('start_date').split('T')[0], '%Y-%m-%d')  # Convert strings to datetime objects
    end_date = dt.datetime.strptime(flask.request.args.get('end_date').split('T')[0], '%Y-%m-%d')

    lat_min = flask.request.args.get('lat_min')
    lat_max = flask.request.args.get('lat_max')
    lon_min = flask.request.args.get('lon_min')
    lon_max = flask.request.args.get('lon_max')

    ground_stations = flask.request.args.get('ground_stations') # parses a string representation of ground_stations
    ground_stations = literal_eval(ground_stations) # converts into a list representation

    dff = filter_dataframe(df, start_date, end_date, int(lat_min), int(lat_max), int(lon_min), int(lon_max), ground_stations)

    if language == 'fr':
        dff.columns = [
            'ID',
            'Nom du fichier',
            'Fréquence minimale',
            'Profondeur maximale',
            'Nom du sous-répertoire',
            'Numéro du satellite',
            'Numéro du station au sol',
            'Horodatage',
            'Nom du station au sol',
            'Code du station au sol',
            'Latitude',
            'Longitude'
        ]
    else:
        dff.columns = [
            'ID',
            'File name',
            'Minimum frequency',
            'Maximum depth',
            'Subdirectory name',
            'Satellite number',
            'Ground station number',
            'Timestamp',
            'Ground station name',
            'Ground station code',
            'Latitude',
            'Longitude'
        ]

    # Making the output csv from the filtered df
    csv_buffer = StringIO()
    dff.to_csv(csv_buffer, index=False)
    output = make_response(csv_buffer.getvalue())
    if language == 'fr':
        output.headers["Content-Disposition"] = "attachment; filename=résumé_données.csv"
        filter_dataframe
    else:
        output.headers["Content-Disposition"] = "attachment; filename=summary_data.csv"
    output.headers["Content-type"] = "text/csv"
    return output


# Selectors -> count graph
@app.callback(
    [
        Output("count_graph", "figure"),
        Output("count_table", "columns"),
        Output("count_table", "data")
    ],
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
            name=_("All Ionograms"),
            opacity=0,
            hoverinfo="skip",
        ),
        dict(
            type="bar",
            x=g.index,
            y=g['file_name'],
            name=_("All Ionograms"),
            marker=dict(color="rgb(18, 99, 168)"),
        ),
    ]

    layout_count["title"] = _("Ionograms per month")
    layout_count["xaxis"] = {"title": "Date", "automargin": True}
    layout_count["yaxis"] = {"title": _("Number of ionograms"), "automargin": True}
    layout_count["dragmode"] = "select"
    layout_count["showlegend"] = False
    layout_count["autosize"] = True
    layout_count["transition"] = {'duration': 500}

    figure = dict(data=data, layout=layout_count)

    g["timestamp"]=g.index.strftime("%Y-%m-%d")
    table_data = g.to_dict('records')
    columns = [{"name":_("Date"), "id":"timestamp"},{"name":_("Count"),"id":"file_name"}]

    return [figure, columns, table_data]


@app.callback(
    [
        Output("selector_map", "figure"),
        Output("geo_table", "columns"),
        Output("geo_table", "data"),
    ],
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
    start_date = dt.datetime.strptime(start_date.split('T')[0], '%Y-%m-%d')  # Convert strings to datetime objects
    end_date = dt.datetime.strptime(end_date.split('T')[0], '%Y-%m-%d')

    filtered_data = filter_dataframe(df, start_date, end_date, lat_min, lat_max, lon_min, lon_max, ground_stations)

    traces = []
    table_data = []
    grouped_data = filtered_data.groupby(["station_name", "lat", "lon"])
    for station_details, dfff in grouped_data:
        template = {"station":"","lat":"","long":"","count":""}
        template["station"] = station_details[0]
        template["lat"] = station_details[1]
        template["long"] = station_details[2]
        template["count"] = len(dfff)
        table_data.append(template)
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
                     + _("<br>No. of Ionograms: ")
                     + str(val)
                     + _("<br>Latitude: ") + str(lat[i]) + "°"
                     + _("<br>Longitude: ") + str(lon[i]) + "°"
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

    columns = [{"name":_("Ground station"), "id":"station"},{"name":_("Latitude"),"id":"lat"},{"name":_("Longitude"),"id":"long"},{"name":_("Ionograms count"),"id":"count"}]
    return [{"data": stations, "layout": layout}, columns, table_data]


# Selectors -> viz chart (95% CI)
@app.callback(
    [
        Output("viz_chart", "figure"),
        Output("viz_table", "columns"),
        Output("viz_table", "data"),
    ],
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
    """Create and update the chart for visualizing selected ionograms based on varying x and y-axis selection.

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

    language = get_locale()
    if language == 'en':
        confidence_interval = "95\u0025 confidence interval"
    else:
        confidence_interval = "Intervalle de confiance de 95%"
    start_date = dt.datetime.strptime(start_date.split('T')[0], '%Y-%m-%d')  # Convert strings to datetime objects
    end_date = dt.datetime.strptime(end_date.split('T')[0], '%Y-%m-%d')

    dff = filter_dataframe(df, start_date, end_date, lat_min, lat_max, lon_min, lon_max, ground_stations)

    confidence = 0.95

    estimated_means = []
    ci_upper_limits = []
    ci_lower_limits = []
    bins = []
    title=""
    
    # bucketing the data
    if x_axis_selection == 'timestamp':
        dff.index = dff["timestamp"]
        title=_("Date")
        index_month = dt.date(int(dff.index.min().year), int(dff.index.min().month), 1)
        end_month = dt.date(int(dff.index.max().year), int(dff.index.max().month), 1)

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
            title=_("Latitude (°)")
            step = 5
            index_range = range(-90,90,step)
        if x_axis_selection == 'lon':
            title=_("Longitude (°)")
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
            name=confidence_interval,
            # name=_("95% confidence interval"),
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
            name=_("Estimated mean"),
            line={'color': 'rgb(18,99,168)'},
            marker={'size': 2.5},
            connectgaps=False,
            showlegend=True,
        ),
    ]

    table_data = []
    for i in range(0,len(bins)):
        template = {"bin":"","lw_conf":"","mean":"","up_conf":""}
        template["bin"] = bins[i]
        if ci_lower_limits[i]!=None:
            template["lw_conf"] = "%.3f" % ci_lower_limits[i]
        else:
            template["lw_conf"] = ci_lower_limits[i]
        if ci_upper_limits[i]!=None:
            template["up_conf"] = "%.3f" % ci_upper_limits[i]
        else:
            template["up_conf"] = ci_upper_limits[i]
        if estimated_means[i]!=None:
            template["mean"] = "%.3f" % estimated_means[i]
        else:
            template["mean"] = estimated_means[i]
        table_data.append(template)

    #Set x-axis label dynamically
    if x_axis_selection == 'lat':
        x_label = _("Latitude")
    elif x_axis_selection == 'lon':
        x_label = _("Longitude")
    elif x_axis_selection == 'timestamp':
        x_label = _("Date")

    # Set y-axis label dynamically
    if y_axis_selection == 'max_depth':
        y_label = _("Maximum depth [km]")
        lw_conf = _("Min. confidence interval of max. depth (km)")
        mean_name = _("Mean maximum depth (km)")
        up_conf = _("Max. confidence interval of max. depth (km)")
    elif y_axis_selection == 'fmin':
        y_label = _("Minimum frequency [MHz]")
        lw_conf = _("Min. confidence interval of min. frequency (MHz)")
        mean_name = _("Mean minimum frequency (MHz)")
        up_conf = _("Max. confidence interval of min. frequency (MHz)")

    columns = [{"name":title, "id":"bin"},{"name":lw_conf,"id":"lw_conf"},{"name":mean_name,"id":"mean"},{"name":up_conf,"id":"up_conf"}]

    layout = dict(
        autosize=True,
        automargin=True,
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        # legend=dict(font=dict(size=10), orientation="h"),
        title=_("Data visualization (95 percent confidence interval)"),
        xaxis={"title": x_label, "automargin": True},
        yaxis={"title": y_label, "automargin": True},
        height=500,
        transition={'duration': 500},
    )

    figure = dict(data=data, layout=layout)
    return [figure, columns, table_data]

# Selectors -> viz map
@app.callback(
    [
        Output("viz_map", "figure"),
        Output("viz_map_table", "columns"),
        Output("viz_map_table", "data"),
    ],
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

    start_date = dt.datetime.strptime(start_date.split('T')[0], '%Y-%m-%d')  # Convert strings to datetime objects
    end_date = dt.datetime.strptime(end_date.split('T')[0], '%Y-%m-%d')

    filtered_data = filter_dataframe(df, start_date, end_date, lat_min, lat_max, lon_min, lon_max, ground_stations)

    traces = []
    table_data = []
    
    grouped_data = filtered_data.groupby(["station_name", "lat", "lon"])
    means = grouped_data[var_selection].mean()
    medians = grouped_data[var_selection].median()
    for station_details, dfff in grouped_data:
        template = {"station":"","lat":"","long":"","count":"", "mean":"", "median":""}
        template["station"] = station_details[0]
        template["lat"] = station_details[1]
        template["long"] = station_details[2]
        template["count"] = len(dfff)
        template["mean"] =   "%.2f" % means[station_details[0]][0]
        template["median"] = "%.2f" % medians[station_details[0]][0]
        table_data.append(template)
        trace = dict(
            station_name=station_details[0],
            lat=station_details[1],
            lon=station_details[2],
            count=len(dfff),
            mean=means[station_details[0]][0],
            median=medians[station_details[0]][0]
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
            stat_label = _("Mean")
        elif stat_selection == 'median':
            stat_values = df_stations["median"].tolist()
            stat_label = _("Median")

        #Set labels for frequency/depth
        if var_selection == 'fmin':
            var_label = _("Minimum Frequency")
            var_label_2 = _("minimum frequency")
            var_unit = "MHz"
        elif var_selection == 'max_depth':
            var_label = _("Maximum depth")
            var_label_2 = _("maximum depth")
            var_unit = "km"

        columns = [{"name":_("Ground station"),"id":"station"}, {"name":_("Latitude (°)"),"id":"lat"},{"name":_("Longitude (°)"), "id":"long"}, {"name":stat_label+" - "+var_label_2+" ("+var_unit+")","id":stat_selection}]
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
                + "<br>" + stat_label + ", " + var_label + ": "
                + str(round(val, 2)) + " " + var_unit + " "
                + _("<br>Latitude: ") + str(lat[i]) + "°"
                + _("<br>Longitude: ") + str(lon[i]) + "°"
            )
            stations.append(station)

    else:
        columns = []
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

    return [{"data": stations, "layout": layout}, columns, table_data]


# Inject the static text here after translating
# The variables in controls.py are placed here; babel does not work for translation unless it is hard coded here, not sure why. Likely has to with the way Dash builds the web app.
@app.callback(
    [
        Output("ionograms-ratio", "children"),
        Output("description-1", "children"),
        Output("description-2", "children"),
        Output("github-link", "children"),
        Output("select-data", "children"),
        Output("lat_alert", "children"),
        Output("lon_alert", "children"),
        Output("date_alert", "children"),
        Output("ground_station_selection", "children"),
        Output("lat_selection", "children"),
        Output("lon_selection", "children"),
        Output("date_selection", "children"),
        Output("download_selection", "children"),
        Output("latitude-text", "children"),
        Output("lat_min-text", "children"),
        Output("lat_max-text", "children"),
        Output("longitude-text", "children"),
        Output("lon_min-text", "children"),
        Output("lon_max-text", "children"),
        Output("Map_description-1", "children"),
        Output("yearslider-text", "children"),
        Output("groundstations-text", "children"),
        Output("download-button-1", "children"),
        Output("download-button-2", "children"),
        Output("Graph_description-1", "children"),
        Output("Download_limit", "children"),
        Output("x-axis-selection-text", "children"),
        Output("y-axis-selection-text", "children"),
        Output("Graph_description-2", "children"),
        Output("stat-selection-text", "children"),
        Output("stat-y-axis-text", "children"),
        Output("date_picker_range", "start_date_placeholder_text"),
        Output("date_picker_range", "end_date_placeholder_text"),
        Output("ground_station_list", "options"),
        Output("x_axis_selection_1", "options"),
        Output("y_axis_selection_1", "options"),
        Output("y_axis_selection_2", "options"),
        Output("Map_description-2", "children"),
        Output("stat_selection", "options"),
        Output("count_table_text", "children"),
        Output("geo_table_text","children"),
        Output("viz_table_text","children"),
        Output("viz_map_table_text","children"),
    ],
        [Input('none', 'children')], # A placeholder to call the translations upon startup
)

def translate_static(x):

    return [
                _("Ionograms selected") + " / " + _("Total number of ionograms"),
                _("Launched in 1962, Alouette I scientific satellite marked Canada's entry into the space age and was seen by many as initiating the most progressive space program of that era. Launched in 1969 and 1971, Canada's International Satellites for Ionospheric Studies (ISIS) satellites were used to study the ionosphere and the aurora borealis. ISIS satellites sent radio waves of different frequencies into the topmost layer of the atmosphere, known as the ionosphere, and collected data on the depth of penetration of these waves. The results of this were sent to ground stations around the world and stored on films, a portion of which have now been digitized. These data were used to fuel hundreds of scientific papers at the time. Although ionosphere data derived from inversions and this dataset are readily available, the raw data from ionograms allow for further studies due to scientific advancements since they were acquired. In the past, accessing this data was difficult, which limited its use, interpretation, and analysis on a larger scale."),
                _("This application provides users the ability to select, download and visualize ionogram data. Please note that the metadata and parameters extracted from the ionogram images ([see more about the extraction process](https://github.com/asc-csa/Alouette_extract)) are provided primarily for demonstration purposes. These values are subject to error, and should not be directly used in a scientific context."),
                _("Visit our GitHub page to learn more about the [code used to make this application](https://github.com/asc-csa/AlouetteApp) and the [code used to extract metadata and parameters from the ionogram images](https://github.com/asc-csa/Alouette_extract). The dataset can also be accessed in [CSA's Open Government Portal](https://data.asc-csa.gc.ca/en/dataset/221c1c75-4c42-4286-a4ce-ca6c3027b7fe)"),
                _("Select data"),
                _("Invalid values provided. Latitude values must be between -90 and 90. Minimum values must be smaller than maximum values. All values must be round numbers that are multiples of 5."),
                _("Invalid values provided. Longitude values must be between -180 and 180. Minimum values must be smaller than maximum values. All values must be round numbers that are multiples of 5."),
                _("Invalid dates provided. Dates must be between 29/09/1962 (Sep. 29th 1962) and 31/12/1972 (Dec. 31st 1972)."),
                _("Selection of the ground stations"),
                _("Selection of the range of latitude "),
                _("Selection of the range of longitude"),
                _("Date selection"),
                _("Download the selected dataset"),
                _("Filter by ground station latitude:"),
                _("Minimum latitude"),
                _("Maximum latitude"),
                _("Filter by ground station longitude:"),
                _("Minimum longitude"),
                _("Maximum longitude"),
                _("Map of the world showing ground stations. Each station is represented by a circle, the size of which depends on the number of ionograms at each station."),
                _("Filter by date:"),
                _("Select ground stations:"),
                _('Download summary data as CSV'),
                _('Download selected ionogram images'),
                _("Graph showing the number of ionograms captured during each month. The X-axis indicates the date and the Y-axis indicates the number of ionograms."),
                _("The ionogram images download is currently limited to ")+str(MAX_IONOGRAM)+_(" images at a time."),
                _("Select x-axis:"),
                _("Select y-axis:"),
                _("Map showing either minimum frequency or maximum depth values at each ground station. Each station is represented by a circle, the size of which depends on either the mean or median values of the variables selected. Explore the data by selecting different variables in the drop-down menu on the right."),
                _("Select statistic:"),
                _("Select plotted value:"),
                _("Select start date"),
                _("Select end date"),
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
                    {'label': _('Minimum frequency'), 'value': 'fmin'},
                    {'label': _('Maximum depth'), 'value': 'max_depth'}
                ],
                [  # y_axis_selection_2
                    {'label': _('Minimum frequency'), 'value': 'fmin'},
                    {'label': _('Maximum depth'), 'value': 'max_depth'}
                ],
                _("Graph showing either the mean minimum frequency or mean maximum depth values as a function of either date, longitude, or latitude. Explore the data by selecting different variables in the drop-down menu on the right."),
                [  # stat_selection
                    {'label': _('Mean'), 'value': 'mean'},
                    {'label': _('Median'), 'value': 'median'}
                ],
                _("Text version - Monthly ionograms count"),
                _("Text version - Geographical ionograms count"),
                _("Text version - Data visualization (95 percent confidence interval)"),
                _("Text version - Geographical visualization"),
    ]
# # Translate the header and the footer by injecting raw HTML
# @app.callback(
#     [
#         Output('gc-header', 'children'),
#         Output('gc-footer', 'children')
#     ],
#     [Input('none2', 'children')]
# )
# def translate_header_footer(x):
#     """ Translates the government header and footer
#     """
#     try: # On the first load of the webpage, there is a bug where the header won't load due to the session not being established yet. This try/except defaults the header/footer to english
#         if session['language'] == 'fr':
#             return [dash_dangerously_set_inner_html.DangerouslySetInnerHTML(gc_header_fr), dash_dangerously_set_inner_html.DangerouslySetInnerHTML(gc_footer_fr)]
#         else:
#             return [dash_dangerously_set_inner_html.DangerouslySetInnerHTML(gc_header_en), dash_dangerously_set_inner_html.DangerouslySetInnerHTML(gc_footer_en)]
#     except:
#         return [dash_dangerously_set_inner_html.DangerouslySetInnerHTML(gc_header_en), dash_dangerously_set_inner_html.DangerouslySetInnerHTML(gc_footer_en)]


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
    language = app_config.DEFAULT_LANGUAGE
    if language == 'fr':
        return 'EN', prefixe+'/language/en'
    else:
        return 'FR', prefixe+'/language/fr'


@babel.localeselector
def get_locale():
    # if the user has set up the language manually it will be stored in the session,
    # so we use the locale from the user settings
    language = app_config.DEFAULT_LANGUAGE
    return language


@app.server.route('/language/<language>')
def set_language(language=None):
    """Sets the session language, then refreshes the page
    """

    session['language'] = app_config.DEFAULT_LANGUAGE
    return redirect(url_for('/'))


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8888)  # For the server

print('Alouette loaded.')