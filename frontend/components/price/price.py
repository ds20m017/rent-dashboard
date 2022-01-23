import dash_bootstrap_components as dbc;
from dash import dcc
from dash import html

price= html.Div([
                dbc.Row([html.H5("Preisentwicklung")]),
                dbc.Row([
                    dbc.Col(
                    dcc.Dropdown(id="slct_legal",
                                 options=[
                                     {"label": "Hauseigentum", "value": 'Hauseigentum'},
                                     {"label": "Wohnungseigentum", "value": 'Wohnungseigentum'},
                                     {"label": "Gemeindewohnung", "value": 'Gemeindewohnung'},
                                     {"label": "Genossenschaftswohnung", "value": 'Genossenschaftswohnung'},
                                     {"label": "Andere Hauptmiete", "value": 'Andere Hauptmiete'},
                                     {"label": "Sonstige", "value": 'Sonstige'},
                                     {"label": "Insgesamt", "value": 'Insgesamt'}],
                                 multi=False,
                                 value='Insgesamt',
                                 style={'width': "40%"}
                                 ),
                    ),
                ], style={'margin-bottom': '15px'}),
                dbc.Row([
                    dbc.Col(dcc.Graph(id='legal_line', figure={}))
                ], style={'margin-bottom': '5px'})]
                );