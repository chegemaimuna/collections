# collection
# [App](http://flask.pocoo.org/) To Keep Track of a collection of *Stuffs*

# Installation:
* Clone this repo to your workspace
* Create  a python virtual environment. [Here](http://docs.python-guide.org/en/latest/dev/virtualenvs/) is how to do so.
* Make sure you have `pip` installed. If new to this follow this [link](https://packaging.python.org/tutorials/installing-packages/)
* Make sure you are in the environement that you created and Install dependencies. `pip install -r requirements.txt`
* Navigate your way to the `~/flaskapp/` directory.
* Run `pip install -e .` _Note: you should run this command on the directory where the setup.py is located_ 
* Run `export FLASK_APP=flaskapp` if on unix shells or `set FLASK_APP=flaskapp`  if on Windows _note: No space between the equal sign_.
* Run `export FLASK_DEBUG=1` if on unix shells or `set FLASK_DEBUG=1` if on Windows to allow debugging. 
* Finally run `flask run`.
* visit `http://127.0.0.1:5000/` in your browser.
## enjoy!

