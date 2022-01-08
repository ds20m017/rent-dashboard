from flask import Flask
from dash import Dash
from dash import dcc
from dash import html
import dash_daq as daq
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import pickle
import requests
import numpy as np
import os
from dash.dependencies import Input, Output, State

url = os.getenv('URL')

print(url)
server = Flask(__name__)
app = Dash(
    __name__,
    server=server,
    url_base_pathname='/'
)

value_vars=["Österreich", "Burgenland", "Kärnten", "Niederösterreich", "Oberösterreich", "Salzburg", "Steiermark", "Tirol", "Vorarlberg", "Wien"]
legal_vars=["Insgesamt", "Hauseigentum", "Wohnungseigentum", "Gemeindewohnung", "Genossenschaftswohnung", "Andere Hauptmiete", "Sonstige"]


app.layout = html.Div([
    html.Div(
        className="app-header",
        children=[
            html.Div('Österreich Wohnsituation', className="app-header--title")
        ]
    ),
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
                 style={'width': "40%"}
                 ),
            daq.NumericInput(
                id='size',
                min=10,
                max=500,
                value=70
            ),
            html.Div(id='container', children=[]),
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
                 style={'width': "40%"}
                 ),

        dcc.Graph(id='living_space_line', figure={}),
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
                 style={'width': "40%"}
                 ),
            dcc.Graph(id='rooms_line', figure={}),
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

@app.callback(
    Output(component_id='container', component_property='children'),
    [Input(component_id='slct_state3', component_property='value'),
    Input('size', 'value')]  
)
def update_graph(slct_state, size):

    container = "The predicted price is: {}".format(requests.get(url+"/predictPrice?state="+str(slct_state)+"&size="+str(size)).json())
    
    return container

@app.callback(
    Output(component_id='living_space_line', component_property='figure'),
    [Input(component_id='slct_state1', component_property='value')]  
)
def update_graph(slct_state):

    averageSpace = pd.read_json(requests.get(url+'/averageSpace').json())
    df1 = averageSpace.melt(id_vars='Jahr', value_vars=value_vars).copy()
    
    if slct_state != 'Österreich':
        df1 = df1[df1.variable == slct_state]
        
    fig = px.line(df1, 
                  x=df1.Jahr, 
                  y=df1.value,
                  color=df1.variable,
                  title="Average living space"
                 )
    
    fig.update_layout(
                  xaxis_title="Jahr",
                  yaxis_title="Größe",
                legend_title="Bundesland")
    
    return fig

@app.callback(
    Output(component_id='rooms_line', component_property='figure'),
    [Input(component_id='slct_state2', component_property='value')]  
)
def update_graph(slct_state):

    averageRooms = pd.read_json(requests.get(url+'/averageRooms').json())
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

    medianPriceLegal = pd.read_json(requests.get(url+'/medianPriceLegal').json())
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