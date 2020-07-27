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
    my_poster = iPoster(title=" A Deep Learning Model for Predicting Sentiment of Disease of Despair Patients", # Title of your poster
                        authors_dict={"Praneetha Gouni":"University of Cincinnati",
                                      "Victor":"University of Cincinnati", # Authors in {student, mentors, PI} order
                                      "Rafael Zamora":"Lawrence Berkeley National Laboratory",
                                      "Shirley Wang":"Lawrence Berkeley National Laboratory",
                                      "Victoria Wangia-Anderson":"University of Cincinnati",
                                      "Silvia Crivelli":"Lawrence Berkeley National Laboratory"},
                                    
                        logo = "uc1.png", # Home institution logo
                        banner_color=colors.DOE_GREEN, # Color of banner header; colors has preset colors
                        text_color=colors.WHITE)

    # Add sections to first column then add new column
    my_poster.add_section(title="ABSTRACT",
        text="Work on suicide and suicidal behavior has risen in the last 15 years on many fronts, from the health, social and psychological dimensions to the broader world and influences at the community level where there is realization that mental health care and interventions are critical. Electronic health records ( EHRs) provide opportunities to mine patient data  for early detection and to improve patient care. The growing difficulties in recruiting trials, burdensome data collection and unpredictable common outcomes have been voiced. There have been doubts. To counteract these trends by using electronic health records is a subject of intense interest.  Long-term our goal is to develop predictive models able to use sentiment to detect risk factors associated with suicide such as homelessness.    Advances in natural language processing have made it possible to extract information from large scale unstructured data like nursing notes. Nursing notes extracted from MIMIC-III have not been widely used in prediction models for clinical outcomes, despite containing rich information.   Nurse notes have been found to be reflect the patient's perspective. Through our work we contribute to the longer-term goal by proposing a supervised machine learning approach using bag-of-words (BOW) and parts of speech. We compare word scoring methods and find that frequency performs the best. We built a deep learning model based on sentiment analysis that could classify patients notes as either POSITIVE or NEGATIVE.")
    my_poster.add_section(title="BACKGROUND",
        text="MIMIC III is an openly available dataset developed by the MIT Lab for Computational Physiology, comprising de-identified health data associated with ~60,000 intensive care unit admissions. We are focused on ICD9 codes of the Diseases of Despair patient group which include conditions like Depression, Mental Illness, Anxiety, Stress, Family Conflict, Isolation, Loneliness, Domestic or Sexual Abuse, Unemployment, Alcohol or Drug Use, Previous Suicide Attempts. National Health Care for the Homeless Council’s states that, many individuals that are unhoused have health conditions that are often intertwined with behavioral health issues. These health issues are exacerbated by exposure to the elements, heightened risk of violence through physical and sexual abuse can lead to hopelessness, distrust and self-treatment. Given the conditions above that already increase the likelihood of suicide in the general population, these compounding factors place those experiencing homelessness at an explicitly higher risk.")
    my_poster.add_section(title="Preprocessing of Text Data",
        img1={"filename":"preprocess.PNG", "height":"7in", "width":"10in", "caption":"This figure explains how unstructered data is preprocessed before the data is fed to a model."})
    my_poster.next_column()
    my_poster.add_section(title="MODEL",
        text="A Multilayer Perceptron (MLP) consists of at least three layers of nodes: an input layer, a hidden layer and an output layer. MLP utilizes a supervised learning technique called backpropagation for training. The model was built with a single hidden layer with 50 neurons and a rectified linear activation function. The output layer is a single neuron with a sigmoid activation function for predicting 0 for negative and 1 for positive reviews. After  preprocessing, training data is prepared by calculating the sentiment polarity scores for notes of each patient and then fed into the model. The network will be trained using the efficient Adam implementation of gradient descent and the binary cross entropy loss function, suited to binary classification problems.")
 
    # Add sections to second column then add new column
    # my_poster.next_column()

    # my_poster.add_section(title="MODEL",
    #     text="A Multilayer Perceptron (MLP) consists of at least three layers of nodes: an input layer, a hidden layer and an output layer. Except for the input nodes, each node is a neuron that uses a nonlinear activation function. MLP utilizes a supervised learning technique called backpropagation for training. Its multiple layers and non-linear activation distinguish MLP from a linear perceptron. It can distinguish data that is not linearly separable.")
    my_poster.add_section(title="Model Accuracy and loss",
        img1={"filename":"accuracy.PNG", "height":"6in", "width":"8in", "caption":"This figure shows us that as number of epochs increases accuracy increases."},
    # my_poster.add_section(title="Model loss",
        img2={"filename":"loss.PNG", "height":"6in", "width":"8in", "caption":"This figure shows us that as number of epochs increases loss decreases."})
    my_poster.add_section(title="Word Scoring methods",
        img1={"filename":"word models.PNG", "height":"7in", "width":"10in", "caption":"Comparing Word Scoring Methods."})
    # my_poster.add_section(title="Model Output",
    #     img1={"filename":"model.PNG", "height":"6in", "width":"10in", "caption":"Comparing Word Scoring Methods."})
       
    my_poster.next_column()
    my_poster.add_section(title="Model Output",
        img1={"filename":"model.PNG", "height":"6in", "width":"8in", "caption":"Comparing Word Scoring Methods."})
      

    my_poster.add_section(title="Findings from MIMIC 3 Dataset",
        pyLDA={"filename":"code3.html", "height":"9in", "width":"10in", "caption": "This interactive plot is used for analysing the MIMIC3 dataset and find interesting facts from the data using tableau desktop."})
        # img1={"filename":"Story 1.PNG", "height":"6in", "width":"10in", "caption":"Length of Stay of DOD patients in ICU"},
        # img2={"filename":"Story 2.PNG", "height":"6in", "width":"10in", "caption":"Death counts for DOD patients based on marital status"})
       
    my_poster.add_section(title="CONCLUSIONS", text="The multilayer Perceptron bag-of- word model has been successful and can be used to predict new clinical data. Frequency word comparison works best for clinical data. The database of MIMIC-III comes from a single clinical center with a unique clinical culture which has influenced the way the nurses have built the notes. Thus the generalization of the model can be limited.")
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
