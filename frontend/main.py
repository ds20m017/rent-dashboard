from flask import Flask
from dash import Dash
from dash import html
import dash_bootstrap_components as dbc
import geopandas as gpd
import geoplot as gplt
import os
import plotly.express as px

from components.average_living_space.average_living_space import  average_living_space;
from components.average_living_space.average_living_space_callback import  get_average_living_space_callback;

from components.average_rooms.average_rooms import average_rooms;
from components.average_rooms.average_rooms_callback import  get_average_rooms_callback;

from components.price.price import price;
from components.price.price_callback import  get_price_callback;

from components.price_based_on_space.price_based_on_space import price_based_on_space;
from components.price_based_on_space.price_based_on_space_callback import get_price_based_on_space;

from components.map.map import map;
from components.map.map_callback import  get_map_callback;


url = os.getenv('URL')
#url = 'http://127.0.0.1:80'

print(url)
server = Flask(__name__)
app = Dash(
    __name__,
    server=server,
    url_base_pathname='/',
    external_stylesheets=[dbc.themes.CYBORG]
)

app.layout = html.Div([

    dbc.Row(
        html.Div(
            className="app-header",
            children=[
                html.Div('Wohnsituation Österreich', className="app-header--title")
            ]
        ), style={'margin-bottom': '5px'}
    ),
    dbc.Row([
        dbc.Col([dbc.Row([map]), dbc.Row([price])],width=9),
        dbc.Col(price_based_on_space,width=3)
    ], style={'margin-bottom': '15px'}),
    dbc.Row([
        dbc.Col(average_living_space),
        dbc.Col(average_rooms)
    ], style={'margin-bottom':'15px'}),
], style={'margin-left': '15px','margin-right': '15px'})

get_average_living_space_callback(app,url);
get_average_rooms_callback(app,url);
get_price_callback(app,url);
get_price_based_on_space(app,url);
get_map_callback(app,url);

@server.route("/")
def my_dash_app():
    return app.index()

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=5000)