from pydantic import BaseModel


class QueryInput(BaseModel):
    text: str
    session_id: str = None


class QueryOutput(BaseModel):
    input: str
    output: str
    intermediate_steps: list[str] = None
