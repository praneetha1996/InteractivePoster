from iposter.server import run_poster
import iposter.components as ip
import dash_html_components as html

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

if __name__ == "__main__":

    poster = create_poster()
    web_app = run_poster(poster)
