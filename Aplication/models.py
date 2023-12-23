from django.db import models

# Create your models here.

'''
CREATE TABLE Socios(
    DNI_Socio VARCHAR(9) PRIMARY KEY,
    Nombre VARCHAR(50),
    Telefono_socio VARCHAR(9),
    Correo VARCHAR(50),
    N_tarjeta VARCHAR(16),
    Domicilio VARCHAR(50)
);
'''

class Socios(models.Model):
    DNI_Socio = models.CharField(max_length=9, primary_key=True)
    Nombre = models.CharField(max_length=50)
    Telefono_socio = models.CharField(max_length=9)
    Correo = models.CharField(max_length=50)
    N_tarjeta = models.CharField(max_length=16)
    Domicilio = models.CharField(max_length=50)

    def __str__(self):
        return self.DNI_Socio

'''
CREATE TABLE Promociona(
	ID_Campana VARCHAR(9) REFERENCES Campañas(id_campana),
	ID_Articulo VARCHAR(9) REFERENCES ArtIculos(id_articulo),
	Temporada NUMBER(4),
	PRIMARY KEY(ID_Campana,ID_Articulo,Temporada)	
);
'''

class Promociona(models.Model):
    ID_Campana = models.CharField(max_length=9)
    ID_Articulo = models.CharField(max_length=9)
    Temporada = models.IntegerField()

    def __str__(self):
        return self.ID_Campana


'''
CREATE TABLE Financia(
	ID_Gasto VARCHAR(3) REFERENCES Gastos(id_gasto),
	Fecha_financia DATE,
	ID_campana VARCHAR(9) REFERENCES Campañas(ID_campana),
	PRIMARY KEY (ID_gasto,Fecha_financia)
);
'''

class Financia(models.Model):
    ID_Gasto = models.CharField(max_length=3)
    Fecha_financia = models.DateField()
    ID_campana = models.CharField(max_length=9)

    def __str__(self):
        return self.ID_Gasto

'''
CREATE TABLE Campañas(
	ID_Campana VARCHAR(9) PRIMARY KEY,
	Nom_Campana VARCHAR(50),
	Tipo VARCHAR(50),
	Duracion INT,
	Presupuesto INT
);
'''

class Campanas(models.Model):
    ID_Campana = models.CharField(max_length=9, primary_key=True)
    Nom_Campana = models.CharField(max_length=50)
    Tipo = models.CharField(max_length=50)
    Duracion = models.IntegerField()
    Presupuesto = models.IntegerField()

    def __str__(self):
        return self.ID_Campana
    
'''
CREATE TABLE Gastos (
	ID_gasto VARCHAR2(3) PRIMARY key,
  	Cantidad INT,
  	Tipo_gasto VARCHAR(30) 
);
'''

class Gastos(models.Model):
    ID_gasto = models.CharField(max_length=3, primary_key = True)
    Cantidad = models.IntegerField()
    Tipo_gasto = models.CharField(max_length = 20)

    def _str_(self):
        return self.ID_gasto
    

'''
CREATE TABLE Ingreso_Factura (
	ID_Ingreso VARCHAR(3),
  	Cantidad_ing INT,
  	Tipo_Ingreso VARCHAR(30),
  	DNI_Socio VARCHAR(9),
 	ID_Articulo VARCHAR(5),
  	Fecha_factura DATE,
	FOREIGN key (DNI_Socio, ID_Articulo, Fecha_factura) REFERENCES Compra(DNI_Socio, ID_Articulo, Fecha_factura) ,
  	PRIMARY KEY (ID_Ingreso)
);
'''

class Ingreso_factura(models.Model):
    ID_ingreso = models.CharField(max_length=3, primary_key = True)
    Cantidad = models.IntegerField()
    Tipo_gasto = models.CharField(max_length = 20)
    DNI_Socio = models.CharField(max_length=9)
    ID_Articulo = models.CharField(max_length=5)
    Fecha_factura = models.DateField()

    def _str_(self):
        return self.ID_ingreso
    

'''
CREATE table Supone(
    ID_gasto VARCHAR(3) REFERENCES Gastos(ID_gasto),
  	Nompro VARCHAR(30),
    Deporte_especializado CHAR(50),
 	Fecha_pago DATE,
    FOREIGN KEY(Nompro,Deporte_especializado) REFERENCES Proveedor(Nompro,Deporte_especializado),
  	PRIMARY KEY(ID_gasto,Nompro,Deporte_especializado,Fecha_pago)
);
'''

class Supone(models.Model):
    ID_gasto = models.CharField(max_length=3, primary_key = True)
    Nompro = models.CharField(max_length=30)
    Deporte_especializado = models.CharField(max_length=50)
    Fecha_pago = models.DateField()

    def _str_(self):
        return self.ID_gasto
    
    
''' --------------------------- '''
''' MODELOS ALBERTO - LOGISTICA '''
''' --------------------------- '''

'''
CREATE TABLE Articulos(
    ID_Articulo VARCHAR(5) PRIMARY KEY,
    Cantidad INT,
    Precio DECIMAL(10, 2),
    Deporte VARCHAR(50)
);

'''
class Articulos(models.Model):
    ID_Articulo = models.CharField(max_length=5, primary_key=True)
    Cantidad = models.IntegerField()
    Precio = models.IntegerField()
    Deporte = models.CharField(max_length=50)

    def __str__(self):
        return self.ID_Articulo
    
'''
CREATE TABLE Proveedor(
    Nompro VARCHAR(30),
    Deporte_especializado CHAR(50),
    Ciudad VARCHAR(50),
    Telefono_proveedor NUMBER(9) NOT NULL,
    PRIMARY KEY(Nompro,Deporte_especializado)
);
'''

class Proveedor(models.Model):
    Nompro = models.CharField(max_length=20, primary_key=True)
    Deporte_especializado = models.CharField(max_length=50)
    Ciudad = models.CharField(max_length=50)
    Telefono_proveedor = models.CharField(max_length=9)

    def __str__(self):
        return self.Nompro

'''
CREATE TABLE Compra(
    DNI_Socio VARCHAR(9) REFERENCES Socios(dni_socio),
    ID_Articulo VARCHAR(9) REFERENCES Articulos(id_articulo),
    Fecha_factura DATE,
    Cantidad_compra INT,
    PRIMARY KEY(DNI_Socio,ID_articulo,Fecha_factura)
);
'''

class Compra(models.Model):
    DNI_Socio = models.CharField(max_length=9, primary_key=True)
    ID_Articulo = models.CharField(max_length=5)
    Fecha_factura = models.DateField()
    Cantidad_compra = models.IntegerField()

    def __str__(self):
        return self.DNI_Socio