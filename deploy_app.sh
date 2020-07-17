POSTERTITLE=sample-iposter

# Create Heroku App
heroku create $POSTERTITLE
python iposter/qrcode.py $POSTERTITLE

# Commit Repo
git add .
git commit -m 'latest'
git push heroku master

# Run Heroku App
heroku ps:scale web=1
