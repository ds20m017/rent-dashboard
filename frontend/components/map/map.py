import dash_bootstrap_components as dbc;
from dash import dcc
from dash import html

map= html.Div([
                dbc.Row([html.H5("Preisentwicklung Heatmap")]),
                dbc.Row([
                    dbc.Col(
                    dcc.Dropdown(id="slct_year",
                                 options=[
                                     {"label": "2005", "value": 2005},
                                     {"label": "2006", "value": 2006},
                                     {"label": "2007", "value": 2007},
                                     {"label": "2008", "value": 2008},
                                     {"label": "2009", "value": 2009},
                                     {"label": "2010", "value": 2010},
                                     {"label": "2011", "value": 2011},
                                     {"label": "2012", "value": 2012},
                                     {"label": "2013", "value": 2013},
                                     {"label": "2014", "value": 2014},
                                     {"label": "2015", "value": 2015},
                                     {"label": "2016", "value": 2016},
                                     {"label": "2017", "value": 2017},
                                     {"label": "2018", "value": 2018},
                                     {"label": "2019", "value": 2019},
                                     {"label": "2020", "value": 2020}],
                                 multi=False,
                                 value=2020,
                                 style={'width': "40%"}
                                 ),
                    ),
                ], style={'margin-bottom': '5px'}),
                dbc.Row([
                    dbc.Col(dcc.Graph(id='price_map', figure={}))
                ], style={'margin-bottom': '5px'})]
                );