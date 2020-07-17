# 1. Iposter Guide
## =-----------=
# 2. Herokuapp Guide
This is simple guide for deploying  and managing this public Flask applications heroku platform.

## Step 1. Create a new folder for your project:
```
$ Git Clone [project]
$ cd [project]
```

## Step 2. Initialize the folder with git and a virtualenv
```
$ git init        # initializes an empty git repo
$ virtualenv venv      # creates a virtualenv called "venv"
$ source venv/bin/activate       # uses the virtualenv
```
### Step 3. Install Needed package 
```
$ pip install dash
$ pip install plotly
$ pip install dash-bootstrap-components
```
### Step 4. Deploying app 
```
$ pip install gunicorn
```

### Step 5. Initialize the folder with a sample app (app.py), a .gitignore file, requirements.txt, and a Procfile for deployment
1) app.py

2) .gitignore
>venv  
>*.pyc       
>.DS_Store  
>.env 

3) requirements.txt

4) Procfile
```
$ web: gunicorn app:server
```
(Note that app refers to the filename app.py. server refers to the variable server inside that file).

### Step 6. Initialize the folder with a sample app (app.py), a .gitignore file, requirements.txt, and a Procfile for deployment
```
$ heroku create sample-dash-app # change sample-dash-app to your website name
$ git add . # add all files to git
$ git commit -m 'Initial'
$ git push heroku master # deploy code to heroku
$ heroku ps:scale web=1  # run the app with a 1 heroku "dyno"
```

