from flask import Flask, render_template, redirect, request, Response, url_for
from config import config
from flask_mysqldb import MySQL






app=Flask(__name__)

#app.config['MYSQL_HOST']='localhost'
#app.config['MYSQL_USER']='root'
#app.config['MYSQL_PASSWORD']=''
#app.config['MYSQL_DB']='florma'


#db= MySQL(app)




@app.route('/')
def index():
   return redirect(url_for('login'))

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=="POST":
        email= request.form['usuario']
        password =request.form['contrasena']
        return render_template('auth/login.html')
        print(email)
        print(password)
    else:
        return render_template('auth/login.html') 
        print(email)
        print(password)  

@app.route('/venta')
def venta():
    return render_template('index.html')

@app.route('/registro')
def registro():
    return render_template('registroC_P.html')

@app.route('/registro/producto')
def registroP():
    return render_template('registroProducto.html')

@app.route('/inventario')
def inventario():
    return render_template('index.html')

if __name__== '__main__':
    app.config.from_object(config['development'])
    app.run()