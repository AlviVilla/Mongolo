class Consultas():

    def __init__(self, cliente):
      self._cliente=cliente;
    def c1(self, comunidad):
        return self._cliente.wikicity.aggreagate([{'$match': {'autonomous_community': comunidad}}, {'$project' : {'name':1}}]).next()

