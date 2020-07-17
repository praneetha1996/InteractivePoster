# iPoster: Interactive Poster Guide
The following guide for deploying  and managing a public Flask iPoster application on the heroku platform.
This is our [example project](https://student-poster-template.herokuapp.com/)

### Step 1. Fork this Github Repo:
Fork this repo into your Github account using the fork button at the
top of the page. After that clone the forked repo using the following command on your
terminal.
```
$ git clone [forked-repo-url]
$ cd [project]
```

### Step 2. Create a virtualenv with needed requirments
This process assumes you have Python3 and Pip installed.

```
$ source setup_env.sh # Run installation BASH script
```

### Step 3. Implement your Poster using the available tools
The poster code can be found in `app.py`. There you will find a function
called `create_poster` which defines the current template used in this guide.

Here is a commented version of that function:

```python
def create_poster():

    # Create an iPoster object and define its title and authors.
    # Authors are defined as a dictionary with the name of the authors as keys and
    # name of institutions as values.
    my_poster = iPoster(title="Research poster title; state the main topic of your study",
                        authors_dict={"Inter Name" : "University Name",
                                      "Researcher Name" : "University Name",
                                      "Mentor (Primary Investigator) Name" : "Lawrence Berkeley National Laboratory"})

    # Add sections to first column then add new column
    my_poster.add_section(title="Abstract",
        text="The first cell of your Research Poster must include your research abstract in its entirety. \
        The abstract should fully summarize the contents of your Research Paper in one paragraph. For \
        detailed instructions about how to write the abstract, read Chapter 14 of Scientific Writing\
        and Communication. ")
    my_poster.add_section(title="Background Info",
        text="Begin with the broad background information and significance of\
             your research topic; answer the question “Why should I care?’ \
             This provides the audience with context about how your research \
             relates to the world around them.")
    my_poster.add_section(title="Colors", color="#5062dd",
        text="Use color to increase the readability of your Research Poster, highlighting important \
        points. Avoid distracting colors. Set section header color with the color parameter.")
    my_poster.next_column()

    # Add sections to second column then add new column
    my_poster.add_section(title="Fonts",
        text="Use the third person. Use concise, not conversational language.\
        .Use bulletpoints whenever possible. Use more images/graphics and less \
        text. Title, up to 90 pt, bold in Arial, Georgia, Palatino or Tahoma font. Headers, \
        50 - 72 pt, bold in Arial, Georgia, Palatino or Tahoma font. Internal text, 24 - 44 \
        pt in Georgia or Palatino font. Spell out acronyms the first time they are ")
    my_poster.add_section(title="Images",
        text="Save your image in the assets directory and set img to the filename.",
        img={"filename":"test.png", "height":"6in", "width":"8in"},
        fig_caption="Text for figure caption.")
    my_poster.add_section(title="Other", text="This is some card text.")
    my_poster.next_column()

    # Add sections to third column then add new column
    df = pd.DataFrame([[i,i] for i in range(100)], columns=["x","y"])
    my_plot = bar(df, "x", "y")
    my_poster.add_section(title="Plots",
        text="You can add interactive plots through plotly.",
        plot=my_plot)
    my_poster.add_section(title="Other", text="This is some card text.")
    my_poster.add_section(title="Other", text="This is some card text.")
    my_poster.add_section(title="Other", text="This is some card text.")
    my_poster.next_column()

    return my_poster.compile()
```

### Step 4. Initialize the folder with a sample app (app.py), a .gitignore file, requirements.txt, and a Procfile for deployment
* Deploy from local:
```
$ heroku create sample-dash-app # change sample-dash-app to your website name
$ git add . # add all files to git
$ git commit -m 'Initial'
$ git push heroku master # deploy code to heroku
$ heroku ps:scale web=1  # run the app with a 1 heroku "dyno"
```

* Deploy from github remote:
you can open herokuapp dashboard and connect your github repo to your herokuapp.
The instruction here :
[Instruction](https://devcenter.heroku.com/articles/github-integration)
