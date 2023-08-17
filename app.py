from flask import Flask,render_template
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime 
from flask_bootstrap import Bootstrap

#Creacion y configuracion 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/flask_shopy_2687365' 
app.config["SECRET_KEY"] = "loquequierresssdsds"
bootstrap = Bootstrap(app)
#crear los objetos de SQLAlchemy y migrate
db = SQLAlchemy(app)
migrate = Migrate(app ,db)
#modelos 
class Cliente(db.Model):
    __tablename__= "clientes" #renombrar la tabla <- __tablename__: "nombre en plural"
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(100) , unique=True)
    email = db.Column(db.String(120) , unique=True)
    password = db.Column(db.String(128) )
class Producto(db.Model):
    __tablename__= "productos"
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(100))
    precio = db.Column(db.Numeric(precision= 10, scale=2))
    imagen = db.Column(db.String(100))
    
    
        
class Venta(db.Model):
    __tablename__= "ventas"
    id = db.Column(db.Integer, primary_key =True)
    fecha = db.Column(db.DateTime ,default=datetime.utcnow)
    cliente_id = db.Column(db.Integer , db.ForeignKey ('clientes.id'))
    
    
class Detalle(db.Model):
    __tablename__= "detalles"
    id = db.Column(db.Integer, primary_key =True)
    producto_id = db.Column(db.Integer , db.ForeignKey ('productos.id'))
    venta_id = db.Column(db.Integer , db.ForeignKey ('ventas.id'))
    cantidad = db.Column(db.Integer) 


#definir el formulario de registro de productos


class NuevoProductoForm(FlaskForm):
    username = StringField("Nombre de producto")
    precio = StringField("Precio de producto")
    submit = SubmitField("Registrar")



@app.route("/registrar_producto", methods=['GET' , 'POST'])
def registrar():
    form = NuevoProductoForm()
    p = Producto()
    if form.validate_on_submit():
        #registrar  producto en db
        form.populate_obj(p)
        db.session.add(p)
        db.session.commit() 

        return "producto registrado"
    return render_template("registrar.html",
                            form=form )

    #la clase debe ir con mayuscula

    #EN CASO DE TENER ERROR BORRAR EL ARCHIVO CON ESE POCO DE NUMEROS DE "versions" o si no borrar y crear la bd
    #model en mvc-> es una clase en la que se puede instanciar objetos, viene con atributos/metodos especificos para la CRUD
    #ORM OBJECT RELATIONAL MAPPER (especie de traductor) permite construir objetos para los registros

    #entrar a la consola python en vs:

    #python
    #from app(en este caso nombre del archivo) import "nombre" <- para acceder a un elemento, clase.
    #exit()  <-para salir
    # >>> c = Cliente(username = 'Juan A', email = 'jj@misena.edu.co', password = "123") EJEMPLO DE CREAR OBJETOS E INGRESAR ATRIBUTOS
    #db.session.add(c) para selecionar lo que esta en el objeto 
    #db.session.commit()   para actualizra en la base de datos 

    #clientes = Cliente.query.all() para hacer una consulta de los datos que estan en la tabla 
    #> xd = Cliente.query.get(3) para llamar uno especifio
    #para saber un campo de objeto xd.nombre_campo
    #db.session.delete(xd)  para eliminar objeto de la db 






