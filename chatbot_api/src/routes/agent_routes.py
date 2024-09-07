from fastapi import APIRouter, HTTPException
from src.agents.mongo_agent import AgentManagerMongo
from src.models.rag_query import QueryInput, QueryOutput
from src.utils.async_utils import async_retry
import logging

# Configura o roteador FastAPI
router = APIRouter(
    prefix="/agent",
    tags=["AGENT"],
    responses={404: {"description": "Not found"}}
)

# Função para invocar o agente MongoDB com repetição em caso de falhas
@async_retry(max_retries=3, delay=1)
async def invoke_agent_mongo_with_retry(query: QueryInput):
    """
    Invoca o agente MongoDB com tentativas de repetição em caso de falhas.
    """
    try:
        manager = AgentManagerMongo()
        return await manager.execute(query.text, query.session_id)
    except Exception as e:
        logging.error(f"Erro ao invocar o agente MongoDB: {e}")
        raise HTTPException(status_code=500, detail="Erro ao processar a solicitação.")

# Rota POST para executar consultas no agente MongoDB
@router.post("/agent-mongo")
async def agent_mongo(query: QueryInput) -> QueryOutput:
    """
    Recebe uma query e invoca o agente MongoDB. Retorna a resposta ou erro.
    """
    try:
        query_response = await invoke_agent_mongo_with_retry(query)
        query_response["intermediate_steps"] = [
            str(s) for s in query_response["intermediate_steps"]
        ]
        return query_response
    except HTTPException as e:
        raise e
    except Exception as e:
        logging.error(f"Erro na rota /agent-mongo: {e}")
        raise HTTPException(status_code=500, detail="Erro ao executar a consulta.")