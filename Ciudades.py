import json

import Connection


class Ciudad():

    def __init__(self, nombre, provincia, comunidadAutonoma,geolocalizacion, superficie, altitud, poblacion, POI):
        self._nombre= nombre
        self._provincia=provincia
        self._comunidadAutonoma = comunidadAutonoma
        self._geolocalizacion=geolocalizacion
        self._superficie = superficie
        self._altitud=altitud
        self._poblacion=poblacion
        self.PuntoInteres=POI


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

    def __init__(self, nombre, tipo, direccion, geolocalizacion):
        self._nombre=nombre
        self._tipo=tipo
        self._direccion=direccion
        self._geolocalizacion = geolocalizacion
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def snombre(self, nombre):
        self._nombre= nombre

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def stipo(self, tipo):
        self._tipo = tipo

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def sdireccion(self, direccion):
        self._direccion = direccion

    @property
    def geolocalizacion(self):
        return self._geolocalizacion

    @geolocalizacion.setter
    def sgeolocalizacion(self, geolocalizacion):
        self._geolocalizacion = geolocalizacion

'''
class MyCiudad(object):
    def __init__(self, **kwars):
        self.__dict__.update(self, kwars)

def analIce(inputString):
'''

def save(cliente, ciudad):

    diccionario={}
    try:
        cliente.wikicity.aggregate([{'$match': {'name': ciudad.nombre}}]).next()
        print("exise")
    except:
        diccionario.update({"province": ciudad.provincia})
        print(ciudad.provincia)
        diccionario.update({"name": ciudad.nombre})
        diccionario.update({"autonomous_community": ciudad.comunidadAutonoma})
        diccionario.update({"location": ciudad.geolocalizacion})
        diccionario.update({"elevation": ciudad.altitud})
        diccionario.update({"area": ciudad.superficie})
        diccionario.update({"POI": ciudad.PuntoInteres})
        cliente.wikicity.insert(diccionario)


def insert(cliente, inputCity):

    print (inputCity)
    for key, value in inputCity.items():
        if key=="name":
            try:
                print("try..")
                cliente.wikicity.aggregate([{'$match': {'name': value}}]).next()
                print("tryed nicerony")
            except:
                cliente.wikicity.insert(inputCity)


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
            insert(cliente, n)

    file.close()
nuevoPOI = PuntoInteres("poii","poii","poii","poii")
nuevaCiudad = Ciudad("Astun", "Astun", "Astun", "Astun", "Astun", "Astun", "Astun", nuevoPOI)
print("hola")
save(cliente, nuevaCiudad)











'''
            try:
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


    #print (wikicity[0].provincia())



    #c = MyCiudad(**{'nombre': 'Barajas', 'provincia': 'madrid'})

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