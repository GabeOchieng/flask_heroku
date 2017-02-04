# flask_heroku
Beginners project for a minimal Flask app

# Introduction
Hello everyone! This repo hosts an educational level Flask app, preparing for Heroku deployment!
It does not require any special knowledge, just to know and understand Python!

# Getting Started
There are some pretty basic steps needed in order to get things started with this project!
- Install the project requirements: `pip install -r requirements.txt`
- Login to your Heroku account using the Heroku cli. Simple as `heroku login`.
- Create a Heroku app on your account, to deploy your first app! `heroku create`
- Make your first Heroku app deployment! This will also host your code on Heroku's git repo! `git push heroku master`
- The application should be now deployed. Ensure that you have at least one instance running your app code! `heroku ps:scale web=1`
- Open your app and get greeted by your `home.html` template! Congratulations, you did it!

# Next steps
In order to get things a bit more advanced and better understand how Flask and Heroku work together, try
creating a new template, let's say `about.html` containing a short bio of yourself, along with the respective Python method inside `app.py`, something like `/about`. Then try deploying a new version of your app on Heroku!
