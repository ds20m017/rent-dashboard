from dash.dependencies import Input, Output;
import requests;
from dash import html


def get_price_based_on_space(app,url):
    @app.callback(
        [Output(component_id='qm1', component_property='children'),
         Output(component_id='qm10', component_property='children'),
         Output(component_id='qm30', component_property='children'),
         Output(component_id='qm50', component_property='children'),
         Output(component_id='qm60', component_property='children'),
         Output(component_id='qm70', component_property='children'),],
        [Input(component_id='slct_state3', component_property='value')]
    )
    def update_graph(slct_state):
        qm1= round(requests.get(url + "/predictPrice?state=" + str(slct_state) + "&size=1").json(),2);
        qm10= round(requests.get(url + "/predictPrice?state=" + str(slct_state) + "&size=10").json(),2);
        qm30= round(requests.get(url + "/predictPrice?state=" + str(slct_state) + "&size=30").json(),2);
        qm50=round( requests.get(url + "/predictPrice?state=" + str(slct_state) + "&size=50").json(),2);
        qm60= round(requests.get(url + "/predictPrice?state=" + str(slct_state) + "&size=60").json(),2);
        qm70=round( requests.get(url + "/predictPrice?state=" + str(slct_state) + "&size=70").json(),2);

        return qm1,qm10,qm30,qm50,qm60,qm70;

    @app.callback(
        Output(component_id='prediction_price', component_property='children'),
        [Input(component_id='qm_slider', component_property='value'),
         Input(component_id='slct_state3', component_property='value')]
    )
    def predict(slider,slct_state):
        x= requests.get(url + "/predictPrice?state=" + str(slct_state) + "&size="+str(slider)).json();
        return str(round(x,2))+" EUR"