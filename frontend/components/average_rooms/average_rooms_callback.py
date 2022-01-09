from dash.dependencies import Input, Output;
import pandas as pd;
import requests;
import plotly.express as px;

value_vars = ["Österreich", "Burgenland", "Kärnten", "Niederösterreich", "Oberösterreich", "Salzburg", "Steiermark",
              "Tirol", "Vorarlberg", "Wien"]

def get_average_rooms_callback(app,url):
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
