import os
import logging
import json
import os

from langchain_openai import ChatOpenAI
from langchain.memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import (
    create_openai_functions_agent,
    AgentExecutor,
)
from src.tools import ToolDefinition

instructions = (f"Você é um profissional assistente em questões encontrar qual o recurso do HL7 analisa o contexto fornecido; \n"
                f"IMPORTANTE: "
                f"Crie respostas curtas que somente respondam relacionando o recurso 'key' com o input do usuário"
                f"informações fornecidas e perguntadas, não se limite a somente um formato de resposta. " 
                f"responda de acordo com o tipo de input. ")

store = {}
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

class AgentManagerMongo:
    """
    Uma classe para gerenciar um agente sobre recursos do HL7 FHIR usando OpenAIAssistantV2Runnable e AgentExecutor.
    """

    def __init__(self):
        try:
            self.model = os.getenv("AGENT_MODEL", "gpt-3.5-turbo")
            self.api_key = os.getenv('OPENAI_API_KEY')
            if not self.api_key:
                raise ValueError("A chave de API da OpenAI não foi configurada.")

            self.tools = [ToolDefinition().create_mongo_retriever()]

            self.llm = ChatOpenAI(
                model=self.model,
                temperature=0,
                openai_api_key=self.api_key
            )

            self.prompt = ChatPromptTemplate.from_messages([
                ("system", instructions),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad")
            ])

            self.agent = create_openai_functions_agent(
                llm=self.llm,
                prompt=self.prompt,
                tools=self.tools,
            )

            self.agent_executor = AgentExecutor(
                agent=self.agent,
                tools=self.tools,
                return_intermediate_steps=True,
                verbose=True
            )

            self.memory = ChatMessageHistory(session_id="test-session")

            self.rag_agent_executor = RunnableWithMessageHistory(
                self.agent_executor,
                lambda session_id: self.memory,
                input_messages_key="input",
                history_messages_key="chat_history",
            )
        except Exception as e:
            logging.error(f"Erro na inicialização do AgentManagerMongo: {e}")
            raise

    async def execute(self, query: str, session_id: str):
        try:
            result = await self.rag_agent_executor.ainvoke(
            {
                "input": query
            }, config={"configurable": {"session_id": session_id}}
        )
            if "metadata" in result:
                metadata = result["metadata"]
                explanation = ", ".join([f'Document: {meta["key"]}' for meta in metadata])
                result["intermediate_steps"]["explanation"] = explanation

            return result
        except KeyError as e:
            logging.error(f"Chave ausente no resultado: {e}")
            return {"error": f"Erro de chave ao processar a resposta: {str(e)}"}
        except Exception as e:
            logging.error(f"Erro ao executar o agente: {e}")
            return {"error": f"Ocorreu um erro ao executar o agente: {str(e)}"}