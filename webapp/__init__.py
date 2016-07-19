from flask import Flask

app = Flask(__name__)

#app.config["MAIL_SERVER"] = "smtp.gmail.com"
#app.config["MAIL_PORT"] = 465
#app.config["MAIL_USE_SSL"] = True
#app.config["MAIL_USERNAME"] = 'beauappmail@gmail.com'
#app.config["MAIL_PASSWORD"] = 'Weareudstudents'

#import app.models
#import app.forms
#import app.routes
from webapp import routes

#from webapp.routes import mail
#mail.init_app(app)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://neurod_devuser:devpwd@166.62.40.36/neurod_database'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://neurod_devuser:devpwd@166.62.40.36/neurod_webappdev'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ndsitedev:devpwd@mysql.server/ndsitedev$NeuroDining_2015'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://devuser:devpwd@localhost/NeuroDining'
#app.config['SQLALCHEMY_POOL_RECYCLE'] = 499
#app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20

#from webapp.models import db
#db.init_app(app)
