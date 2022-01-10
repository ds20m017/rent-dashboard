from dash.dependencies import Input, Output;
import pandas as pd;
import requests;
import geopandas as gpd
import geoplot as gplt
from geopandas import GeoDataFrame
import plotly.express as px;

value_vars = ["Österreich", "Burgenland", "Kärnten", "Niederösterreich", "Oberösterreich", "Salzburg", "Steiermark", "Tirol", "Vorarlberg", "Wien"]
laender = gpd.read_file('components/map/laender_999_geo.json')

def get_map_callback(app,url):
    @app.callback(
        Output(component_id='price_map', component_property='figure'),
        [Input(component_id='slct_year', component_property='value')]
    )
    def update_graph(slct_year):
        averagePrice = pd.read_json(requests.get(url + '/averagePrice').json())
        averagePrice_melt = averagePrice.melt(id_vars='Jahr', value_vars=value_vars).copy()
        averagePrice_melt = averagePrice_melt[averagePrice_melt.Jahr == slct_year]
        gdf = GeoDataFrame(averagePrice_melt[averagePrice_melt.variable != 'Österreich'])
        averagePriceMap = laender.merge(gdf, how='inner', left_on=['name'], right_on=['variable'])
        
        fig = px.choropleth(averagePriceMap, geojson=averagePriceMap.geometry, locations=averagePriceMap.index, color="value")
        fig.update_geos(fitbounds="locations", visible=False)

        return fig