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
        self.PuntoInteres=[]


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

'''
class MyCiudad(object):
    def __init__(self, **kwars):
        self.__dict__.update(self, kwars)

def analIce(inputString):
'''


def save(cliente, inputCity):

    print (inputCity)
    for key, value in inputCity.items():
        if key=="name":
            try:
                print("try..")
                cliente.wikicity.aggregate([{'$match': {'name': value}}]).next()
                print("tryed nicerony")
            except:
                cliente.wikicity.insert(inputCity)
    '''
            for name in ids:
                if name == value:
                    print ("se siente ya esta")
                    return
            ids.append(value)
    cliente.wikicity.insert(inputCity)
    '''


'''
        if(key=="province"):
            diccionario.update({"province": value})
        if(key=="name"):
            diccionario.update({"name": value})
        if (key == "autonomous_community"):
            diccionario.update({"autonomous_community": value})
        if (key == "location"):
            diccionario.update({"location": value})
        if (key == "elevation"):
            diccionario.update({"elevation": value})
        if (key == "area"):
            diccionario.update({"area": value})
        if (key =="location"):
            for k, v in value.items():
                if(k=="coordinates"):
                    diccionario.update({"location": v})
        if (key=="POI"):
            diccionario.update({"POI": value})
            for punto in value:
                print("hola amigsidjflaksdf")
                for k, v in punto.items():
                    print (k, v)
                print("\n")
            print("--------------------------------------------------------------------")
    cliente.wikicity.update({"location": id}, diccionario, True)
'''

conexion = Connection.Conection()
cliente = conexion.conected()
ids = []
count = 1


def consulta(inputString, cliente):
    pass

with open('wikicity.json', 'r') as file:
    for l in file:
        ciudades = json.loads(l)
        #cliente.createCollection("wikicity", ciudades)
        for n in ciudades:
            save(cliente, n)
            '''try:
                cliente.wikicity.update({"name": },)

            ide= cliente.wikicity.insert(n)

            print (ide)
            '''
    '''  for l in :
        print ('hola')

        save(cliente, l, count)
        count += 1
        elID = cliente.insert_one(l).inserted_id
        print(type(elID))
    '''
file.close()

    #print (wikicity[0].provincia())



    #c = MyCiudad(**{'nombre': 'Barajas', 'provincia': 'madrid'})

