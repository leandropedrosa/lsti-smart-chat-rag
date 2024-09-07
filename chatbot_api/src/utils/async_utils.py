import asyncio
import requests
import os
from langchain_community.document_loaders import WebBaseLoader, JSONLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter

def async_retry(max_retries: int = 3, delay: int = 1):
    """
    Decora funções assíncronas para tentar novamente em caso de falhas.
    """
    def decorator(func):
        async def wrapper(*args, **kwargs):
            for attempt in range(1, max_retries + 1):
                try:
                    result = await func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Tentativa {attempt} falhou: {str(e)}")
                    await asyncio.sleep(delay)

            raise ValueError(f"Falha após {max_retries} tentativas")
        return wrapper
    return decorator

def read_json_from_url(url):
    """
    Busca dados JSON de uma URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança um erro para status HTTP de falha
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar JSON da URL: {e}")
        raise

def url_to_vector(url=None, file_name=None):
    """
    Converte dados de texto de uma URL ou arquivo JSON em vetores.
    """
    try:
        if url:
            loader = WebBaseLoader(url)
        elif file_name:
            base_path = os.path.dirname(__file__)
            json_file_path = os.path.join(base_path, "..", "data", file_name)
            loader = JSONLoader(jq_schema=".", file_path=json_file_path, text_content=False)
        else:
            raise ValueError("Nenhuma URL ou arquivo foi fornecido.")

        # Carrega e divide os documentos
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter()
        documents = text_splitter.split_documents(docs)

        # Cria o banco de dados vetorial
        reviews_vector_db = Chroma.from_documents(
            documents, OpenAIEmbeddings(openai_api_key=os.getenv('OPENAI_API_KEY')), persist_directory="chroma_data/"
        )

        return reviews_vector_db.as_retriever(k=10)
    except Exception as e:
        print(f"Erro ao converter URL ou arquivo para vetores: {e}")
        raise