from controls.dao.daoAdapter import DaoAdapter
from models.uni.universidad import Universidad
class UniversidadDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Universidad)
        self.__universidad = None

    @property
    def _universidad(self):
        if self.__universidad == None:
            self.__universidad = Universidad()
        return self.__universidad

    @_universidad.setter
    def _universidad(self, value):
        self.__universidad = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__universidad._id = self._lista._length + 1
        self._save(self.__universidad)
    
        
    