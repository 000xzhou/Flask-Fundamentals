from flask import Flask

app = Flask(__name__)

# ***/welcome***   Returns “welcome”

# ***/welcome/home***   Returns “welcome home”

# ***/welcome/back***   Return “welcome back”

@app.route('/welcome')
def welcome():
   return "welcome"

@app.route('/welcome/home')
def welcome_home():
   return "welcome home"

@app.route('/welcome/back')
def welcome_back():
   return "welcome back"