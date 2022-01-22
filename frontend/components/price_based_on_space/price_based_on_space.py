import dash_bootstrap_components as dbc
import dash_daq as daq
from dash import dcc
from dash import html

table_header = [ html.Thead([html.Tr([html.Th("QM"), html.Th("Preis in EUR")])])
]
row2 = html.Tr([html.Td("10"), html.Td("TBA",id="qm10")])
row3 = html.Tr([html.Td("30"), html.Td("TBA",id="qm30")])
row4 = html.Tr([html.Td("50"), html.Td("TBA",id="qm50")])
row5 = html.Tr([html.Td("60"), html.Td("TBA",id="qm60")])
row6 = html.Tr([html.Td("70"), html.Td("TBA",id="qm70")])
table_body = [html.Tbody([row2, row3, row4,row5,row6])]
table = dbc.Table(table_header + table_body, bordered=True)


price_based_on_space =  html.Div([

    dbc.Row(
        html.H5("Vorraussichtliche Kosten nach qm",className="card-title")
    ),
    dbc.Row([
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
        )
    ], style={'margin-bottom': '15px'}),
    dbc.Row([
        table
    ], style={'margin-bottom': '15px'}),
    dbc.Row([
        dcc.Slider(
            id="qm_slider",
            min=10,
            max=300,
            step=1,
            value=70,
            tooltip={"placement": "bottom", "always_visible": True},
            marks={
                10: {'label': '10qm', 'style': {'color': '#77b0b1'}},
                50: {'label': '50qm' , 'style': {'color': '#77b0b1'}},
                100: {'label': '100qm', 'style': {'color': '#77b0b1'}},
                150: {'label': '150qm', 'style': {'color': '#77b0b1'}},
                200: {'label' : '200qm', 'style': {'color': '#77b0b1'}},
                250: {'label': '250qm', 'style': {'color': '#77b0b1'}},
                300: {'label': '300qm', 'style': {'color': '#77b0b1'}}
            }
        )

    ], style={'margin-bottom': '20px'}),
    dbc.Row([
        html.H4(id="prediction_price", style={'color': 'white'})
    ])
])