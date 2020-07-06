import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

def PosterSection(title,children=[]):
    layout = dbc.Row(
    dbc.Card([
        dbc.Card([
            html.H4(title,style={"color":"white","text-align":"center","font-size":"66px"}),
        ],style={"background":"#0033cc","padding":"20px"}),
        dbc.Card(children,style={"padding":"20px"})],
        body=True),style={"padding-bottom":"25px"})
    return layout

def PosterColumn(sections):
    layout = dbc.Col(
    dbc.Card(
    sections,
    body=True,
    style={"padding":"45px"}))
    return layout

def Header(title, authors, institutions):
    layout = dbc.Card(
    dbc.Row(
    [dbc.Col(html.Img(src="logo1.png", style={'height':'2in', "width":"4in","padding-left":"20px"}),width=1.5),
     dbc.Col([
        dbc.Row(dbc.Container(title,fluid=True)),
        dbc.Row(dbc.Container(authors,fluid=True)),
        dbc.Row(dbc.Container(institutions,fluid=True)),
        ],style={"padding-top":"25px"}),
     dbc.Col(html.Img(src="logo2.png", style={'height':'2in', "width":"4in"}),style={"display":"flex","justify-content":"flex-end","padding-right":"80px"},width=1.5)],
    style={'height':'4in', "width":"42in"},justify="center"),
    body=True)
    return layout

def Poster(title, authors, institutions, columns):
    layout = html.Div(
    dbc.Col([
        dbc.Row(Header(title, authors, institutions), style={"padding":"15px"}),
        dbc.DropdownMenuItem(divider=True),
        dbc.Row(columns)]),
    style={"background": "#e6eeff", "height": "36in", "width": "42in"})

    return layout
