from flask import Flask

app = Flask(__name__)

from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'beauapp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

from webapp import routes

