from dash.dependencies import Input, Output;
import pandas as pd;
import requests;
import plotly.express as px;


value_vars = ["Österreich", "Burgenland", "Kärnten", "Niederösterreich", "Oberösterreich", "Salzburg", "Steiermark",
              "Tirol", "Vorarlberg", "Wien"]

def get_average_living_space_callback(app,url):
    @app.callback(
        Output(component_id='living_space_line', component_property='figure'),
        [Input(component_id='slct_state1', component_property='value')]
    )
    def update_graph(slct_state):
        averageSpace = pd.read_json(requests.get(url + '/averageSpace').json())
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

