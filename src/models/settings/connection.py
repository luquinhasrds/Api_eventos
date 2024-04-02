from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:  #manipulador / gerenciador de bando de dados
    def __init__(self) -> None:   #construtor
        self.__connection_String = "{}:///{}".format(
            "sqlite",
            "storage,db",
        )
        self.__engine = None
        self.__session = None
    
    def connetc_to_db(self) -> None:
        self.__engine = create_engine(self.__connection_string)
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_maker = sessionmaker()
        self.__session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.close()