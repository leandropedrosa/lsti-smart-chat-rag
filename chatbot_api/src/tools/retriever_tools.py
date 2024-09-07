from langchain.agents import Tool
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings
from src.client.atlas_client import AtlasClient
from src.utils.async_utils import url_to_vector

import os

from src.models import docs

INDEX_NAME = os.getenv('ATLAS_INDEX_NAME')


class ToolDefinition:
    """
    Uma classe para definir ferramentas usadas em agentes LangChain.
    """

    def create_json_retriever(self, json_path: str, name: str, description: str) -> Tool:
        """
        Cria uma ferramenta de recuperação de JSON para o caminho especificado.
        """
        retriever_json = url_to_vector(file_name=json_path)
        return Tool(
            func=retriever_json.invoke,
            name=name,
            description=description
        )

    def create_page_retriever(self, page_url: str) -> Tool:
        """
        Cria uma ferramenta de recuperação de página para a URL especificada.
        """
        retriever_page = url_to_vector(url=page_url)
        return Tool(
            func=retriever_page.invoke,
            name="lcel_text",
            description="Use esta ferramenta para obter os termos referentes aos conhecimentos da página web."
        )

    def create_mongo_retriever(self) -> Tool:
        """
        Cria uma ferramenta de recuperação de JSON para o caminho especificado, retornando também os metadados dos documentos.
        """
        client = AtlasClient()

        vector_search = MongoDBAtlasVectorSearch.from_documents(
            documents=docs,
            embedding=OpenAIEmbeddings(),
            collection=client.get_collection(),
            index_name=INDEX_NAME
        )
        retriever = vector_search.as_retriever(search_type="similarity", search_kwargs={"k": 5})

        def retrieve_with_metadata(query):
            results = retriever.get_relevant_documents(query)

            metadata = [{"key": result.metadata.get("key", "No Key")} for result in results]

            response = {
                "results": results,
                "metadata": metadata
            }
            return response

        return Tool(
            func=retrieve_with_metadata,
            name="lcel_mongo_json",
            description="Use this tool to retrieve the terms present in the JSON file, including metadata"
        )