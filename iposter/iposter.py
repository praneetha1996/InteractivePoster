import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

#--
def PosterSection(title, color, children=[], height=None):
    style = {"padding-bottom":"25px"}
    if height: style["height"] = height
    layout = dbc.Row(
    dbc.Card([
        dbc.Card([
            html.H4(title,style={"color":"white","text-align":"center","font-size":"66px"}),
        ],style={"background":color,"padding":"20px"}),
        dbc.Card(dbc.Container(children,fluid=True),style={"padding":"20px"})],
        body=True),style=style)
    return layout

#--
def PosterColumn(sections):
    layout = dbc.Col(
    dbc.Card(
    sections,
    body=True,
    style={"padding":"45px"}))
    return layout

#--
def Header(title, authors, institutions, logo, banner_color):
    layout = dbc.Card(
    dbc.Row(
    [dbc.Col([dbc.Row(html.Img(src=logo, style={'height':'3.5in', "width":"3.5in","padding-left":"100px"}))],width=1.5),
     dbc.Col([dbc.Row(html.Img(src="logo1.png", style={'height':'1.75in', "width":"5in","padding-left":"50px"})),
              dbc.Row(html.Img(src="logo2.png", style={'height':'1.75in', "width":"5in", "padding-left":"50px"}))],width=1.5),
     dbc.Col([
        dbc.Row(dbc.Container(title,fluid=True)),
        dbc.Row(dbc.Container(authors,fluid=True)),
        dbc.Row(dbc.Container(institutions,fluid=True)),
        ],style={"padding-top":"25px"}),
     dbc.Col(html.Img(src="qrcode.png", style={'height':'4in', "width":"4in"}),style={"display":"flex","justify-content":"flex-end","padding-right":"80px"},width=1.5)],
    style={'height':'4in', "width":"42in"},justify="center"),
    style={"background": banner_color},
    body=True)
    return layout

#-
def Poster(title, authors, institutions, logo, columns, bg_color, banner_color):
    layout = html.Div(
    dbc.Col([
        dbc.Row(Header(title, authors, institutions, logo, banner_color), style={"padding":"15px"}),
        dbc.DropdownMenuItem(divider=True),
        dbc.Row(columns)], style={"height": "32in"}),
    style={"background": bg_color, "height": "36in", "width": "42in"})

    return layout

#-
class iPoster:

    #--
    def __init__(self, title, authors_dict, logo, banner_color="#0033cc", text_color="white"):
        self.poster_title = title
        self.authors = authors_dict
        self.logo= logo
        self.bg_color = "#e6eeff"
        self.banner_color = banner_color
        self.text_color = text_color
        self.sects = []
        self.cols = []
        self.figure_counter = 0

    #--
    
    def _header_components(self):
    	index_dict = dict([(x[1], x[0]+1) for x in enumerate(set(reversed(sum(list(self.authors.values()), []))))])
    	authors = []
    	for a in self.authors:
        	authors += [a]
        	authors += [html.Sup(",".join([str(index_dict[x]) for x in self.authors[a]]))]
        	authors += [", "]
    	authors = authors[:-1]
    	insts = []
    	for s in index_dict:
        	insts += [html.Sup(index_dict[s])]
        	insts += [s]
        	insts += [", "]
    	insts = insts[:-1]
    	title = html.H1(self.poster_title, style={"text-align":"center","font-size":"89px","color":self.text_color, "font-family": "Arial", "font-weight":"bold"})
    	authors = html.H2(authors,style={"text-align":"center","font-size":"59px","color":self.text_color, "font-family": "Arial", "font-weight":"bold"})
    	institutions = html.H3(insts, style={"text-align":"center","font-size":"48px","color":self.text_color, "font-family": "Arial", "font-weight":"bold"})
    	return title, authors, institutions
    #--
    def add_section(self, title, text=None, img=None,img1=None, img2=None, img3=None, plot=None, pyLDA=None,pyLDA2=None,pyLDA3=None, color="#0033cc", height=None, children=[]):
        childs = []
        if text: childs.append(html.P(text, style={"font-size":"34px"}))
        if img:
            childs.append(html.Img(src=img["filename"], style={"height":img["height"], "width":img["width"]}))
            self.figure_counter += 1
            childs.append(html.P("Figure {}. ".format(self.figure_counter), style={"font-size":"28px", "font-weight":"bold"}))
            childs.append(html.P(img["caption"], style={"font-size":"28px"}))
        if img1:
            childs.append(html.Img(src=img1["filename"], style={"height":img1["height"], "width":img1["width"], "margin-left": "auto", "margin-right": "auto", "display": "block"}))
            self.figure_counter += 1
            childs.append(html.P("Figure {}. ".format(self.figure_counter) + img1["caption"], style={"font-family": "Georgia","font-size":"24px", "font-weight":"normal", "text-align":"center"}))
        if img2:
            childs.append(html.Img(src=img2["filename"], style={"height":img2["height"], "width":img2["width"], "margin-left": "auto", "margin-right": "auto", "display": "block"}))
            self.figure_counter += 1
            childs.append(html.P("Figure {}. ".format(self.figure_counter) + img2["caption"], style={"font-family": "Georgia", "font-size":"24px", "font-weight":"normal", "text-align":"center"}))
        if img3:
            childs.append(html.Img(src=img3["filename"], style={"height":img3["height"], "width":img3["width"], "margin-left": "auto", "margin-right": "auto", "display": "block"}))
            self.figure_counter += 1
            childs.append(html.P("Figure {}. ".format(self.figure_counter) + img3["caption"], style={"font-family": "Georgia", "font-size":"24px", "font-weight":"normal", "text-align":"center"}))
        if plot:
            childs.append(dcc.Graph(figure=plot["fig"]))
            self.figure_counter += 1
            childs.append(html.P("Figure {}. ".format(self.figure_counter), style={"font-size":"28px", "font-weight":"bold"}))
            childs.append(html.P(plot["caption"], style={"font-size":"28px"}))
        if pyLDA:
            childs.append(html.Iframe(src=pyLDA["filename"], style={"height":pyLDA["height"], "width":pyLDA["width"]}))
            self.figure_counter += 1
            childs.append(html.P("Figure {}. ".format(self.figure_counter) + pyLDA["caption"], style={"font-family": "Georgia", "font-size":"24px", "font-weight":"normal", "text-align":"center"}))
        if pyLDA2:
            childs.append(html.Iframe(src=pyLDA2["filename"], style={"height":pyLDA["height"], "width":pyLDA["width"]}))
            self.figure_counter += 1
            childs.append(html.P("Figure {}. ".format(self.figure_counter) + pyLDA["caption"], style={"font-family": "Georgia", "font-size":"24px", "font-weight":"normal", "text-align":"center"}))
        if pyLDA3:
            childs.append(html.Iframe(src=pyLDA3["filename"], style={"height":pyLDA["height"], "width":pyLDA["width"]}))
            self.figure_counter += 1
            childs.append(html.P("Figure {}. ".format(self.figure_counter) + pyLDA["caption"], style={"font-family": "Georgia", "font-size":"24px", "font-weight":"normal", "text-align":"center"}))            

        childs += children
        self.sects.append(PosterSection(title, color, childs, height=height))

    #--
    def next_column(self):
        if len(self.sects) > 0:
            self.cols.append(PosterColumn(self.sects))
            self.sects = []

    #--
    def compile(self):
        title, authors, institutions = self._header_components()
        return Poster(title, authors, institutions, self.logo, self.cols, self.bg_color, self.banner_color)
