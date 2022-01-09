from flask import Flask
from dash import Dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash_daq as daq
import pandas as pd
import plotly.express as px
import requests
import os
from dash.dependencies import Input, Output, State
from components.average_living_space.average_living_space import  average_living_space;
from components.average_living_space.average_living_space_callback import  get_average_living_space_callback;

url = os.getenv('URL')

print(url)
server = Flask(__name__)
app = Dash(
    __name__,
    server=server,
    url_base_pathname='/',
    external_stylesheets=[dbc.themes.CYBORG]
)

value_vars = ["Österreich", "Burgenland", "Kärnten", "Niederösterreich", "Oberösterreich", "Salzburg", "Steiermark",
              "Tirol", "Vorarlberg", "Wien"]
legal_vars = ["Insgesamt", "Hauseigentum", "Wohnungseigentum", "Gemeindewohnung", "Genossenschaftswohnung",
              "Andere Hauptmiete", "Sonstige"]

app.layout = html.Div([dbc.Row(
    html.Div(
        className="app-header",
        children=[
            html.Div('Österreich Wohnsituation', className="app-header--title")
        ]
    ), style={'margin-bottom': '5px'}
    ),
    average_living_space,
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id="slct_state2",
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
                         )
        ], width=4)
    ], style={'margin-bottom': '5px'}),
    dbc.Row([
        dcc.Graph(id='rooms_line', figure={})
    ], style={'margin-bottom': '5px'}),
    dbc.Row([
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
        dcc.Graph(id='legal_line', figure={})
    ])
])


get_average_living_space_callback(app,url);


@app.callback(
    Output(component_id='rooms_line', component_property='figure'),
    [Input(component_id='slct_state2', component_property='value')]
)
def update_graph(slct_state):
    averageRooms = pd.read_json(requests.get(url + '/averageRooms').json())
    df1 = averageRooms.melt(id_vars='Jahr', value_vars=value_vars).copy()

    if slct_state != 'Österreich':
        df1 = df1[df1.variable == slct_state]

    fig = px.line(df1,
                  x=df1.Jahr,
                  y=df1.value,
                  color=df1.variable,
                  title="Average rooms"
                  )

    fig.update_layout(
        xaxis_title="Jahr",
        yaxis_title="Anzahl",
        legend_title="Bundesland")

    return fig


@app.callback(
    Output(component_id='legal_line', component_property='figure'),
    [Input(component_id='slct_legal', component_property='value')]
)
def update_graph(slct_legal):
    medianPriceLegal = pd.read_json(requests.get(url + '/medianPriceLegal').json())
    df1 = medianPriceLegal.melt(id_vars='Jahr', value_vars=legal_vars).copy()

    if slct_legal != 'Insgesamt':
        df1 = df1[df1.variable == slct_legal]

    fig = px.line(df1,
                  x=df1.Jahr,
                  y=df1.value,
                  color=df1.variable,
                  title="Median Price"
                  )

    fig.update_layout(
        xaxis_title="Jahr",
        yaxis_title="Kosten",
        legend_title="Rechtsform")

    return fig


@server.route("/")
def my_dash_app():
    return app.index()


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=5000)