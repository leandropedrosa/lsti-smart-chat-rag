from pymongo import MongoClient, errors
import os
import logging

ATLAS_CONNECTION_STRING = str(os.getenv('ATLAS_CONNECTION_STRING'))
DB_NAME = str(os.getenv('ATLAS_DB_NAME'))
COLLECTION_NAME = str(os.getenv('ATLAS_COLLECTION_NAME'))


class AtlasClient:

    def __init__(self):
        try:
            if not ATLAS_CONNECTION_STRING:
                raise ValueError("A string de conexão do Atlas não foi configurada.")
            if not DB_NAME:
                raise ValueError("O nome do banco de dados não foi configurado.")

            self.mongodb_client = MongoClient(ATLAS_CONNECTION_STRING)
            self.database = self.mongodb_client[DB_NAME]
            logging.info("Conexão com o MongoDB Atlas estabelecida com sucesso.")
        except errors.ConnectionFailure as e:
            logging.error(f"Erro ao conectar ao MongoDB Atlas: {e}")
            raise
        except Exception as e:
            logging.error(f"Erro na inicialização do AtlasClient: {e}")
            raise

    def ping(self):
        try:
            return self.mongodb_client.admin.command('ping')
        except errors.PyMongoError as e:
            logging.error(f"Erro ao pingar o MongoDB: {e}")
            return {"error": f"Erro ao pingar o MongoDB: {str(e)}"}

    def get_collection(self):
        try:
            if not COLLECTION_NAME:
                raise ValueError("O nome da coleção não foi configurado.")
            collection = self.database[COLLECTION_NAME]
            return collection
        except errors.CollectionInvalid as e:
            logging.error(f"Erro ao acessar a coleção: {e}")
            raise
        except Exception as e:
            logging.error(f"Erro ao obter a coleção: {e}")
            raise

    def find(self, collection_name, filter={}, limit=0):
        try:
            collection = self.database[collection_name]
            items = list(collection.find(filter=filter, limit=limit))
            return items
        except errors.PyMongoError as e:
            logging.error(f"Erro ao realizar a consulta no MongoDB: {e}")
            return {"error": f"Erro ao consultar o MongoDB: {str(e)}"}
        except Exception as e:
            logging.error(f"Erro desconhecido ao realizar a consulta: {e}")
            return {"error": f"Ocorreu um erro ao realizar a consulta: {str(e)}"}