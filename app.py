# from iposter.server import run_poster
import iposter.components as ip
import dash_html_components as html
import flask
import dash_bootstrap_components as dbc
import os
from random import randint
import dash
from pathlib import Path




server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],server=server,assets_folder= Path(__file__).parent.absolute(),
                    assets_url_path='/',suppress_callback_exceptions=True)

def create_poster():
    # Header Info
    poster_title = html.H1("Research poster title; state the main topic of your study",
                            style={"text-align":"center","font-size":"89px"})
    poster_authors = html.H2("Intern Name1, Researcher Name2, Researcher Name2, Mentor (Primary Investigator) Name2",
                             style={"text-align":"center","font-size":"59px"})
    poster_institutions = html.H3("1University Name, 2Lawrence Berkeley National Laboratory",
                                  style={"text-align":"center","font-size":"48px"})

    #
    abstract = ip.PosterSection(
        title="Abstract",
        children=[html.P(
            "This is some card text",
            style={"font-size":"34px","height":"7in"}),])

    column_0 = ip.PosterColumn(sections=[
        abstract,
        abstract,
        abstract])

    #
    layout = ip.Poster(
        title=poster_title,
        authors=poster_authors,
        institutions=poster_institutions,
        columns=[
        column_0,
        column_0,
        column_0])

    return layout


poster = create_poster()
app.layout = poster


if __name__ == "__main__":
   # server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
    app.server.run(debug=True,threaded=True)

