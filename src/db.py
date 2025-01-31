from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'hackathon2023-tl.database.windows.net'
app.config['MYSQL_USER'] = 'axelcenteno'
app.config['MYSQL_PASSWORD'] = 'Hackathon2023-tl'
app.config['MYSQL_DB'] = 'pacientes'
mysql=MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/camaras')
def camaras():
    return render_template('camaras.html')

@app.route('/medicamentos')
def medicamentos():
    return render_template('medicamentos.html')


if __name__=='__main__':
    app.run(port=3000, debug = True)
