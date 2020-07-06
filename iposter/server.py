import dash
from pathlib import Path
import dash_bootstrap_components as dbc

def run_poster(layout):
    app = dash.Dash(__name__,
                    external_stylesheets=[dbc.themes.BOOTSTRAP],
                    assets_folder= Path(__file__).parent.absolute(),
                    assets_url_path='/')
    app.layout = layout
    app.run_server(debug=False, host="0.0.0.0", port="8888")
