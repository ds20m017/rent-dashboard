from flask import Flask
from dash import Dash
from dash import html
import dash_bootstrap_components as dbc
import os
from components.average_living_space.average_living_space import  average_living_space;
from components.average_living_space.average_living_space_callback import  get_average_living_space_callback;

from components.average_rooms.average_rooms import average_rooms;
from components.average_rooms.average_rooms_callback import  get_average_rooms_callback;

from components.price.pice import price;
from components.price.price_callback import  get_price_callback;


url = os.getenv('URL')

print(url)
server = Flask(__name__)
app = Dash(
    __name__,
    server=server,
    url_base_pathname='/',
    external_stylesheets=[dbc.themes.CYBORG]
)

app.layout = html.Div([dbc.Row(
    html.Div(
        className="app-header",
        children=[
            html.Div('Österreich Wohnsituation', className="app-header--title")
        ]
    ), style={'margin-bottom': '5px'}
    ),
    average_living_space,
    average_rooms,
    price
])

get_average_living_space_callback(app,url);
get_average_rooms_callback(app,url);
get_price_callback(app,url);

@server.route("/")
def my_dash_app():
    return app.index()

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=5000)