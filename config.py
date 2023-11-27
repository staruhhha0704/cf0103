from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'u1987781_default'
app.config['MYSQL_DATABASE_PASSWORD'] = 'oIFZ5mjeu2L6dYM7'
app.config['MYSQL_DATABASE_DB'] = 'u1987781_prak15'
app.config['MYSQL_DATABASE_HOST'] = 'server39.hosting.reg.ru'
app.config['JSON_AS_ASCII'] = False
mysql.init_app(app)