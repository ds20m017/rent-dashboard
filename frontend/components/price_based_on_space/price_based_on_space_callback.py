from dash.dependencies import Input, Output;
import requests;


def get_price_based_on_space(app,url):
    @app.callback(
         [Output(component_id='qm10', component_property='children'),
         Output(component_id='qm30', component_property='children'),
         Output(component_id='qm50', component_property='children'),
         Output(component_id='qm70', component_property='children'),
         Output(component_id='qm90', component_property='children'),
         Output(component_id='qm110', component_property='children'),
         Output(component_id='qm130', component_property='children'),
         Output(component_id='qm150', component_property='children'),
         Output(component_id='qm170', component_property='children'),
         Output(component_id='qmo10', component_property='children'),
         Output(component_id='qmo30', component_property='children'),
         Output(component_id='qmo50', component_property='children'),
         Output(component_id='qmo70', component_property='children'),
         Output(component_id='qmo90', component_property='children'),
         Output(component_id='qmo110', component_property='children'),
         Output(component_id='qmo130', component_property='children'),
         Output(component_id='qmo150', component_property='children'),
         Output(component_id='qmo170', component_property='children'),],
        [Input(component_id='slct_state3', component_property='value')]
    )
    def update_graph(slct_state):
        qm10 = round(requests.get(url + "/predictPrice?state=" + str(slct_state) + "&size=10").json(),2);
        qm30 = round(requests.get(url + "/predictPrice?state=" + str(slct_state) + "&size=30").json(),2);
        qm50 = round( requests.get(url + "/predictPrice?state=" + str(slct_state) + "&size=50").json(),2);
        qm70 = round(requests.get(url + "/predictPrice?state=" + str(slct_state) + "&size=70").json(),2);
        qm90 = round( requests.get(url + "/predictPrice?state=" + str(slct_state) + "&size=90").json(),2);
        qm110 = round( requests.get(url + "/predictPrice?state=" + str(slct_state) + "&size=110").json(),2);
        qm130 = round(requests.get(url + "/predictPrice?state=" + str(slct_state) + "&size=130").json(),2);
        qm150 = round( requests.get(url + "/predictPrice?state=" + str(slct_state) + "&size=150").json(),2);
        qm170 = round( requests.get(url + "/predictPrice?state=" + str(slct_state) + "&size=170").json(),2);
        
        qmo10 = round(requests.get(url + "/predictOperatingCost?state=" + str(slct_state) + "&size=10").json(),2);
        qmo30 = round(requests.get(url + "/predictOperatingCost?state=" + str(slct_state) + "&size=30").json(),2);
        qmo50 = round(requests.get(url + "/predictOperatingCost?state=" + str(slct_state) + "&size=50").json(),2);
        qmo70 = round(requests.get(url + "/predictOperatingCost?state=" + str(slct_state) + "&size=70").json(),2);
        qmo90 = round(requests.get(url + "/predictOperatingCost?state=" + str(slct_state) + "&size=90").json(),2);
        qmo110 = round(requests.get(url + "/predictOperatingCost?state=" + str(slct_state) + "&size=110").json(),2);
        qmo130 = round(requests.get(url + "/predictOperatingCost?state=" + str(slct_state) + "&size=130").json(),2);
        qmo150 = round(requests.get(url + "/predictOperatingCost?state=" + str(slct_state) + "&size=150").json(),2);
        qmo170 = round(requests.get(url + "/predictOperatingCost?state=" + str(slct_state) + "&size=170").json(),2);

        return qm10,qm30,qm50,qm70,qm90,qm110,qm130,qm150,qm170, qmo10,qmo30,qmo50,qmo70,qmo90,qmo110,qmo130,qmo150,qmo170;

    @app.callback(
        Output(component_id='prediction_price', component_property='children'),
        [Input(component_id='qm_slider', component_property='value'),
         Input(component_id='slct_state3', component_property='value')]
    )
    def predict(slider,slct_state):
        x = requests.get(url + "/predictPrice?state=" + str(slct_state) + "&size="+str(slider)).json();
        y = requests.get(url + "/predictOperatingCost?state=" + str(slct_state) + "&size="+str(slider)).json();
        return str(round(x,2))+" + " + str(round(y,2))+ " = " + str(round(x + y,2)) + " €"