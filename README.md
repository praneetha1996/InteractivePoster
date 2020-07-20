# iPoster: Interactive Poster Guide
The following guide shows how to create and deploying a public Flask iPoster application using the Heroku platform.
This is our [example project](https://student-poster-template.herokuapp.com/)

### Step 1. Fork this Github Repo:
Fork this repo into your Github account using the fork button at the
top of the page. After that clone the forked repo using the following command on your
terminal.
```
$ git clone [forked-repo-url]
$ cd [forked-repo]
```

### Step 2. Create a virtualenv with needed requirments
This process assumes you have Python3 and Pip installed.

```
# Run installation BASH script

$ source setup_env.sh
```

### Step 3. Implement your Poster using the available tools
The poster code can be found in `app.py`. There, you will find a function
called `create_poster` which defines the current template used in this guide.

Here is a commented version of that function:


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
