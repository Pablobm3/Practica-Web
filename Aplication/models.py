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
        return self.Nombre

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

