import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

average_living_space= html.Div([
    dbc.Row(html.H5("Durchschnittliche Wohnfläche")),
    dbc.Row([
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
        dbc.Col(html.Div(id='container', children=[]))
    ], style={'margin-bottom': '5px'}),
    dbc.Row([
        dcc.Graph(id='living_space_line', figure={}),
    ], style={'margin-bottom': '5px'})]
)