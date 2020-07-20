# iPoster: Interactive Poster
The following guide shows how to create and deploy a public
iPoster application using the Heroku platform.
The web application for the poster is implemented using
Flask, Dash, and Plotly.

This is this repo's [example iPoster](https://iposter-template.herokuapp.com/).

### Step 1. Fork this Github Repo:
Fork this repo into your Github account using the fork button at the
top of the page. After that, clone your forked repo using the
following command on your terminal.
```bash
git clone [forked-repo-url]
cd [forked-repo]
```

### Step 2. Create a `virtualenv` with required dependencies:
This process assumes you have Python3 and Pip installed.
Run the following Bash script found in the repo to
install the needed python packages.

```bash
source setup_env.sh
```

To load the virtualenv, run the following command.

```bash
source iposter-env/bin/activate
```

### Step 3. Implement your poster using the available tools:
The poster code can be found in `app.py`. There, you will find a function
called `create_poster` which defines the current template used in this guide.

Here is a commented version of that function:

### Step 4. Run the poster locally:
To make sure that your poster looks like you want it before deploying it
using Heroku, run the poster application locally. First change the
`RUN_LOCAL` flag in the `app.py` file to `True`.

```python
# file: app.py

#*** Run Local Flag ***
RUN_LOCAL=True
```

After this, you can run dash application. Copy and paste the URL listed on the
terminal output.

```bash
$ python3 app.py
```


### Step 4. Deploy poster on Heroku:

#### Step 4.a. Create a free Heroku account:
[Account Signup](https://signup.heroku.com)

#### Step 4.b. Create a new app:
After you log in to your Heroku app, click create a new app.
Your application name will be the url domain. After that,


[Account Signup](https://signup.heroku.com)

* Deploy from github remote:
you can open herokuapp dashboard and connect your github repo to your herokuapp.
The instruction here :
[Instruction](https://devcenter.heroku.com/articles/github-integration)
