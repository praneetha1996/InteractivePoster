# Imports
import os, flask, dash
from pathlib import Path
from random import randint
import dash_bootstrap_components as dbc

# Plots
from plotly.express import bar
import pandas as pd

# Import iPoster Object Class
from iposter.iposter import iPoster
import iposter.colors as colors

#*** Run Local Flag ***
RUN_LOCAL=False

# ******************Define Your Interactive Poster Here***************
# The following shows a sample interactive poster.
# Images for sections must be saved under the assets/ folder.
# You can import code from your own modules and construct the final dash
# interactive poster here.
def create_poster():

    # Instanitate an iPoster
    my_poster = iPoster(title="Diseases of Despair; CLassification model based on Sentimental Analysis", # Title of your poster
                        authors_dict={"Praneetha Gouni" : "University of Cincinnati",
                                      "Victor Adewopo" : "University of Cincinnati", # Authors in {student, mentors, PI} order
                                      "Rafael Zamora" : "Lawrence Berkeley National Laboratory",
                                      "Shirley Wang" : "Lawrence Berkeley National Laboratory",
                                      "Victoria Wangia" : "University of Cincinnati",
                                      "Silvia Crivelli" : "Lawrence Berkeley National Laboratory"},
                                    
                        logo = "UC.png", # Home institution logo
                        banner_color=colors.DOE_GREEN, # Color of banner header; colors has preset colors
                        text_color=colors.WHITE)

    # Add sections to first column then add new column
    my_poster.add_section(title="ABSTRACT",
        text="Work on suicide and suicidal behavior has risen in the last 15 years on many fronts, from the health, social and psychological dimensions to the broader world and Influences at community level, such as access to mental health care. Electronic health records ( EHRs) provide opportunities to improve patient care, integrate clinical practice performance measures and facilitate clinical research. The growing difficulties in recruiting trials, burdensome data collection and unpredictable common outcomes have been voiced. There have been doubts. To counteract these trends by using electronic health records is a subject of intense interest. Nursing notes extracted from MIMIC-III, a public intensive care unit (ICU) database have not been widely used in prediction models for clinical outcomes, despite containing rich information. Advances in natural language processing have made it possible to extract information from large scale unstructured data like nursing notes. In our work we have applied a sentiment analysis to nursing notes and built up a model for deciding polarity of text (health records) and afterward arranging the content as indicated by its opinion into one of the classes POSITIVE and NEGATIVE.")
    my_poster.add_section(title="BACKGROUND",
        text="MIMIC is an openly available dataset developed by the MIT Lab for Computational Physiology, comprising deidentified health data associated with ~60,000 intensive care unit admissions. It includes demographics, vital signs, laboratory tests, medications, and more. We are focused on ICD cods of Diseases of Despair patients group which was created by the Doctors at U.S Department of Veterans Affairs( VA). These Doctors identified the patients who may be at a high risk as their ICD codes are related to suicide and grouped them to obtain Diseases of Despair Patients.")
    my_poster.add_section(title="Figures",
        img1={"filename":"preprocess.PNG", "height":"8in", "width":"10in", "caption":"This figure explains how unstructered data is preprocessed before the data is fed to a model."})
    my_poster.next_column()

    # Add sections to second column then add new column

    my_poster.add_section(title="MODEL",
        text="A Multilayer Perceptron (MLP) consists of at least three layers of nodes: an input layer, a hidden layer and an output layer. Except for the input nodes, each node is a neuron that uses a nonlinear activation function. MLP utilizes a supervised learning technique called backpropagation for training. Its multiple layers and non-linear activation distinguish MLP from a linear perceptron. It can distinguish data that is not linearly separable.")
    my_poster.add_section(title="Figures",
        img1={"filename":"accuracy.PNG", "height":"5in", "width":"5in", "caption":"This figure shows us that as number of epochs increases accuracy increases."})
    my_poster.add_section(title="Figures",
        img1={"filename":"loss.PNG", "height":"5in", "width":"5in", "caption":"This figure shows us that as number of epochs increases loss decreases."})
    my_poster.add_section(title="Figures",
        img1={"filename":"word models.PNG", "height":"5in", "width":"5in", "caption":"Comparing Word Scoring Methods."})
       
    my_poster.next_column()

    my_poster.add_section(title="Data Analysis Plot",
        pyLDA={"filename":"code2.html", "height":"10in", "width":"15in", "caption": "This interactive plot is used for analysing the MIMIC3 dataset and find interesting facts from the data using tableau desktop."})
    
    my_poster.add_section(title="CONCLUSIONS", text="The multilayer Perceptron bag-of - word model has been successful and can be used to predict new clinical data. There are also some limitations and important technical considerations. Although the MIMIC-III information comes from a large-volume hospital with a considerable number of patients, only a small cohort of the nurses are the authors of the study notes. Additional cohorts of clinicians may produce nursing notes with different trainings, experiencing and working environments. The database of MIMIC-III comes from a single clinical center with a unique clinical culture which has influenced the way the nurses have built the notes. Thus the generalization of the model can be limited.")
    my_poster.add_section(title="ACKNOWLEDGMENTS", text="I thank Dr. Silvia Crivelli for providing me this opportunity, I thank Dr. Victoria Wangia for all her support and guidance, I thank Shirley and Rafael for their assistance in helping me complete my project, I thank all other team members for sharing your views and helping me to achieve this and for all those wonderful memories, I thank anonymous references for their useful suggestions.This work was supported by the U.S. Department of Energy, Office of Science, Computational Research Division (CRD) of the Berkeley National Lab, and VA Million Veteran Program (MVP)")
    my_poster.next_column()
    return my_poster.compile()

# **********************************************************************

# Dash App Configuration
if RUN_LOCAL:
    app = dash.Dash(__name__,
                    assets_folder= str(Path(__file__).parent.absolute())+"/assets",
                    assets_url_path='/',
                    external_stylesheets=[dbc.themes.BOOTSTRAP],
                    suppress_callback_exceptions=True)
else:
    server = flask.Flask(__name__)
    server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
    app = dash.Dash(__name__,
                    server=server,
                    assets_folder= str(Path(__file__).parent.absolute())+"/assets",
                    assets_url_path='/',
                    external_stylesheets=[dbc.themes.BOOTSTRAP],
                    suppress_callback_exceptions=True)
app.layout = create_poster()

# Main Function
if __name__ == "__main__":
    if RUN_LOCAL:
        app.run_server(debug=False, host="0.0.0.0", port="8888")
    else:
        app.server.run(debug=True, threaded=True)
