import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Gives access to the project in any OS we find ourselves in 
# Allows outside files_folders to be added to the project
# from the base directory

class Config():
    """
    Set config bariables for the flask app.
    Using enviornment variables where avaliblae otherwise
    creath the config variable if not done already.
    """
    
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'YOU WILL NEVER GUESS NANANAH BOO BOO'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #turns off updates messages from sqlachemy
    
