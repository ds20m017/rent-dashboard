from dash.dependencies import Input, Output;
import pandas as pd;
import requests;
import plotly.express as px;

legal_vars = ["Insgesamt", "Hauseigentum", "Wohnungseigentum", "Gemeindewohnung", "Genossenschaftswohnung",
              "Andere Hauptmiete", "Sonstige"]

def get_price_callback(app,url):
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