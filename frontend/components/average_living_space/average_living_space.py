import dash_bootstrap_components as dbc
import dash_daq as daq
from dash import dcc
from dash import html

average_living_space= html.Div([dbc.Row([
        dbc.Col(
            dcc.Dropdown(id="slct_state3",
                         options=[
                             {"label": "Burgenland", "value": 1},
                             {"label": "Kärnten", "value": 2},
                             {"label": "Niederösterreich", "value": 3},
                             {"label": "Oberösterreich", "value": 4},
                             {"label": "Salzburg", "value": 5},
                             {"label": "Steiermark", "value": 6},
                             {"label": "Tirol", "value": 7},
                             {"label": "Vorarlberg", "value": 8},
                             {"label": "Wien", "value": 9},
                             {"label": "Österreich", "value": 10}],
                         multi=False,
                         value=10,
                         style={'color': 'black'}
                         ), width=2

        ),
        dbc.Col(
            dcc.Dropdown(id="slct_state1",
                         options=[
                             {"label": "Burgenland", "value": 'Burgenland'},
                             {"label": "Kärnten", "value": 'Kärnten'},
                             {"label": "Niederösterreich", "value": 'Niederösterreich'},
                             {"label": "Oberösterreich", "value": 'Oberösterreich'},
                             {"label": "Salzburg", "value": 'Salzburg'},
                             {"label": "Steiermark", "value": 'Steiermark'},
                             {"label": "Tirol", "value": 'Tirol'},
                             {"label": "Vorarlberg", "value": 'Vorarlberg'},
                             {"label": "Wien", "value": 'Wien'},
                             {"label": "Österreich", "value": 'Österreich'}],
                         multi=False,
                         value='Österreich',
                         style={'color': 'black'}
                         ), width=2
        ),
        dbc.Col(
            daq.NumericInput(
                id='size',
                min=10,
                max=500,
                value=70,
                style={'color': 'black'}
            ), width=1
        ),
    ], style={'margin-bottom': '5px'}),
    dbc.Row([
        dbc.Col([html.Div(id='container', children=[])]), ], style={'margin-bottom': '5px'}),
    dbc.Row([
        dcc.Graph(id='living_space_line', figure={}),
    ], style={'margin-bottom': '5px'})]
)