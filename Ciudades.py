import json

import Connection


class Ciudad():

    def __init__(self):
        self._nombre= None
        self._provincia=None
        self._comunidadAutonoma = None
        self._geolocalizacion=None
        self._superficie = None
        self._altitud=None
        self._poblacion=None
        self.PuntosInteres=[]


    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def provincia(self):
        return self._provincia

    @provincia.setter
    def provincia(self, provincia):
        self._provincia = provincia

    @property
    def comunidadAutonoma(self):
        return self._comunidadAutonoma

    @comunidadAutonoma.setter
    def comunidadAutonoma(self,  comunidadAutonoma):
        self._comunidadAutonoma =comunidadAutonoma

    @property
    def geolocalizacion(self):
        return self._geolocalizacion

    @geolocalizacion.setter
    def geolocalizacion(self, geolocalizacion):
        self._geolocalizacion = geolocalizacion

    @property
    def superficie(self):
        return self._superficie

    @superficie.setter
    def superficie(self, superficie):
        self._superficie = superficie

    @property
    def altitud(self):
        return self._altitud

    @altitud.setter
    def altitud(self, altitud):
        self._altitud = altitud

    @property
    def poblacion(self):
        return self._poblacion

    @poblacion.setter
    def poblaciona(self, poblacion):
        self._poblacion = poblacion


class PuntoInteres():
    def __init__(self):
        self._nombre=None
        self._tipo=None
        self._direccion=None
        self._geolocalizacion = None
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre= nombre

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def geolocalizacion(self):
        return self._geolocalizacion

    @geolocalizacion.setter
    def geolocalizacion(self, geolocalizacion):
        self._geolocalizacion = geolocalizacion





class MyCiudad(object):
    def __init__(self, **kwars):
        self.__dict__.update(self, kwars)
'''
def analIce(inputString):
'''
conexion = Connection.Conection()
cliente = conexion.conected()


lista = []
with open('wikicity.json', 'r') as file:
    for l in file:
        lista = json.loads(l)
    file.close()
print lista


        #c = MyCiudad(**{'nombre': 'Barajas', 'provincia': 'madrid'})

