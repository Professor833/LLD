class BaseModel:
    def __init__(self) -> None:
        self.__id = None

    # getter and setter for id
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

